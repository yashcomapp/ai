import { adminDb } from '@/lib/firebase/admin';
import { QuestionItem } from '@/types/question.types';
import { deriveTopicCodeFromQuestionCode } from '@/lib/questionTypes';

export class QuestionRepository {
  private static collection = adminDb.collection('questions');
  private static topicCache = new Map<string, { data: QuestionItem[]; expiry: number }>();

  /**
   * Retrieves a question by ID
   */
  static async getById(id: string): Promise<QuestionItem | null> {
    const doc = await this.collection.doc(id).get();
    if (!doc.exists) return null;
    return { id: doc.id, ...doc.data() } as QuestionItem;
  }

  /**
   * Fetch pagination count plus questions list
   */
  static async getPaginatedList(page: number, limitVal: number): Promise<{ questions: QuestionItem[]; total: number }> {
    const q = this.collection.orderBy('questionCode', 'asc');
    const offset = (page - 1) * limitVal;

    const [listSnap, totalSnap] = await Promise.all([
      q.offset(offset).limit(limitVal).get(),
      this.collection.count().get()
    ]);

    const questions = listSnap.docs.map(doc => ({ id: doc.id, ...doc.data() } as QuestionItem));
    const total = totalSnap.data().count;

    return { questions, total };
  }

  /**
   * Scan for duplicate questions by text mapping (select text only for low footprint)
   */
  static async getDuplicateGroups(
    limitVal = 10000,
    filters?: { board?: string; classNum?: string; subject?: string }
  ): Promise<{ text: string; questions: { questionCode: string; text: string; difficulty?: string; timesUsed?: number }[] }[]> {
    let query: FirebaseFirestore.Query = this.collection;

    if (filters?.board) {
      query = query.where('board', '==', filters.board);
    }
    if (filters?.classNum) {
      query = query.where('class', '==', filters.classNum);
    }
    if (filters?.subject) {
      query = query.where('subject', '==', filters.subject);
    }

    const snap = await query
      .select('questionCode', 'text', 'difficulty', 'timesUsed')
      .limit(limitVal)
      .get();

    const allQs = snap.docs.map(doc => ({ id: doc.id, ...doc.data() as any }));

    const normalizeForDeduplication = (str: string): string => {
      if (!str) return '';
      return String(str)
        // 1. Strip trailing question codes in parentheses, e.g. (MH-9-SCIT-16-16.1-OAR-003)
        .replace(/\s*\([A-Z0-9_\-\.]+\)\s*$/i, '')
        // 2. Normalize smart quotes and typographic dashes
        .replace(/[\u2018\u2019]/g, "'")
        .replace(/[\u201C\u201D]/g, '"')
        .replace(/[\u2013\u2014]/g, '-')
        // 3. Remove LaTeX display wrappers \( \) \[ \] $$ but keep the math content inside untouched
        .replace(/\\\(\s*/g, '')
        .replace(/\s*\\\)/g, '')
        .replace(/\\\[\s*/g, '')
        .replace(/\s*\\\]/g, '')
        .replace(/\$\$/g, '')
        .replace(/\$/g, '')
        // 4. Normalize spaces and trailing sentence punctuation
        .replace(/\s+/g, ' ')
        .replace(/[\s\.\?\!]+$/, '')
        .trim()
        .toLowerCase();
    };

    const groups: { [key: string]: any[] } = {};
    allQs.forEach(q => {
      if (!q.text) return;
      const normText = normalizeForDeduplication(q.text);
      if (!normText) return;
      if (!groups[normText]) {
        groups[normText] = [];
      }
      groups[normText].push({
        id: q.id,
        questionCode: q.questionCode || q.id,
        text: q.text,
        difficulty: q.difficulty,
        timesUsed: q.timesUsed || 0
      });
    });

    const duplicateGroups = Object.keys(groups)
      .filter(textKey => groups[textKey].length > 1)
      .map(textKey => ({
        text: groups[textKey][0].text,
        questions: groups[textKey]
      }));

    return duplicateGroups;
  }

  /**
   * Queries questions by topic Code (cascaded fallback) with memory cache
   */
  static async getQuestionsByTopic(topicCode: string): Promise<QuestionItem[]> {
    if (!topicCode) return [];

    const cached = this.topicCache.get(topicCode);
    if (cached && Date.now() < cached.expiry) {
      return cached.data;
    }

    const result = await this.resolveQuestionsByTopic(topicCode);
    // Cache for 5 minutes
    this.topicCache.set(topicCode, { data: result, expiry: Date.now() + 5 * 60 * 1000 });
    return result;
  }

  private static async resolveQuestionsByTopic(topicCode: string): Promise<QuestionItem[]> {
    // Path 1: canonical — questions saved with topicCode field
    try {
      const exact = await this.collection
        .where('topicCode', '==', topicCode)
        .limit(500)
        .get();
      if (!exact.empty) return exact.docs.map(d => ({ id: d.id, ...d.data() } as QuestionItem));
    } catch (e) {
      console.warn('getQuestionsByTopic: topicCode query failed', e);
    }
    // Path 1.5: query by prefix scan (for questions stored with topic code as prefix)
    const prefixScanResult = await this.queryByQuestionCodePrefix(topicCode);
    if (prefixScanResult.length > 0) return prefixScanResult;

    // Path 2: legacy docs that stored topic instead of topicCode
    try {
      const byTopic = await this.collection
        .where('topic', '==', topicCode)
        .limit(500)
        .get();
      if (!byTopic.empty) return byTopic.docs.map(d => ({ id: d.id, ...d.data() } as QuestionItem));
    } catch (e) {
      console.warn('getQuestionsByTopic: topic query failed', e);
    }

    // Helper parser to extract topic from questionCode in memory
    const parseCode = (qCode: string) => {
      return deriveTopicCodeFromQuestionCode(qCode);
    };

    // Path 3: robust subject prefix scan + in-memory matching (exact code only)
    try {
      const parts = topicCode.split('-');
      if (parts.length >= 3) {
        const subjectPrefix = `${parts[0]}-${parts[1]}-${parts[2]}-`;
        const nextPrefix = `${parts[0]}-${parts[1]}-${parts[2]}.`;
        const listSnap = await this.collection
          .where('questionCode', '>=', subjectPrefix)
          .where('questionCode', '<', nextPrefix)
          .limit(1000)
          .get();
          
        if (!listSnap.empty) {
          const matched: QuestionItem[] = [];
          listSnap.docs.forEach(doc => {
            const data = doc.data();
            const qCode = data.questionCode || '';
            if (parseCode(qCode) === topicCode) {
              matched.push({ id: doc.id, ...data } as QuestionItem);
            }
          });
          if (matched.length > 0) return matched;
        }
      }
    } catch (e) {
      console.warn('getQuestionsByTopic: subject prefix query and in-memory filter failed', e);
    }

    // Path 5: legacy range scan fallback
    try {
      const prefix = topicCode.replace(/-/g, '_').replace(/\./g, 'D') + '_';
      const charCode = prefix.charCodeAt(prefix.length - 1);
      const nextStr = prefix.slice(0, -1) + String.fromCharCode(charCode + 1);
      const byCode = await this.collection
        .where('questionCode', '>=', prefix)
        .where('questionCode', '<', nextStr)
        .limit(500)
        .get();
      if (!byCode.empty) return byCode.docs.map(d => ({ id: d.id, ...d.data() } as QuestionItem));
    } catch (e) {
      console.warn('getQuestionsByTopic: questionCode prefix scan failed', e);
    }

    return [];
  }

  private static async queryByQuestionCodePrefix(topicCode: string): Promise<QuestionItem[]> {
    try {
      const prefix = topicCode + '-';
      const nextStr = topicCode + '.';
      const byNewCode = await this.collection
        .where('questionCode', '>=', prefix)
        .where('questionCode', '<', nextStr)
        .limit(500)
        .get();
      if (!byNewCode.empty) return byNewCode.docs.map(d => ({ id: d.id, ...d.data() } as QuestionItem));
    } catch (e) {
      console.warn('getQuestionsByTopic: questionCode prefix scan failed', e);
    }
    return [];
  }
}
