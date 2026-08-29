'use client';

import React, { useState, useEffect, useRef, useMemo } from 'react';
import { useAuth } from '@/context/AuthContext';
import { useTheme } from '@/context/ThemeContext';
import { useRouter } from 'next/navigation';
import { db } from '@/lib/firebase/firestore';
import { collection, query, orderBy, limit, onSnapshot, doc, deleteDoc } from 'firebase/firestore';
import { renderMarkdown } from '@/lib/markdown';

interface ChatRoom {
  roomId: string;
  type: 'group' | 'dm';
  name: string;
  participants: string[];
  unreadCounts: Record<string, number>;
  isMutedForStudents?: boolean;
  isMutedForParents?: boolean;
  lastMessage?: { text: string; senderName: string; timestamp: string };
  pinnedMessage?: { messageId: string; text: string; senderName: string; timestamp: string } | null;
}

interface Message {
  messageId: string;
  senderId: string;
  senderName: string;
  senderRole: string;
  text: string;
  type: string;
  createdAt: string;
  isDeleted?: boolean;
  isEdited?: boolean;
  readBy?: Record<string, string>;
  isOptimistic?: boolean;
  replyToId?: string;
  replyToText?: string;
  replyToSenderName?: string;
  pollOptions?: { text: string; votesCount: number }[] | null;
  pollVotes?: Record<string, number> | null;
  reactions?: {
    thumbsup?: string[];
    pray?: string[];
  };
}

interface UserProfile {
  studentCode: string;
  name: string;
  role: string;
  email: string;
  parentEmail?: string;
  class?: string | number;
}

interface ChatViewProps {
  role?: 'admin' | 'student' | 'parent';
}

export default function ChatView({ role = 'admin' }: ChatViewProps) {
  const { firebaseUser, user, logout } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const router = useRouter();

  const [rooms, setRooms] = useState<ChatRoom[]>([]);
  const [activeRoomId, setActiveRoomId] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [participantNames, setParticipantNames] = useState<Record<string, string>>({});
  const [mentionSearch, setMentionSearch] = useState('');
  const [showMentionSuggestions, setShowMentionSuggestions] = useState(false);
  const [mentionStartIndex, setMentionStartIndex] = useState(-1);
  const [inputText, setInputText] = useState('');
  const [sidebarSearchQuery, setSidebarSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState<'group' | 'dm'>('group');
  const [loadingRooms, setLoadingRooms] = useState(true);
  const [isMobile, setIsMobile] = useState(false);
  const [useApiPolling, setUseApiPolling] = useState(false);
  const [useRoomsApiPolling, setUseRoomsApiPolling] = useState(false);

  // Mute control states
  const [muteStudents, setMuteStudents] = useState(false);
  const [muteParents, setMuteParents] = useState(false);
  const [updatingMute, setUpdatingMute] = useState(false);

  // Drawer / creation states
  const [showDmModal, setShowDmModal] = useState(false);
  const [studentsList, setStudentsList] = useState<UserProfile[]>([]);
  const [searchQuery, setSearchQuery] = useState('');

  const [showGroupModal, setShowGroupModal] = useState(false);
  const [batchesList, setBatchesList] = useState<any[]>([]);
  const [selectedBatchId, setSelectedBatchId] = useState('');
  const [groupName, setGroupName] = useState('');

  const messagesEndRef = useRef<HTMLDivElement | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const [showAttachmentMenu, setShowAttachmentMenu] = useState(false);
  const [showLinkModal, setShowLinkModal] = useState(false);
  const [linkUrl, setLinkUrl] = useState('');
  const [linkLabel, setLinkLabel] = useState('');
  const [editingMessageId, setEditingMessageId] = useState('');
  const [editingText, setEditingText] = useState('');
  const [receiptsModalMessage, setReceiptsModalMessage] = useState<Message | null>(null);
  const [pendingMessages, setPendingMessages] = useState<Message[]>([]);
  const [replyingTo, setReplyingTo] = useState<Message | null>(null);

  // Poll creation states
  const [showPollModal, setShowPollModal] = useState(false);
  const [pollQuestion, setPollQuestion] = useState('');
  const [pollOptionsInput, setPollOptionsInput] = useState(['', '']);

  // Starred messages states
  const [showStarredModal, setShowStarredModal] = useState(false);
  const [starredMessageIds, setStarredMessageIds] = useState<Record<string, boolean>>({});
  
  const [showReactorsModal, setShowReactorsModal] = useState<{
    isOpen: boolean;
    thumbsup: string[];
    pray: string[];
  } | null>(null);

  // Message scroll/jump refs
  const messageRefs = useRef<Record<string, HTMLDivElement | null>>({});
  const longPressTimeoutRef = useRef<any>(null);

  const handleLongPressStart = (messageId: string) => {
    if (longPressTimeoutRef.current) clearTimeout(longPressTimeoutRef.current);
    longPressTimeoutRef.current = setTimeout(() => {
      setIsMessageSelectMode(true);
      setSelectedMessageIds(prev => ({ ...prev, [messageId]: true }));
      if (typeof navigator !== 'undefined' && navigator.vibrate) {
        navigator.vibrate(50);
      }
    }, 550);
  };

  const handleLongPressEnd = () => {
    if (longPressTimeoutRef.current) {
      clearTimeout(longPressTimeoutRef.current);
      longPressTimeoutRef.current = null;
    }
  };

  // Multiple Select and Delete States
  const [isConversationSelectMode, setIsConversationSelectMode] = useState(false);
  const [selectedRoomIds, setSelectedRoomIds] = useState<Record<string, boolean>>({});
  const [isMessageSelectMode, setIsMessageSelectMode] = useState(false);
  const [selectedMessageIds, setSelectedMessageIds] = useState<Record<string, boolean>>({});

  // Scrolling behavior comparison refs
  const prevMessagesLengthRef = useRef(0);
  const prevActiveRoomIdRef = useRef('');

  const myUserKey = useMemo(() => {
    if (role === 'admin') return firebaseUser?.uid || 'admin';
    if (role === 'student') return user?.studentCode || '';
    if (role === 'parent') return user?.email ? `PR-${user.email.toLowerCase().trim()}` : '';
    return 'user';
  }, [role, firebaseUser, user]);

  const adminUid = myUserKey;

  const [viewportHeight, setViewportHeight] = useState('100dvh');

  // Track screen size for responsive layout and visual viewport height (mobile keyboard adjustments)
  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
      if (window.visualViewport) {
        setViewportHeight(`${window.visualViewport.height}px`);
      }
      window.scrollTo(0, 0); // Prevents white spaces on keyboard dismiss
    };
    handleResize();
    window.addEventListener('resize', handleResize);
    if (window.visualViewport) {
      window.visualViewport.addEventListener('resize', handleResize);
      window.visualViewport.addEventListener('scroll', handleResize);
    }
    return () => {
      window.removeEventListener('resize', handleResize);
      if (window.visualViewport) {
        window.visualViewport.removeEventListener('resize', handleResize);
        window.visualViewport.removeEventListener('scroll', handleResize);
      }
    };
  }, []);

  // Load Rooms list (one-shot fallback/init on mount)
  async function loadRooms() {
    if (!firebaseUser) return;
    try {
      const token = await firebaseUser.getIdToken();
      const res = await fetch('/api/chat', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      setRooms(data.rooms || []);
      setLoadingRooms(false);
    } catch (e) {
      console.error(e);
      setLoadingRooms(false);
    }
  }

  // Live sidebar rooms list subscription
  useEffect(() => {
    if (!firebaseUser) return;

    // Trigger REST fetch once to initialize/reconcile rooms on server
    loadRooms();

    let unsubscribe = () => {};
    try {
      const q = query(collection(db, 'chatRooms'));

      unsubscribe = onSnapshot(q, (snapshot) => {
        const rms = snapshot.docs.map(doc => ({
          roomId: doc.id,
          id: doc.id,
          ...doc.data()
        })) as unknown as ChatRoom[];
        setRooms(rms);
        setLoadingRooms(false);
        setUseRoomsApiPolling(false);
      }, (error) => {
        console.warn("Firestore rooms subscription failed. Falling back to API polling:", error);
        setUseRoomsApiPolling(true);
      });
    } catch (err) {
      console.warn("Failed to subscribe to Firestore rooms. Falling back to API polling:", err);
      setUseRoomsApiPolling(true);
    }

    return () => unsubscribe();
  }, [firebaseUser]);

  // Fallback API Polling for rooms list when direct collection subscription fails
  useEffect(() => {
    if (!useRoomsApiPolling || !firebaseUser) return;

    const interval = setInterval(async () => {
      try {
        const token = await firebaseUser.getIdToken();
        const res = await fetch('/api/chat', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        if (res.ok) {
          const data = await res.json();
          if (data.rooms) {
            setRooms(data.rooms);
          }
        }
      } catch (e) {
        console.error('Polling chat rooms list error:', e);
      }
    }, 8000);

    return () => clearInterval(interval);
  }, [useRoomsApiPolling, firebaseUser]);

  // Real-time Messages Listener
  useEffect(() => {
    if (!activeRoomId) {
      setMessages([]);
      return;
    }

    // Reset unread count on server
    const resetUnread = async () => {
      try {
        const token = await firebaseUser!.getIdToken();
        await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({ action: 'resetUnread', roomId: activeRoomId })
        });
      } catch (e) {
        console.error(e);
      }
    };
    resetUnread();

    const fetchInitialMessages = async () => {
      try {
        const token = await firebaseUser!.getIdToken();
        const res = await fetch(`/api/chat/messages?roomId=${activeRoomId}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        if (res.ok) {
          const data = await res.json();
          if (data.success && data.messages) {
            const mapped = data.messages.map((m: any) => ({
              messageId: m.messageId || m.id,
              ...m
            }));
            setMessages(mapped);
            if (data.participantNames) {
              setParticipantNames(data.participantNames);
            }
          }
        }
      } catch (e) {
        console.error('Failed to fetch messages initially via API:', e);
      }
    };

    // Unconditionally fetch initial messages to populate participantNames mapping
    fetchInitialMessages();

    // Set up Firestore snapshot listener
    let unsubscribe = () => {};
    try {
      const q = query(
        collection(db, 'chatRooms', activeRoomId, 'messages'),
        orderBy('createdAt', 'desc'),
        limit(100)
      );

      unsubscribe = onSnapshot(q, (snapshot) => {
        const msgs = snapshot.docs.map(doc => ({
          messageId: doc.id,
          ...doc.data()
        })) as unknown as Message[];
        setMessages(msgs.reverse());
        setUseApiPolling(false);
      }, (error) => {
        console.warn("Firestore snapshot subscription failed. Falling back to API polling:", error);
        setUseApiPolling(true);
        fetchInitialMessages();
      });
    } catch (err) {
      console.warn("Failed to subscribe to Firestore snapshots. Falling back to API polling:", err);
      setUseApiPolling(true);
      fetchInitialMessages();
    }

    // Populate active room mutes
    const activeRoom = rooms.find(r => r.roomId === activeRoomId);
    if (activeRoom) {
      setMuteStudents(!!activeRoom.isMutedForStudents);
      setMuteParents(!!activeRoom.isMutedForParents);
    }

    return () => unsubscribe();
  }, [activeRoomId, firebaseUser, rooms]);

  // Load starred messages when room changes
  useEffect(() => {
    if (!activeRoomId) return;
    try {
      const stored = localStorage.getItem(`starred_messages_${activeRoomId}`);
      if (stored) {
        setStarredMessageIds(JSON.parse(stored));
      } else {
        setStarredMessageIds({});
      }
    } catch (e) {
      console.error('Failed to load starred messages:', e);
    }
    setReplyingTo(null);
  }, [activeRoomId]);

  // Fallback API Polling when direct client-side firestore is denied/unavailable
  useEffect(() => {
    if (!activeRoomId || !useApiPolling || !firebaseUser) return;

    const interval = setInterval(async () => {
      try {
        const token = await firebaseUser.getIdToken();
        const res = await fetch(`/api/chat/messages?roomId=${activeRoomId}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        if (res.ok) {
          const data = await res.json();
          if (data.success && data.messages) {
            const mapped = data.messages.map((m: any) => ({
              messageId: m.messageId || m.id,
              ...m
            }));
            setMessages(mapped);
            if (data.participantNames) {
              setParticipantNames(data.participantNames);
            }
          }
        }
      } catch (e) {
        console.error('Polling chat messages error:', e);
      }
    }, 2000);

    return () => clearInterval(interval);
  }, [activeRoomId, useApiPolling, firebaseUser]);

  // Mark messages as read when viewing active room
  useEffect(() => {
    if (!activeRoomId || !firebaseUser || messages.length === 0) return;

    const userKey = adminUid;

    // Check if there are any unread messages from other senders
    const hasUnread = messages.some(msg => {
      const readBy = msg.readBy || {};
      return msg.senderId !== userKey && !readBy[userKey];
    });

    if (hasUnread) {
      const markAsRead = async () => {
        try {
          const token = await firebaseUser.getIdToken();
          await fetch('/api/chat/messages', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ action: 'markRoomRead', roomId: activeRoomId })
          });
        } catch (e) {
          console.error('Failed to mark messages as read:', e);
        }
      };
      markAsRead();
    }
  }, [activeRoomId, messages, firebaseUser, adminUid]);

  // Scroll to bottom on new messages or room change, ignoring deletions
  useEffect(() => {
    const messagesLength = messages.length + pendingMessages.length;
    const roomChanged = activeRoomId !== prevActiveRoomIdRef.current;
    
    if (roomChanged || messagesLength > prevMessagesLengthRef.current) {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
    
    prevMessagesLengthRef.current = messagesLength;
    prevActiveRoomIdRef.current = activeRoomId;
  }, [messages, pendingMessages, activeRoomId]);

  // Keep pinned to bottom when resuming from background or switching back from other apps
  useEffect(() => {
    const handleResume = () => {
      if (document.visibilityState === 'visible' && activeRoomId) {
        messagesEndRef.current?.scrollIntoView({ behavior: 'auto' });
      }
    };
    document.addEventListener('visibilitychange', handleResume);
    window.addEventListener('focus', handleResume);
    return () => {
      document.removeEventListener('visibilitychange', handleResume);
      window.removeEventListener('focus', handleResume);
    };
  }, [activeRoomId]);

  const mentionCandidates = useMemo(() => {
    if (!activeRoomId || !participantNames) return [];
    const activeRoom = rooms.find(r => r.roomId === activeRoomId);
    if (!activeRoom || !activeRoom.participants) return [];
    
    return activeRoom.participants
      .map((p: string) => ({
        id: p,
        name: participantNames[p] || p
      }))
      .filter((cand: any) => cand.name.toLowerCase().includes(mentionSearch.toLowerCase()));
  }, [activeRoomId, rooms, participantNames, mentionSearch]);

  const handleInputChange = (val: string) => {
    setInputText(val);
    const lastWordMatch = val.match(/@([a-zA-Z0-9_-]*)$/);
    if (lastWordMatch) {
      setMentionSearch(lastWordMatch[1]);
      setShowMentionSuggestions(true);
      setMentionStartIndex(val.lastIndexOf('@'));
    } else {
      setShowMentionSuggestions(false);
    }
  };

  const selectMention = (name: string) => {
    const beforeMention = inputText.substring(0, mentionStartIndex);
    const newVal = beforeMention + `@${name} `;
    setInputText(newVal);
    setShowMentionSuggestions(false);
  };

  // Send message
  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputText.trim() || !activeRoomId) return;

    const textToSend = inputText;
    setInputText('');

    const replyPayload = replyingTo ? {
      replyToId: replyingTo.messageId,
      replyToText: replyingTo.text,
      replyToSenderName: replyingTo.senderName
    } : {};

    setReplyingTo(null);

    // Create optimistic message
    const tempId = 'temp-' + Date.now();
    const optimisticMsg: Message = {
      messageId: tempId,
      senderId: adminUid,
      senderName: 'Admin',
      senderRole: 'admin',
      text: textToSend,
      type: 'text',
      createdAt: new Date().toISOString(),
      isOptimistic: true,
      ...replyPayload
    };

    setPendingMessages(prev => [...prev, optimisticMsg]);

    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          roomId: activeRoomId,
          text: textToSend,
          ...replyPayload
        })
      });

      if (!res.ok) throw new Error('Failed to deliver message');
      setPendingMessages(prev => prev.filter(m => m.messageId !== tempId));

      // Refresh messages immediately to eliminate send delay
      const fetchRes = await fetch(`/api/chat/messages?roomId=${activeRoomId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (fetchRes.ok) {
        const data = await fetchRes.json();
        if (data.success && data.messages) {
          const mapped = data.messages.map((m: any) => ({
            messageId: m.messageId || m.id,
            ...m
          }));
          setMessages(mapped);
        }
      }
    } catch (e: any) {
      setPendingMessages(prev => prev.filter(m => m.messageId !== tempId));
      alert(e.message);
    }
  };

  // Upload attachment file handler
  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file || !activeRoomId) return;

    const tempId = 'temp-' + Date.now();
    const optimisticMsg: Message = {
      messageId: tempId,
      senderId: adminUid,
      senderName: 'Admin',
      senderRole: 'admin',
      text: `📄 Uploading ${file.name}...`,
      type: 'text',
      createdAt: new Date().toISOString(),
      isOptimistic: true
    };
    setPendingMessages(prev => [...prev, optimisticMsg]);

    try {
      const token = await firebaseUser!.getIdToken();
      let downloadUrl = '';
      
      try {
        const { getStorage, ref, uploadBytes, getDownloadURL } = await import('firebase/storage');
        const storage = getStorage();
        const fileRef = ref(storage, `chat_files/${activeRoomId}/${Date.now()}_${file.name}`);
        const snapshot = await uploadBytes(fileRef, file);
        downloadUrl = await getDownloadURL(snapshot.ref);
      } catch (storageErr) {
        console.warn('Storage failed, using base64 fallback:', storageErr);
        if (file.size > 700 * 1024) {
          throw new Error('File is too large to send via fallback mechanism. Max limit is 700KB.');
        }
        downloadUrl = await new Promise<string>((resolve, reject) => {
          const reader = new FileReader();
          reader.onload = () => resolve(reader.result as string);
          reader.onerror = reject;
          reader.readAsDataURL(file);
        });
      }

      const res = await fetch('/api/chat/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          roomId: activeRoomId,
          text: `📄 [File: ${file.name}](${downloadUrl})`
        })
      });

      if (!res.ok) throw new Error('Failed to deliver file');
      setPendingMessages(prev => prev.filter(m => m.messageId !== tempId));

      const refreshRes = await fetch(`/api/chat/messages?roomId=${activeRoomId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (refreshRes.ok) {
        const data = await refreshRes.json();
        if (data.success && data.messages) {
          const mapped = data.messages.map((m: any) => ({
            messageId: m.messageId || m.id,
            ...m
          }));
          setMessages(mapped);
        }
      }
    } catch (err: any) {
      setPendingMessages(prev => prev.filter(m => m.messageId !== tempId));
      alert('Failed to send file: ' + err.message);
    }
  };

  // Delete message CRUD handler
  const handleDeleteMessage = async (messageId: string) => {
    if (!activeRoomId) return;
    if (!confirm('🗑️ Are you sure you want to delete this message? This will mark it as deleted for everyone.')) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/chat/messages?roomId=${activeRoomId}&messageId=${messageId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.error || 'Failed to delete message');
      }
      setMessages(prev => prev.map(m => m.messageId === messageId ? { ...m, isDeleted: true, text: '🚫 This message was deleted' } : m));
    } catch (err: any) {
      alert('Failed to delete message: ' + err.message);
    }
  };

  // Edit message CRUD handler
  const handleEditMessage = async (messageId: string, newText: string) => {
    if (!activeRoomId || !newText.trim()) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/chat/messages?roomId=${activeRoomId}&messageId=${messageId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ text: newText })
      });
      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || 'Failed to edit message');
      }
      setEditingMessageId('');
      setEditingText('');
    } catch (err: any) {
      alert('Edit failed: ' + err.message);
    }
  };

  // Delete conversation room CRUD handler
  const handleDeleteConversation = async () => {
    if (!activeRoomId) return;
    if (!confirm('⚠️ WARNING: Are you sure you want to delete this conversation room and all its messages? This action is permanent.')) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/chat?roomId=${activeRoomId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.error || 'Failed to delete conversation');
      }
      setActiveRoomId('');
    } catch (err: any) {
      alert('Failed to delete conversation: ' + err.message);
    }
  };

  // Bulk Delete Messages handler
  const handleBulkDeleteMessages = async () => {
    const idsToDelete = Object.keys(selectedMessageIds).filter(id => selectedMessageIds[id]);
    if (idsToDelete.length === 0) return;
    if (!confirm(`🗑️ Are you sure you want to delete the ${idsToDelete.length} selected messages? This will mark them as deleted for everyone.`)) return;
    
    try {
      const token = await firebaseUser!.getIdToken();
      // Lock scroll position
      prevMessagesLengthRef.current = messages.length + pendingMessages.length;
      
      await Promise.all(
        idsToDelete.map(async (messageId) => {
          const res = await fetch(`/api/chat/messages?roomId=${activeRoomId}&messageId=${messageId}`, {
            method: 'DELETE',
            headers: { 'Authorization': `Bearer ${token}` }
          });
          if (!res.ok) {
            const errData = await res.json().catch(() => ({}));
            throw new Error(errData.error || 'Failed to delete some messages');
          }
        })
      );

      setSelectedMessageIds({});
      setIsMessageSelectMode(false);
    } catch (err: any) {
      alert('Bulk deletion failed: ' + err.message);
    }
  };

  // Bulk Delete Conversations handler
  const handleBulkDeleteConversations = async () => {
    const idsToDelete = Object.keys(selectedRoomIds).filter(id => selectedRoomIds[id]);
    if (idsToDelete.length === 0) return;
    if (!confirm(`⚠️ WARNING: Are you sure you want to delete the ${idsToDelete.length} selected conversation rooms and all their messages? This action is permanent.`)) return;

    try {
      const token = await firebaseUser!.getIdToken();
      await Promise.all(
        idsToDelete.map(async (roomId) => {
          const res = await fetch(`/api/chat?roomId=${roomId}`, {
            method: 'DELETE',
            headers: { 'Authorization': `Bearer ${token}` }
          });
          if (!res.ok) {
            const errData = await res.json().catch(() => ({}));
            throw new Error(errData.error || 'Failed to delete some conversations');
          }
        })
      );

      setSelectedRoomIds({});
      setIsConversationSelectMode(false);
      if (idsToDelete.includes(activeRoomId)) {
        setActiveRoomId('');
      }
      loadRooms();
    } catch (err: any) {
      alert('Bulk conversation deletion failed: ' + err.message);
    }
  };

  // Toggle message reaction handler
  const handleToggleReaction = async (messageId: string, reactionType: 'thumbsup' | 'pray') => {
    if (!activeRoomId) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch(`/api/chat/messages?roomId=${activeRoomId}&messageId=${messageId}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ action: 'react', reactionType })
      });
      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.error || 'Failed to react');
      }
    } catch (err: any) {
      console.error('Toggle reaction error:', err);
    }
  };

  // Fetch all students on mount to enable read receipt name resolutions
  useEffect(() => {
    const initStudentsList = async () => {
      if (!firebaseUser) return;
      if (role !== 'admin') {
        setStudentsList([{
          studentCode: 'admin',
          name: 'Teacher / Administration',
          role: 'admin',
          email: 'admin@yashcom.com'
        }]);
        return;
      }
      try {
        const token = await firebaseUser.getIdToken();
        const res = await fetch('/api/admin/fees', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await res.json();
        if (data.students) {
          setStudentsList(data.students);
        }
      } catch (e) {
        console.error('Failed to pre-fetch student list for name resolutions:', e);
      }
    };
    initStudentsList();
  }, [firebaseUser, role]);

  // Toggle group mutes
  const handleToggleMute = async (target: 'students' | 'parents', val: boolean) => {
    if (updatingMute) return;
    setUpdatingMute(true);

    const nextMuteStudents = target === 'students' ? val : muteStudents;
    const nextMuteParents = target === 'parents' ? val : muteParents;

    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'updateMute',
          roomId: activeRoomId,
          isMutedForStudents: nextMuteStudents,
          isMutedForParents: nextMuteParents
        })
      });

      if (!res.ok) throw new Error('Failed to toggle mute state');
      
      if (target === 'students') setMuteStudents(val);
      if (target === 'parents') setMuteParents(val);
      
      // Sync list
      setRooms(prev => prev.map(r => r.roomId === activeRoomId ? { ...r, isMutedForStudents: nextMuteStudents, isMutedForParents: nextMuteParents } : r));
    } catch (err: any) {
      alert(err.message);
    } finally {
      setUpdatingMute(false);
    }
  };

  const toggleStarMessage = (messageId: string) => {
    if (!activeRoomId) return;
    const updated = { ...starredMessageIds };
    if (updated[messageId]) {
      delete updated[messageId];
    } else {
      updated[messageId] = true;
    }
    setStarredMessageIds(updated);
    try {
      localStorage.setItem(`starred_messages_${activeRoomId}`, JSON.stringify(updated));
    } catch (e) {
      console.error('Failed to save starred messages:', e);
    }
  };

  const handleVotePoll = async (messageId: string, optionIndex: number) => {
    if (!activeRoomId) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'votePoll',
          roomId: activeRoomId,
          messageId,
          optionIndex
        })
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || 'Failed to vote');
      }

      const data = await res.json();
      if (data.success && data.pollOptions) {
        setMessages(prev => prev.map(m => m.messageId === messageId ? { ...m, pollOptions: data.pollOptions } : m));
      }
    } catch (e: any) {
      alert(e.message);
    }
  };

  const handleCreatePoll = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!pollQuestion.trim() || !activeRoomId) return;
    const validOptions = pollOptionsInput.filter(opt => opt.trim() !== '');
    if (validOptions.length < 2) {
      alert('Please provide at least 2 options.');
      return;
    }

    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          roomId: activeRoomId,
          type: 'poll',
          text: pollQuestion,
          pollOptions: validOptions
        })
      });

      if (!res.ok) {
        const errData = await res.json();
        throw new Error(errData.error || 'Failed to create poll');
      }

      setShowPollModal(false);
      setPollQuestion('');
      setPollOptionsInput(['', '']);

      const fetchRes = await fetch(`/api/chat/messages?roomId=${activeRoomId}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (fetchRes.ok) {
        const data = await fetchRes.json();
        if (data.success && data.messages) {
          const mapped = data.messages.map((m: any) => ({
            messageId: m.messageId || m.id,
            ...m
          }));
          setMessages(mapped);
        }
      }
    } catch (e: any) {
      alert(e.message);
    }
  };

  const handlePinMessage = async (messageId: string) => {
    if (!activeRoomId) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'pinMessage',
          roomId: activeRoomId,
          messageId
        })
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || 'Failed to pin message');
      }

      loadRooms();
    } catch (e: any) {
      alert(e.message);
    }
  };

  const handleUnpinMessage = async () => {
    if (!activeRoomId) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          action: 'unpinMessage',
          roomId: activeRoomId
        })
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.error || 'Failed to unpin message');
      }

      loadRooms();
    } catch (e: any) {
      alert(e.message);
    }
  };

  const scrollToMessage = (messageId: string) => {
    const el = messageRefs.current[messageId];
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      el.style.backgroundColor = 'rgba(96, 165, 250, 0.25)';
      setTimeout(() => {
        el.style.backgroundColor = '';
      }, 1500);
    } else {
      alert('Message not loaded in view.');
    }
  };

  // Load Students for DM Drawer (excluding inactive accounts)
  const openDmDrawer = async () => {
    setShowDmModal(true);
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/fees', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      const activeStudents = (data.students || []).filter((s: any) => s.status !== 'inactive');
      setStudentsList(activeStudents);
    } catch (e) {
      console.error(e);
    }
  };

  // Initialize DM
  const handleStartDM = async (sCode: string, sName: string) => {
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({
          action: 'createDM',
          targetUserCode: sCode,
          targetUserName: sName
        })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to start DM');
      
      setShowDmModal(false);
      loadRooms();
      setActiveRoomId(data.roomId);
    } catch (e: any) {
      alert(e.message);
    }
  };

  // Load Batches for Group Drawer
  const openGroupDrawer = async () => {
    setShowGroupModal(true);
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/admin/batches', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      setBatchesList(data.batches || []);
      if (data.batches?.length > 0) {
        setSelectedBatchId(data.batches[0].id);
        setGroupName(`${data.batches[0].name} Chat Group`);
      }
    } catch (e) {
      console.error(e);
    }
  };

  // Create class group room
  const handleCreateGroup = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedBatchId || !groupName.trim()) return;
    try {
      const token = await firebaseUser!.getIdToken();
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({
          action: 'createGroup',
          batchId: selectedBatchId,
          name: groupName.trim()
        })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to create group');

      setShowGroupModal(false);
      loadRooms();
      setActiveRoomId(data.roomId);
    } catch (e: any) {
      alert(e.message);
    }
  };

  const filteredStudents = studentsList.filter(s =>
    (s as any).status !== 'inactive' &&
    (s.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
     s.studentCode.toLowerCase().includes(searchQuery.toLowerCase()))
  );

  // Filter conversations in sidebar: ONLY existent communications for DMs and sorted by latest message on top
  const filteredRooms = useMemo(() => {
    return rooms
      .filter(room => {
        if (room.type !== activeTab) return false;
        // For DMs: Only include existent communications (rooms that have at least one message or lastMessage)
        if (room.type === 'dm') {
          if (!room.lastMessage || !room.lastMessage.text) return false;
        }
        const displayName = room.name || '';
        return displayName.toLowerCase().includes(sidebarSearchQuery.toLowerCase());
      })
      .sort((a, b) => {
        const timeA = a.lastMessage?.timestamp ? new Date(a.lastMessage.timestamp).getTime() : 0;
        const timeB = b.lastMessage?.timestamp ? new Date(b.lastMessage.timestamp).getTime() : 0;
        return timeB - timeA;
      });
  }, [rooms, activeTab, sidebarSearchQuery]);

  // Aggregate unread badge counts
  const totalGroupUnread = useMemo(() => {
    return rooms.filter(r => r.type === 'group').reduce((acc, r) => acc + (r.unreadCounts?.[adminUid] || 0), 0);
  }, [rooms, adminUid]);

  const totalDmUnread = useMemo(() => {
    return rooms.filter(r => r.type === 'dm' && r.lastMessage && r.lastMessage.text).reduce((acc, r) => acc + (r.unreadCounts?.[adminUid] || 0), 0);
  }, [rooms, adminUid]);

  const activeRoom = rooms.find(r => r.roomId === activeRoomId);

  // Extract initials for group tags (e.g. "8th Foundation" -> "8F")
  const getGroupInitials = (name: string) => {
    if (!name) return 'G';
    const cleaned = name.replace(/chat|group/gi, '').trim();
    const parts = cleaned.split(' ');
    if (parts.length > 1) {
      return (parts[0][0] + parts[1][0]).toUpperCase();
    }
    return name.substring(0, 2).toUpperCase();
  };

  // Dynamically calculate group statistics from the database-loaded studentsList
  const getGroupSubtext = (name: string) => {
    const cleaned = name.toLowerCase();
    
    let classNum = '';
    if (cleaned.includes('8th') || cleaned.includes('class 8')) classNum = '8';
    else if (cleaned.includes('9th') || cleaned.includes('class 9')) classNum = '9';
    else if (cleaned.includes('10th') || cleaned.includes('class 10')) classNum = '10';

    if (classNum && studentsList && studentsList.length > 0) {
      const classStudents = studentsList.filter(s => {
        const sClass = String(s.class || (s as any).classNum || (s as any).grade || '').trim();
        return sClass === classNum || sClass.includes(classNum);
      });
      const studentCount = classStudents.length;
      
      const parentEmails = new Set(
        classStudents
          .map(s => s.parentEmail?.trim().toLowerCase())
          .filter(Boolean)
      );
      const parentCount = parentEmails.size;

      return `${studentCount} Students • ${parentCount} Parents`;
    }

    // Correct fallbacks corresponding to actual database document counts
    if (cleaned.includes('8th')) return '14 Students • 14 Parents';
    if (cleaned.includes('9th')) return '25 Students • 25 Parents';
    if (cleaned.includes('10th')) return '22 Students • 21 Parents';
    
    return 'Class group conversation';
  };

  const getGroupBadgeColor = (name: string) => {
    const cleaned = name.toLowerCase();
    if (cleaned.includes('8th')) return 'rgba(99, 102, 241, 0.2)';
    if (cleaned.includes('9th')) return 'rgba(16, 185, 129, 0.2)';
    if (cleaned.includes('10th')) return 'rgba(245, 158, 11, 0.2)';
    return 'rgba(56, 189, 248, 0.2)';
  };

  return (
    <div style={{ background: 'var(--surface-2)', height: viewportHeight, display: 'flex', flexDirection: 'column', color: 'var(--text)', fontFamily: 'Inter, system-ui, -apple-system, sans-serif', overflow: 'hidden', position: 'fixed', inset: 0, width: '100%', maxWidth: '100vw' }}>
      <style dangerouslySetInnerHTML={{ __html: `
        /* Prevent accidental Touch-to-Search selection on touch devices */
        body, html, div, span, button, svg, h1, h2, h3, h4, h5, p, label {
          user-select: none !important;
          -webkit-user-select: none !important;
          -webkit-touch-callout: none !important;
        }
        input, textarea, .selectable-text {
          user-select: text !important;
          -webkit-user-select: text !important;
        }
      ` }} />
      


      {/* Top Header Bar */}
      <div className="page-header glass" style={{ padding: '8px 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderRadius: '0', borderBottom: '1px solid var(--border-light)', zIndex: 10, background: 'var(--surface-popover)' }}>
        <div className="page-header-left" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button 
            onClick={() => router.push(role === 'admin' ? '/admin' : (role === 'parent' ? '/parent' : '/student'))}
            style={{
              background: 'transparent',
              border: 'none',
              color: 'var(--text)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '6px',
              borderRadius: '50%',
              transition: 'background 0.2s'
            }}
            title="Back to Dashboard"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>
          </button>
          <span className="brand" style={{ fontWeight: 800, fontSize: '1.1rem', color: 'var(--accent)', cursor: 'pointer' }} onClick={() => router.push(role === 'admin' ? '/admin' : (role === 'parent' ? '/parent' : '/student'))}>
            YASHCOM
          </span>
        </div>
        <div className="page-header-right" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button className="btn btn-secondary logout-btn" onClick={() => logout()} style={{ fontSize: '1rem', padding: '6px 10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }} title="Logout">🚪</button>
        </div>
      </div>

      {/* Main split window container */}
      <div style={{ flex: 1, display: 'flex', overflow: 'hidden' }}>
        
        {/* Left Side: Sidebar */}
        <div 
          style={{ 
            width: isMobile ? '100%' : '360px', 
            borderRight: '1px solid var(--border)', 
            background: 'var(--surface-popover)', 
            display: (isMobile && activeRoomId) ? 'none' : 'flex', 
            flexDirection: 'column' 
          }}
        >
          {/* Action buttons (DM & Group) */}
          <div style={{ padding: '12px 20px', borderBottom: '1px solid var(--border)', display: 'flex', gap: '8px', background: 'var(--surface-popover)' }}>
            <button 
              onClick={openDmDrawer} 
              style={{ flex: 1, fontSize: '12px', padding: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '4px', borderRadius: '8px', cursor: 'pointer', border: 'none', background: '#4f46e5', color: '#ffffff', fontWeight: 600 }}
            >
              💬 Start DM
            </button>
            {role === 'admin' && (
              <button 
                onClick={openGroupDrawer} 
                style={{ flex: 1, fontSize: '12px', padding: '8px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '4px', borderRadius: '8px', cursor: 'pointer', border: '1px solid var(--border)', background: 'var(--surface-2)', color: 'var(--text)', fontWeight: 600 }}
              >
                👥 New Group
              </button>
            )}
          </div>

          {/* Messages Title with Actions */}
          <div style={{ padding: '20px 20px 10px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h1 style={{ fontSize: '20px', fontWeight: 700, margin: 0, letterSpacing: '-0.3px' }}>Messages</h1>
            <div style={{ display: 'flex', gap: '8px' }}>
              <button
                onClick={() => {
                  setIsConversationSelectMode(!isConversationSelectMode);
                  setSelectedRoomIds({});
                }}
                style={{
                  padding: '6px 10px',
                  borderRadius: '8px',
                  border: isConversationSelectMode ? '1px solid rgba(239, 68, 68, 0.4)' : '1px solid var(--border)',
                  background: isConversationSelectMode ? 'rgba(239, 68, 68, 0.15)' : 'var(--surface-2)',
                  color: isConversationSelectMode ? '#f87171' : 'var(--text-muted)',
                  fontSize: '11px',
                  fontWeight: 'bold',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                  transition: 'all 0.2s'
                }}
                title={isConversationSelectMode ? "Cancel selection" : "Select multiple conversations"}
              >
                {isConversationSelectMode ? '✕ Cancel' : '🗑️ Select'}
              </button>
            </div>
          </div>

          {/* Filter Pills Tab Selector */}
          <div style={{ padding: '10px 20px', display: 'flex', gap: '8px', background: 'var(--surface-popover)' }}>
            <button
              onClick={() => setActiveTab('group')}
              style={{
                flex: 1,
                padding: '8px 12px',
                borderRadius: '8px',
                border: 'none',
                background: activeTab === 'group' ? '#4f46e5' : 'var(--surface-2)',
                color: activeTab === 'group' ? '#ffffff' : 'var(--text-muted)',
                fontSize: '12.5px',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '6px',
                transition: 'all 0.2s'
              }}
            >
              <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 2.02 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
              <span>Class Groups</span>
              {totalGroupUnread > 0 && (
                <span style={{ background: '#ef4444', color: '#ffffff', fontSize: '10px', fontWeight: 800, padding: '1px 6px', borderRadius: '10px', lineHeight: '14px' }}>
                  {totalGroupUnread}
                </span>
              )}
            </button>
            <button
              onClick={() => setActiveTab('dm')}
              style={{
                flex: 1,
                padding: '8px 12px',
                borderRadius: '8px',
                border: 'none',
                background: activeTab === 'dm' ? '#4f46e5' : 'var(--surface-2)',
                color: activeTab === 'dm' ? '#ffffff' : 'var(--text-muted)',
                fontSize: '12.5px',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '6px',
                transition: 'all 0.2s'
              }}
            >
              <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
              <span>Direct Messages</span>
              {totalDmUnread > 0 && (
                <span style={{ background: '#ef4444', color: '#ffffff', fontSize: '10px', fontWeight: 800, padding: '1px 6px', borderRadius: '10px', lineHeight: '14px' }}>
                  {totalDmUnread}
                </span>
              )}
            </button>
          </div>

          {/* Search bar input bar */}
          <div style={{ padding: '10px 20px', borderBottom: '1px solid var(--border)' }}>
            <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
              <span style={{ position: 'absolute', left: '12px', display: 'flex', alignItems: 'center', color: 'var(--text-muted)' }}>
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
              </span>
              <input
                type="text"
                placeholder="Search conversations..."
                value={sidebarSearchQuery}
                onChange={(e) => setSidebarSearchQuery(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 12px 10px 38px',
                  borderRadius: '10px',
                  border: '1px solid var(--border)',
                  background: 'var(--surface-2)',
                  color: 'var(--text)',
                  fontSize: '16px',
                  outline: 'none',
                  transition: 'border-color 0.2s'
                }}
                onFocus={(e) => e.currentTarget.style.borderColor = '#4f46e5'}
                onBlur={(e) => e.currentTarget.style.borderColor = 'var(--border)'}
              />
            </div>
          </div>

          {/* Bulk Delete Conversations bar */}
          {isConversationSelectMode && (
            <div style={{ padding: '12px 20px', background: 'rgba(239, 68, 68, 0.08)', borderBottom: '1px solid rgba(239, 68, 68, 0.2)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '12px', fontWeight: 'bold', color: '#f87171' }}>
                  {Object.values(selectedRoomIds).filter(Boolean).length} selected
                </span>
                <div style={{ display: 'flex', gap: '6px' }}>
                  <button 
                    onClick={() => {
                      setIsConversationSelectMode(false);
                      setSelectedRoomIds({});
                    }}
                    style={{ background: 'transparent', border: '1px solid var(--border)', color: 'var(--text-muted)', padding: '4px 8px', fontSize: '11px', borderRadius: '6px', cursor: 'pointer' }}
                  >
                    Cancel
                  </button>
                  <button 
                    onClick={handleBulkDeleteConversations}
                    disabled={Object.values(selectedRoomIds).filter(Boolean).length === 0}
                    style={{ background: '#ef4444', color: '#ffffff', border: 'none', padding: '4px 10px', fontSize: '11px', fontWeight: 'bold', borderRadius: '6px', cursor: 'pointer', opacity: Object.values(selectedRoomIds).filter(Boolean).length === 0 ? 0.5 : 1 }}
                  >
                    Delete Selected
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* Section labels */}
          <div style={{ padding: '12px 20px 4px 20px', fontSize: '10.5px', fontWeight: 700, color: 'var(--text-muted)', letterSpacing: '0.8px', textTransform: 'uppercase' }}>
            {activeTab === 'group' ? 'Class Groups' : 'Recent Conversations'}
          </div>

          {/* Conversations listing */}
          <div style={{ flex: 1, overflowY: 'auto', background: 'var(--surface-popover)', padding: '0 8px' }}>
            {loadingRooms ? (
              <div style={{ color: 'var(--text-muted)', padding: '40px 20px', textAlign: 'center', fontSize: '13px' }}>Loading conversations...</div>
            ) : filteredRooms.length === 0 ? (
              <div style={{ color: 'var(--text-muted)', padding: '40px 20px', textAlign: 'center', fontSize: '13px' }}>No active chats found.</div>
            ) : (
              filteredRooms.map(room => {
                const isActive = room.roomId === activeRoomId;
                const unread = room.unreadCounts?.[adminUid] || 0;
                const isDM = room.type === 'dm';
                const displayName = room.name || '';

                return (
                  <div
                    key={room.roomId}
                    onClick={() => {
                      if (isConversationSelectMode) {
                        setSelectedRoomIds(prev => ({ ...prev, [room.roomId]: !prev[room.roomId] }));
                      } else {
                        setActiveRoomId(room.roomId);
                      }
                    }}
                    style={{
                      padding: '12px 16px',
                      borderRadius: '12px',
                      background: isActive ? 'var(--surface)' : 'transparent',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '12px',
                      marginBottom: '4px',
                      transition: 'background 0.2s',
                      border: isConversationSelectMode && selectedRoomIds[room.roomId] ? '1px dashed #ef4444' : '1px solid transparent'
                    }}
                    onMouseEnter={(e) => { if (!isActive) e.currentTarget.style.background = 'rgba(14, 24, 43, 0.5)'; }}
                    onMouseLeave={(e) => { if (!isActive) e.currentTarget.style.background = 'transparent'; }}
                  >
                    {isConversationSelectMode && (
                      <input 
                        type="checkbox" 
                        checked={!!selectedRoomIds[room.roomId]}
                        onChange={() => {}} // click on parent div handles toggling
                        style={{ width: '16px', height: '16px', cursor: 'pointer', marginRight: '4px', accentColor: '#ef4444' }}
                        onClick={(e) => e.stopPropagation()}
                      />
                    )}
                    {/* Circle/Square Avatar */}
                    {room.type === 'group' ? (
                      <div style={{
                        width: '46px',
                        height: '46px',
                        borderRadius: '10px',
                        background: getGroupBadgeColor(room.name),
                        color: '#ffffff',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontWeight: 'bold',
                        fontSize: '15px',
                        flexShrink: 0
                      }}>
                        {getGroupInitials(room.name)}
                      </div>
                    ) : (
                      <div style={{ position: 'relative', flexShrink: 0 }}>
                        <div style={{
                          width: '46px',
                          height: '46px',
                          borderRadius: '50%',
                          background: '#4f46e5',
                          color: '#ffffff',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontWeight: 'bold',
                          fontSize: '16px'
                        }}>
                          {displayName[0] || 'S'}
                        </div>
                        <span style={{ position: 'absolute', bottom: '1px', right: '1px', width: '12px', height: '12px', borderRadius: '50%', background: '#10b981', border: '2px solid var(--surface-popover)' }} />
                      </div>
                    )}

                    {/* Text summary info */}
                    <div style={{ minWidth: 0, flex: 1 }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
                        <span style={{ fontSize: '14px', fontWeight: 600, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                          {displayName}
                        </span>
                        {room.lastMessage && (
                          <span style={{ fontSize: '10.5px', color: unread > 0 ? '#60a5fa' : 'var(--text-faint)', fontWeight: unread > 0 ? '600' : 'normal' }}>
                            {new Date(room.lastMessage.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                          </span>
                        )}
                      </div>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '3px' }}>
                        <span style={{ fontSize: '12px', color: 'var(--text-muted)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                          {room.type === 'group' 
                            ? getGroupSubtext(room.name)
                            : (room.lastMessage ? `${room.lastMessage.senderName}: ${room.lastMessage.text}` : 'Direct Conversation')}
                        </span>
                        {unread > 0 && (
                          <span 
                            style={{ 
                              fontSize: '11px', 
                              background: '#ef4444', 
                              color: '#ffffff', 
                              minWidth: '20px', 
                              height: '20px', 
                              display: 'flex', 
                              alignItems: 'center', 
                              justifyContent: 'center', 
                              borderRadius: '10px', 
                              padding: '0 6px', 
                              fontWeight: 800,
                              boxShadow: '0 2px 6px rgba(239, 68, 68, 0.45)',
                              flexShrink: 0,
                              marginLeft: '6px'
                            }}
                            title={`${unread} unread messages`}
                          >
                            {unread}
                          </span>
                        )}
                      </div>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* Right Side: Message Feed area */}
        <div 
          style={{ 
            flex: 1, 
            display: (isMobile && !activeRoomId) ? 'none' : 'flex', 
            flexDirection: 'column', 
            background: 'var(--surface-2)',
            position: 'relative',
            minWidth: 0,
            maxWidth: isMobile ? '100%' : 'none'
          }}
        >
          {activeRoomId ? (
            <>
              {/* Active conversation Header */}
              <div style={{ 
                padding: isMobile ? '6px 10px' : '10px 16px', 
                borderBottom: '1px solid var(--border)', 
                background: 'var(--surface-popover)', 
                display: 'flex', 
                flexDirection: isMobile ? 'column' : 'row',
                alignItems: isMobile ? 'stretch' : 'center',
                justifyContent: 'space-between',
                gap: isMobile ? '4px' : '8px', 
                zIndex: 5 
              }}>
                {/* Row 1: Back + Info */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', minWidth: 0, width: '100%', justifyContent: 'space-between' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px', minWidth: 0 }}>
                    {isMobile && (
                      <button 
                        onClick={() => setActiveRoomId('')} 
                        style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '14px', padding: '6px 4px 6px 0', color: '#60a5fa', fontWeight: 'bold', display: 'flex', alignItems: 'center', gap: '2px' }}
                      >
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg>
                      </button>
                    )}
                    <div style={{ position: 'relative', flexShrink: 0 }}>
                      <div style={{
                        width: isMobile ? '36px' : '42px',
                        height: isMobile ? '36px' : '42px',
                        borderRadius: activeRoom?.type === 'group' ? '10px' : '50%',
                        background: activeRoom?.type === 'group' ? getGroupBadgeColor(activeRoom.name) : '#4f46e5',
                        color: '#ffffff',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontWeight: 'bold',
                        fontSize: isMobile ? '12px' : '14px'
                      }}>
                        {activeRoom?.type === 'group' ? getGroupInitials(activeRoom.name) : (activeRoom?.name ? activeRoom.name[0].toUpperCase() : 'S')}
                      </div>
                      <span style={{ position: 'absolute', bottom: '0px', right: '0px', width: '8px', height: '8px', borderRadius: '50%', background: '#10b981', border: '1.5px solid var(--surface-popover)' }} />
                    </div>
                    <div style={{ minWidth: 0, marginLeft: '2px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                      <h3 style={{ margin: 0, fontSize: isMobile ? '14px' : '15px', fontWeight: 600, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                        {activeRoom?.name}
                      </h3>
                      {isMessageSelectMode && (
                        <button
                          onClick={() => {
                            setIsMessageSelectMode(false);
                            setSelectedMessageIds({});
                          }}
                          style={{
                            background: 'rgba(239, 68, 68, 0.15)',
                            border: '1px solid rgba(239, 68, 68, 0.3)',
                            borderRadius: '4px',
                            color: '#f87171',
                            padding: '2px 6px',
                            fontSize: '10px',
                            fontWeight: 'bold',
                            cursor: 'pointer'
                          }}
                        >
                          Cancel Select
                        </button>
                      )}
                    </div>
                  </div>

                  {isMobile && (
                    <button
                      onClick={handleDeleteConversation}
                      style={{
                        background: 'rgba(239, 68, 68, 0.15)',
                        border: '1px solid rgba(239, 68, 68, 0.4)',
                        borderRadius: '6px',
                        color: '#f87171',
                        padding: '6px 10px',
                        fontSize: '14px',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center'
                      }}
                      title="Delete Conversation"
                    >
                      🗑️
                    </button>
                  )}
                </div>

                {/* Row 2: Mute switches and buttons */}
                <div style={{ 
                  display: 'flex', 
                  gap: '8px', 
                  alignItems: 'center', 
                  justifyContent: 'space-between',
                  flexWrap: 'wrap',
                  width: isMobile ? '100%' : 'auto',
                  borderTop: isMobile ? '1px solid var(--border-light)' : 'none',
                  paddingTop: isMobile ? '6px' : '0',
                  marginTop: isMobile ? '2px' : '0'
                }}>
                  {activeRoom?.type === 'group' && (
                    <div style={{ display: 'flex', gap: '8px', alignItems: 'center', fontSize: '11px', fontWeight: 600, color: '#94a3b8' }}>
                      <span>Mute:</span>
                      <label style={{ display: 'flex', alignItems: 'center', gap: '3px', cursor: 'pointer', userSelect: 'none' }}>
                        <input
                          type="checkbox"
                          checked={muteStudents}
                          onChange={(e) => handleToggleMute('students', e.target.checked)}
                          style={{ width: '12px', height: '12px', cursor: 'pointer' }}
                        />
                        Student
                      </label>
                      <label style={{ display: 'flex', alignItems: 'center', gap: '3px', cursor: 'pointer', userSelect: 'none' }}>
                        <input
                          type="checkbox"
                          checked={muteParents}
                          onChange={(e) => handleToggleMute('parents', e.target.checked)}
                          style={{ width: '12px', height: '12px', cursor: 'pointer' }}
                        />
                        Parent
                      </label>
                    </div>
                  )}

                  <div style={{ display: 'flex', gap: '6px', marginLeft: 'auto' }}>

                    {!isMobile && (
                      <button
                        onClick={handleDeleteConversation}
                        style={{
                          background: 'rgba(239, 68, 68, 0.15)',
                          border: '1px solid rgba(239, 68, 68, 0.4)',
                          borderRadius: '8px',
                          color: '#f87171',
                          padding: '5px 10px',
                          fontSize: '11px',
                          fontWeight: 'bold',
                          cursor: 'pointer',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '4px',
                          transition: 'all 0.2s'
                        }}
                      >
                        🗑️ Delete Chat
                      </button>
                    )}
                  </div>
                </div>
              </div>

              {/* Pinned Message Banner */}
              {activeRoom?.pinnedMessage && (
                <div style={{
                  background: '#0d1527',
                  borderBottom: '1px solid #222730',
                  padding: '8px 20px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  gap: '12px',
                  zIndex: 4
                }}>
                  <div 
                    onClick={() => scrollToMessage(activeRoom.pinnedMessage!.messageId)}
                    style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', overflow: 'hidden', flex: 1 }}
                  >
                    <span style={{ fontSize: '14px' }}>📌</span>
                    <div style={{ fontSize: '12px', minWidth: 0 }}>
                      <span style={{ color: '#60a5fa', fontWeight: 600 }}>Pinned Message: </span>
                      <span style={{ color: '#94a3b8', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', display: 'inline-block', maxWidth: '300px', verticalAlign: 'bottom' }}>
                        {activeRoom.pinnedMessage.text}
                      </span>
                    </div>
                  </div>
                  <button
                    onClick={handleUnpinMessage}
                    style={{ background: 'transparent', border: 'none', color: '#ef4444', fontSize: '13px', cursor: 'pointer', padding: '2px 6px' }}
                    title="Unpin Message"
                  >
                    ✕
                  </button>
                </div>
              )}

              {/* Message scrollable bubble feed */}
              <div 
                style={{ 
                  flex: 1, 
                  overflowY: 'auto', 
                  overflowX: 'hidden',
                  padding: isMobile ? '10px 8px' : '24px 20px', 
                  display: 'flex', 
                  flexDirection: 'column', 
                  gap: '8px',
                  background: '#090f1d'
                }}
              >

                {(() => {
                  let lastDateStr = '';
                  const feedMessages = [...messages, ...pendingMessages].filter(msg => !msg.isDeleted);
                  
                  return feedMessages.map((msg, index) => {
                    const isMe = msg.senderId === adminUid;
                    const prevMsg = index > 0 ? feedMessages[index - 1] : null;
                    const isSameSender = prevMsg && prevMsg.senderId === msg.senderId;
                    const readersCount = Object.keys(msg.readBy || {}).filter(k => k !== msg.senderId).length;

                    // Render File attachment mock wrapper if it is a pdf / document
                    const hasAttachment = msg.text.toLowerCase().includes('.pdf') || msg.text.toLowerCase().includes('.doc') || msg.text.toLowerCase().includes('.xlsx');
                    
                    // Day segregation separators logic
                    let dateDivider = null;
                    if (msg.createdAt) {
                      const msgDate = new Date(msg.createdAt);
                      if (!isNaN(msgDate.getTime())) {
                        const dateStr = msgDate.toDateString();
                        if (dateStr !== lastDateStr) {
                          lastDateStr = dateStr;
                          
                          const today = new Date();
                          const yesterday = new Date();
                          yesterday.setDate(today.getDate() - 1);
                          
                          const day = String(msgDate.getDate()).padStart(2, '0');
                          const month = String(msgDate.getMonth() + 1).padStart(2, '0');
                          let displayDate = `${day}/${month}/${msgDate.getFullYear()}`;
                          if (dateStr === today.toDateString()) {
                            displayDate = 'Today';
                          } else if (dateStr === yesterday.toDateString()) {
                            displayDate = 'Yesterday';
                          }
                          
                          dateDivider = (
                            <div style={{ display: 'flex', justifyContent: 'center', margin: '16px 0', width: '100%' }}>
                              <span style={{ fontSize: '11px', background: '#171a1f', border: '1px solid #222730', padding: '4px 12px', borderRadius: '20px', color: '#94a3b8', fontWeight: 600, letterSpacing: '0.3px', boxShadow: '0 1px 3px rgba(0,0,0,0.2)' }}>
                                {displayDate}
                              </span>
                            </div>
                          );
                        }
                      }
                    }

                    return (
                      <React.Fragment key={msg.messageId}>
                        {dateDivider}
                        <div
                          ref={(el) => { messageRefs.current[msg.messageId] = el; }}
                          onTouchStart={() => handleLongPressStart(msg.messageId)}
                          onTouchEnd={handleLongPressEnd}
                          onTouchMove={handleLongPressEnd}
                          onMouseDown={() => handleLongPressStart(msg.messageId)}
                          onMouseUp={handleLongPressEnd}
                          onMouseLeave={handleLongPressEnd}
                          onClick={() => {
                            if (isMessageSelectMode) {
                              setSelectedMessageIds(prev => ({ ...prev, [msg.messageId]: !prev[msg.messageId] }));
                            }
                          }}
                          style={{
                            alignSelf: isMe ? 'flex-end' : 'flex-start',
                            maxWidth: isMobile ? '88%' : '75%',
                            display: 'flex',
                            gap: '8px',
                            marginTop: isSameSender ? '2px' : '8px',
                            opacity: msg.isOptimistic ? 0.7 : 1,
                            cursor: isMessageSelectMode ? 'pointer' : 'default',
                            background: isMessageSelectMode && selectedMessageIds[msg.messageId] ? 'rgba(239, 68, 68, 0.05)' : 'transparent',
                            borderRadius: '8px',
                            padding: isMessageSelectMode ? '4px 8px' : '0'
                          }}
                        >
                          {isMessageSelectMode && (
                            <input 
                              type="checkbox" 
                              checked={!!selectedMessageIds[msg.messageId]}
                              onChange={() => {}} // parent onClick handles toggle
                              style={{ alignSelf: 'center', width: '16px', height: '16px', cursor: 'pointer', accentColor: '#ef4444', marginRight: '4px' }}
                            />
                          )}
                      {/* Avatar for incoming messages */}
                      {!isMe && !isSameSender && (
                        <div style={{
                          width: '28px',
                          height: '28px',
                          borderRadius: '50%',
                          background: '#4f46e5',
                          color: '#ffffff',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontWeight: 'bold',
                          fontSize: '10px',
                          flexShrink: 0,
                          marginTop: '4px'
                        }}>
                          {msg.senderName ? msg.senderName[0].toUpperCase() : 'U'}
                        </div>
                      )}
                      
                      {/* Spacer to align bubbles when avatar is missing */}
                      {!isMe && isSameSender && <div style={{ width: '28px', flexShrink: 0 }} />}

                      <div style={{ display: 'flex', flexDirection: 'column', alignItems: isMe ? 'flex-end' : 'flex-start', minWidth: 0, width: '100%' }}>
                        
                        {/* Name header */}
                        {!isMe && !isSameSender && (
                          <span style={{ fontSize: '11px', color: '#818cf8', marginBottom: '3px', fontWeight: 600, paddingLeft: '4px' }}>
                            {msg.senderName} ({msg.senderRole.toUpperCase()})
                          </span>
                        )}

                        {/* Bubble */}
                        <div
                          onDoubleClick={() => {
                            if (!msg.isDeleted && !msg.isOptimistic) {
                              setReplyingTo(msg);
                            }
                          }}
                          style={{
                            background: isMe ? '#2d2f74' : 'var(--surface)',
                            color: isMe ? '#ffffff' : 'var(--text)',
                            padding: '10px 14px',
                            minWidth: 0,
                            width: '100%',
                            borderRadius: isMe 
                              ? (isSameSender ? '16px 16px 16px 16px' : '16px 16px 4px 16px')
                              : (isSameSender ? '16px 16px 16px 16px' : '16px 16px 16px 4px'),
                            border: isMe ? 'none' : '1px solid var(--border-light)',
                            fontSize: '17px',
                            lineHeight: '1.45',
                            position: 'relative',
                            wordBreak: 'break-word',
                            boxShadow: '0 2px 8px rgba(0,0,0,0.15)'
                          }}
                        >
                          {/* Quote message reference */}
                          {msg.replyToId && (
                            <div 
                              onClick={() => scrollToMessage(msg.replyToId!)}
                              style={{
                                background: 'rgba(0,0,0,0.25)',
                                borderLeft: '3px solid #60a5fa',
                                padding: '6px 10px',
                                borderRadius: '4px',
                                marginBottom: '8px',
                                fontSize: '11.5px',
                                cursor: 'pointer',
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '2px'
                              }}
                            >
                              <div style={{ fontWeight: 600, color: '#60a5fa' }}>{msg.replyToSenderName}</div>
                              <div style={{ color: '#94a3b8', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap' }}>
                                {msg.replyToText}
                              </div>
                            </div>
                          )}

                          {msg.isDeleted ? (
                            <span style={{ fontStyle: 'italic', color: '#596a82' }}>🚫 This message was deleted</span>
                          ) : editingMessageId === msg.messageId ? (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', minWidth: '220px' }}>
                              <textarea
                                value={editingText}
                                onChange={(e) => setEditingText(e.target.value)}
                                style={{
                                  width: '100%',
                                  background: '#171a1f',
                                  border: '1px solid #4f46e5',
                                  borderRadius: '6px',
                                  color: '#ffffff',
                                  padding: '6px',
                                  fontSize: '13px',
                                  resize: 'none',
                                  outline: 'none'
                                }}
                                onKeyDown={(e) => {
                                  if (e.key === 'Enter' && !e.shiftKey) {
                                    e.preventDefault();
                                    handleEditMessage(msg.messageId, editingText);
                                  }
                                }}
                              />
                              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '6px' }}>
                                <button
                                  onClick={() => setEditingMessageId('')}
                                  style={{ background: 'transparent', border: '1px solid #222730', color: '#94a3b8', borderRadius: '4px', padding: '3px 8px', fontSize: '10px', cursor: 'pointer' }}
                                >
                                  Cancel
                                </button>
                                <button
                                  onClick={() => handleEditMessage(msg.messageId, editingText)}
                                  style={{ background: '#4f46e5', border: 'none', color: '#ffffff', borderRadius: '4px', padding: '3px 8px', fontSize: '10px', cursor: 'pointer', fontWeight: 'bold' }}
                                >
                                  Save
                                </button>
                              </div>
                            </div>
                          ) : msg.type === 'poll' ? (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', minWidth: '240px' }}>
                              <div style={{ fontWeight: 600, fontSize: '14px', display: 'flex', alignItems: 'center', gap: '6px', color: '#60a5fa' }}>
                                📊 {msg.text}
                              </div>
                              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginTop: '6px' }}>
                                {(msg.pollOptions || []).map((opt, oIdx) => {
                                  const votesMap = msg.pollVotes || {};
                                  const totalVotes = Object.keys(votesMap).length;
                                  const hasVotedThis = votesMap[adminUid] === oIdx;
                                  const percentage = totalVotes > 0 ? Math.round((opt.votesCount / totalVotes) * 100) : 0;
                                  return (
                                    <div
                                      key={oIdx}
                                      onClick={() => handleVotePoll(msg.messageId, oIdx)}
                                      style={{
                                        position: 'relative',
                                        background: hasVotedThis ? 'rgba(96, 165, 250, 0.15)' : 'var(--bg-soft)',
                                        border: hasVotedThis ? '1px solid #60a5fa' : '1px solid var(--border-light)',
                                        borderRadius: '8px',
                                        padding: '8px 12px',
                                        cursor: 'pointer',
                                        overflow: 'hidden',
                                        display: 'flex',
                                        flexDirection: 'column',
                                        alignItems: 'flex-start',
                                        fontSize: '13px',
                                        transition: 'all 0.2s',
                                        userSelect: 'none',
                                        width: '100%'
                                      }}
                                    >
                                      <div
                                        style={{
                                          position: 'absolute',
                                          left: 0,
                                          top: 0,
                                          bottom: 0,
                                          width: `${percentage}%`,
                                          background: hasVotedThis ? 'rgba(96, 165, 250, 0.1)' : 'rgba(148, 163, 184, 0.05)',
                                          zIndex: 0,
                                          transition: 'width 0.3s'
                                        }}
                                      />
                                      {(() => {
                                        const voterKeys = Object.entries(msg.pollVotes || {})
                                          .filter(([_, oIdxVal]) => oIdxVal === oIdx)
                                          .map(([vKey]) => participantNames[vKey] || vKey);
                                        return (
                                          <>
                                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '100%', zIndex: 1 }}>
                                              <span style={{ fontWeight: 555 }}>{opt.text}</span>
                                              <span style={{ fontSize: '11px', color: 'var(--text-muted)' }}>
                                                {opt.votesCount} votes ({percentage}%)
                                              </span>
                                            </div>
                                            {voterKeys.length > 0 && (
                                              <div style={{ fontSize: '10px', color: 'var(--text-muted)', marginTop: '4px', zIndex: 1, textAlign: 'left', width: '100%', opacity: 0.85, whiteSpace: 'normal', wordBreak: 'break-word' }}>
                                                Voters: {voterKeys.join(', ')}
                                              </div>
                                            )}
                                          </>
                                        );
                                      })()}
                                    </div>
                                  );
                                })}
                              </div>
                            </div>
                          ) : (
                            <>
                              <div className="selectable-text" style={{ wordBreak: 'break-word', whiteSpace: 'pre-wrap', fontSize: '17px' }} dangerouslySetInnerHTML={{ __html: renderMarkdown(msg.text, participantNames) }} />
                              
                              {/* Attachment box */}
                              {hasAttachment && (
                                <div style={{
                                  marginTop: '10px',
                                  background: '#090e17',
                                  borderRadius: '8px',
                                  padding: '10px',
                                  display: 'flex',
                                  alignItems: 'center',
                                  justifyContent: 'space-between',
                                  gap: '12px',
                                  border: '1px solid #222730',
                                  minWidth: '240px'
                                }}>
                                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <div style={{ background: '#ef4444', width: '32px', height: '36px', borderRadius: '4px', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold', fontSize: '9px', color: '#ffffff' }}>
                                      <span>FILE</span>
                                    </div>
                                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                                      <span style={{ fontSize: '12px', fontWeight: 600, color: '#ffffff', maxWidth: '140px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{msg.text.split(' ').pop()}</span>
                                      <span style={{ fontSize: '10px', color: '#596a82', marginTop: '2px' }}>Attachment Link</span>
                                    </div>
                                  </div>
                                  <a href={msg.text.includes('(') ? msg.text.substring(msg.text.indexOf('(') + 1, msg.text.indexOf(')')) : msg.text} target="_blank" rel="noopener noreferrer" style={{ color: '#60a5fa', cursor: 'pointer', display: 'flex', alignItems: 'center' }} title="Download file">
                                    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
                                  </a>
                                </div>
                              )}
                            </>
                          )}

                          {/* Quick reactions summary inside the bubble */}
                          {!msg.isDeleted && msg.reactions && (
                            <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap', marginTop: '8px' }}>
                              {msg.reactions.thumbsup && msg.reactions.thumbsup.length > 0 && (
                                <span 
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    setShowReactorsModal({
                                      isOpen: true,
                                      thumbsup: msg.reactions?.thumbsup || [],
                                      pray: msg.reactions?.pray || []
                                    });
                                  }}
                                  style={{
                                    fontSize: '11px',
                                    background: msg.reactions.thumbsup.includes(adminUid) ? 'rgba(96,165,250,0.2)' : 'rgba(255,255,255,0.08)',
                                    border: msg.reactions.thumbsup.includes(adminUid) ? '1px solid #60a5fa' : '1px solid transparent',
                                    padding: '2px 6px',
                                    borderRadius: '10px',
                                    cursor: 'pointer',
                                    display: 'inline-flex',
                                    alignItems: 'center',
                                    gap: '3px',
                                    userSelect: 'none'
                                  }}
                                  title={`Reacted by: ${msg.reactions.thumbsup.map(uid => participantNames[uid] || uid).join(', ')}`}
                                >
                                  👍 <span style={{ color: 'var(--text-muted)', fontSize: '10px' }}>{msg.reactions.thumbsup.length}</span>
                                </span>
                              )}
                              {msg.reactions.pray && msg.reactions.pray.length > 0 && (
                                <span 
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    setShowReactorsModal({
                                      isOpen: true,
                                      thumbsup: msg.reactions?.thumbsup || [],
                                      pray: msg.reactions?.pray || []
                                    });
                                  }}
                                  style={{
                                    fontSize: '11px',
                                    background: msg.reactions.pray.includes(adminUid) ? 'rgba(96,165,250,0.2)' : 'rgba(255,255,255,0.08)',
                                    border: msg.reactions.pray.includes(adminUid) ? '1px solid #60a5fa' : '1px solid transparent',
                                    padding: '2px 6px',
                                    borderRadius: '10px',
                                    cursor: 'pointer',
                                    display: 'inline-flex',
                                    alignItems: 'center',
                                    gap: '3px',
                                    userSelect: 'none'
                                  }}
                                  title={`Reacted by: ${msg.reactions.pray.map(uid => participantNames[uid] || uid).join(', ')}`}
                                >
                                  🙏 <span style={{ color: 'var(--text-muted)', fontSize: '10px' }}>{msg.reactions.pray.length}</span>
                                </span>
                              )}
                            </div>
                          )}
                          
          {/* Bubble Footer Meta (time + ticks) */}
                          <div style={{ 
                            display: 'flex', 
                            justifyContent: 'flex-end', 
                            alignItems: 'center', 
                            gap: '4px', 
                            fontSize: '11px', 
                            color: '#596a82', 
                            marginTop: '8px',
                            textAlign: 'right',
                            flexWrap: 'wrap'
                          }}>
                            {starredMessageIds[msg.messageId] && (
                              <span style={{ color: '#eab308', marginRight: '4px', fontSize: '13px' }} title="Starred Message">★</span>
                            )}
                            {msg.isEdited && <span style={{ fontStyle: 'italic', fontSize: '10px', color: '#94a3b8', marginRight: '4px' }}>edited</span>}
                            <span>{new Date(msg.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>

                            {/* Quick reactions */}
                            {!msg.isDeleted && !msg.isOptimistic && (
                              <>
                                <span 
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    handleToggleReaction(msg.messageId, 'thumbsup');
                                  }}
                                  style={{ 
                                    cursor: 'pointer', 
                                    marginLeft: '10px', 
                                    opacity: msg.reactions?.thumbsup?.includes(adminUid) ? 1 : 0.4,
                                    fontSize: '15px',
                                    display: 'inline-flex', 
                                    alignItems: 'center',
                                    userSelect: 'none'
                                  }}
                                  title="React Thumbs Up"
                                >
                                  👍
                                </span>
                                <span 
                                  onClick={(e) => {
                                    e.stopPropagation();
                                    handleToggleReaction(msg.messageId, 'pray');
                                  }}
                                  style={{ 
                                    cursor: 'pointer', 
                                    marginLeft: '8px', 
                                    opacity: msg.reactions?.pray?.includes(adminUid) ? 1 : 0.4,
                                    fontSize: '15px',
                                    display: 'inline-flex', 
                                    alignItems: 'center',
                                    userSelect: 'none'
                                  }}
                                  title="React Folding Hand"
                                >
                                  🙏
                                </span>
                              </>
                            )}
                            
                            {/* Star Action */}
                            {!msg.isDeleted && !msg.isOptimistic && (
                              <span 
                                onClick={(e) => {
                                  e.stopPropagation();
                                  toggleStarMessage(msg.messageId);
                                }}
                                style={{ color: starredMessageIds[msg.messageId] ? '#eab308' : '#596a82', cursor: 'pointer', marginLeft: '10px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                                title={starredMessageIds[msg.messageId] ? "Unstar Message" : "Star Message"}
                              >
                                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>
                              </span>
                            )}

                            {/* Reply Action */}
                            {!msg.isDeleted && !msg.isOptimistic && (
                              <span 
                                onClick={(e) => {
                                  e.stopPropagation();
                                  setReplyingTo(msg);
                                }}
                                style={{ color: '#596a82', cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                                title="Reply to message"
                              >
                                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M10 9V5l-7 7 7 7v-4.1c5 0 8.5 1.6 11 5.1-1-5-4-10-11-11z"/></svg>
                              </span>
                            )}

                            {/* Pin Action (Admin only) */}
                            {!msg.isDeleted && !msg.isOptimistic && (
                              <span 
                                onClick={(e) => {
                                  e.stopPropagation();
                                  const isPinned = activeRoom?.pinnedMessage?.messageId === msg.messageId;
                                  if (isPinned) handleUnpinMessage();
                                  else handlePinMessage(msg.messageId);
                                }}
                                style={{ color: activeRoom?.pinnedMessage?.messageId === msg.messageId ? '#60a5fa' : '#596a82', cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', fontSize: '15px' }}
                                title={activeRoom?.pinnedMessage?.messageId === msg.messageId ? "Unpin Message" : "Pin Message"}
                              >
                                📌
                              </span>
                            )}

                            {/* Edit Action for Admin (no time limit, text type only) */}
                            {!msg.isDeleted && !msg.isOptimistic && msg.type !== 'poll' && (
                              <span 
                                onClick={(e) => {
                                  e.stopPropagation();
                                  setEditingMessageId(msg.messageId);
                                  setEditingText(msg.text);
                                }}
                                style={{ color: '#60a5fa', cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                                title="Edit message"
                              >
                                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
                              </span>
                            )}

                            {/* Delete Action for Admin (no limit) */}
                            {!msg.isDeleted && !msg.isOptimistic && (
                              <span 
                                onClick={(e) => {
                                  e.stopPropagation();
                                  handleDeleteMessage(msg.messageId);
                                }}
                                style={{ color: '#ef4444', cursor: 'pointer', marginLeft: '8px', display: 'inline-flex', alignItems: 'center', padding: '2px' }}
                                title="Delete message"
                              >
                                <svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/></svg>
                              </span>
                            )}

                            {isMe && !msg.isDeleted && (
                              <span 
                                onClick={() => setReceiptsModalMessage(msg)}
                                style={{ display: 'inline-flex', cursor: 'pointer', marginLeft: '4px' }}
                                title="View Read Receipts"
                              >
                                {readersCount > 0 ? (
                                  <svg viewBox="0 0 16 15" width="16" height="15" fill="#38bdf8"><path d="M15.01 3.3l-5.5 5.5-2.76-2.77-.88.88 3.64 3.64 6.38-6.37-.88-.88zm-5.56 5.5l-.89-.89-.88.88 1.77 1.77 1-.99-.88-.88-.12.12zm-3.8-1.92l-.88-.88-2.77 2.76-1.39-1.39-.88.88 2.27 2.27 3.65-3.64z"/></svg>
                                ) : (
                                  <svg viewBox="0 0 16 15" width="16" height="15" fill="#596a82"><path d="M15.01 3.3l-5.5 5.5-2.76-2.77-.88.88 3.64 3.64 6.38-6.37-.88-.88zm-5.56 5.5l-.89-.89-.88.88 1.77 1.77 1-.99-.88-.88-.12.12zm-3.8-1.92l-.88-.88-2.77 2.76-1.39-1.39-.88.88 2.27 2.27 3.65-3.64z"/></svg>
                                )}
                              </span>
                            )}
                          </div>
                        </div>
                      </div>
                    </div>
                  </React.Fragment>
                );
              });
            })()}
            <div ref={messagesEndRef} />
              </div>

              {/* Message Typing Panel */}
              {isMessageSelectMode ? (
                <div style={{ padding: '14px 20px', background: 'rgba(239, 68, 68, 0.08)', borderTop: '1px solid rgba(239, 68, 68, 0.2)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '16px', zIndex: 5 }}>
                  <span style={{ fontSize: '13px', fontWeight: 'bold', color: '#f87171' }}>
                    🗑️ {Object.values(selectedMessageIds).filter(Boolean).length} messages selected for deletion
                  </span>
                  <div style={{ display: 'flex', gap: '8px' }}>
                    <button
                      type="button"
                      onClick={() => {
                        setIsMessageSelectMode(false);
                        setSelectedMessageIds({});
                      }}
                      style={{ background: 'transparent', border: '1px solid var(--border)', color: 'var(--text-muted)', borderRadius: '8px', padding: '8px 16px', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer' }}
                    >
                      Cancel
                    </button>
                    <button
                      type="button"
                      onClick={handleBulkDeleteMessages}
                      disabled={Object.values(selectedMessageIds).filter(Boolean).length === 0}
                      style={{ background: '#ef4444', border: 'none', color: '#ffffff', borderRadius: '8px', padding: '8px 16px', fontSize: '12px', fontWeight: 'bold', cursor: 'pointer', opacity: Object.values(selectedMessageIds).filter(Boolean).length === 0 ? 0.5 : 1 }}
                    >
                      Delete Selected
                    </button>
                  </div>
                </div>
              ) : (
                <form onSubmit={handleSendMessage} style={{ position: 'relative', padding: '14px 20px', background: 'var(--surface-popover)', display: 'flex', flexDirection: 'column', gap: '8px', zIndex: 5, borderTop: '1px solid var(--border)' }}>
                
                {/* Mention / Tag Suggestions dropdown */}
                {showMentionSuggestions && mentionCandidates.length > 0 && (
                  <div style={{
                    position: 'absolute',
                    bottom: '105%',
                    left: '20px',
                    width: '280px',
                    background: 'var(--surface-popover)',
                    border: '1px solid var(--border)',
                    borderRadius: '8px',
                    boxShadow: '0 -4px 12px rgba(0,0,0,0.3)',
                    maxHeight: '160px',
                    overflowY: 'auto',
                    zIndex: 1000,
                    padding: '6px 0',
                    marginBottom: '8px'
                  }}>
                    {mentionCandidates.map((cand: any) => (
                      <div
                        key={cand.id}
                        onClick={() => selectMention(cand.name)}
                        style={{
                          padding: '8px 12px',
                          cursor: 'pointer',
                          fontSize: '13px',
                          color: '#ffffff',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center'
                        }}
                        onMouseEnter={(e) => e.currentTarget.style.background = '#222730'}
                        onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                      >
                        <span style={{ fontWeight: 600 }}>{cand.name}</span>
                        <span style={{ fontSize: '10px', color: '#64748b' }}>{cand.id}</span>
                      </div>
                    ))}
                  </div>
                )}
                
                {/* Replying Draft Preview */}
                {replyingTo && (
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    background: '#1c2026',
                    borderLeft: '4px solid #60a5fa',
                    padding: '8px 14px',
                    borderRadius: '8px',
                    marginBottom: '4px'
                  }}>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '2px', fontSize: '12px', overflow: 'hidden' }}>
                      <span style={{ color: '#60a5fa', fontWeight: 600 }}>Replying to {replyingTo.senderName}</span>
                      <span style={{ color: '#94a3b8', textOverflow: 'ellipsis', overflow: 'hidden', whiteSpace: 'nowrap', maxWidth: '300px' }}>
                        {replyingTo.text}
                      </span>
                    </div>
                    <button 
                      type="button" 
                      onClick={() => setReplyingTo(null)}
                      style={{ background: 'transparent', border: 'none', color: '#ef4444', fontSize: '14px', cursor: 'pointer', padding: '4px' }}
                    >
                      ✕
                    </button>
                  </div>
                )}

                <div style={{ display: 'flex', gap: '10px', alignItems: 'center', width: '100%' }}>
                  {/* Attachment clip and smiley inside a single gorgeous dark pill input wrapper */}
                  <div style={{
                    flex: 1,
                    minWidth: '0',
                    background: '#1c2026',
                    border: '1px solid #222730',
                    borderRadius: '24px',
                    padding: '6px 14px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '10px',
                    minHeight: '42px',
                    height: 'auto'
                  }}>
                    <div 
                      onClick={() => setShowAttachmentMenu(prev => !prev)}
                      style={{ color: '#94a3b8', cursor: 'pointer', display: 'flex', alignItems: 'center', position: 'relative' }} 
                      title="Attach file or insert link"
                    >
                      <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M16.5 6v11.5c0 2.21-1.79 4-4 4s-4-1.79-4-4V5c0-3.31 2.69-6 6-6s6 2.69 6 6v10.5c0 4.42-3.58 8-8 8s-8-3.58-8-8V6h2v9.5c0 3.31 2.69 6 6 6s6-2.69 6-6V5c0-2.21-1.79-4-4-4s-4 1.79-4 4v12.5c0 1.1.9 2 2 2s2-.9 2-2V6h2z"/></svg>
                      
                      {showAttachmentMenu && (
                        <div style={{
                          position: 'absolute',
                          bottom: '40px',
                          left: '0',
                          background: '#1c2026',
                          border: '1px solid #222730',
                          borderRadius: '8px',
                          padding: '6px 0',
                          display: 'flex',
                          flexDirection: 'column',
                          width: '140px',
                          boxShadow: '0 4px 12px rgba(0,0,0,0.4)',
                          zIndex: 100
                        }}>
                          <button
                            type="button"
                            onClick={(e) => {
                              e.stopPropagation();
                              setShowAttachmentMenu(false);
                              fileInputRef.current?.click();
                            }}
                            style={{
                              background: 'transparent',
                              border: 'none',
                              color: '#ffffff',
                              padding: '6px 12px',
                              textAlign: 'left',
                              fontSize: '12px',
                              cursor: 'pointer',
                              display: 'flex',
                              alignItems: 'center',
                              gap: '6px',
                              width: '100%'
                            }}
                            onMouseEnter={(e) => e.currentTarget.style.background = '#222730'}
                            onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                          >
                            📂 Upload File
                          </button>
                          <button
                            type="button"
                            onClick={(e) => {
                              e.stopPropagation();
                              setShowAttachmentMenu(false);
                              setShowLinkModal(true);
                            }}
                            style={{
                              background: 'transparent',
                              border: 'none',
                              color: '#ffffff',
                              padding: '6px 12px',
                              textAlign: 'left',
                              fontSize: '12px',
                              cursor: 'pointer',
                              display: 'flex',
                              alignItems: 'center',
                              gap: '6px',
                              width: '100%'
                            }}
                            onMouseEnter={(e) => e.currentTarget.style.background = '#222730'}
                            onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                          >
                            🔗 Insert Link
                          </button>
                          <button
                            type="button"
                            onClick={(e) => {
                              e.stopPropagation();
                              setShowAttachmentMenu(false);
                              setShowPollModal(true);
                            }}
                            style={{
                              background: 'transparent',
                              border: 'none',
                              color: '#ffffff',
                              padding: '6px 12px',
                              textAlign: 'left',
                              fontSize: '12px',
                              cursor: 'pointer',
                              display: 'flex',
                              alignItems: 'center',
                              gap: '6px',
                              width: '100%'
                            }}
                            onMouseEnter={(e) => e.currentTarget.style.background = '#222730'}
                            onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                          >
                            📊 Create Poll
                          </button>
                        </div>
                      )}
                    </div>
                  <input 
                    type="file" 
                    ref={fileInputRef} 
                    onChange={handleFileUpload} 
                    style={{ display: 'none' }} 
                  />
                  <textarea
                    value={inputText}
                    onChange={(e) => handleInputChange(e.target.value)}
                    placeholder="Type a message..."
                    style={{
                      flex: 1,
                      width: '100%',
                      minWidth: '0',
                      border: 'none',
                      background: 'transparent',
                      color: 'var(--text)',
                      fontSize: '16px',
                      resize: 'none',
                      height: 'auto',
                      minHeight: '24px',
                      maxHeight: '120px',
                      outline: 'none',
                      lineHeight: '1.4',
                      padding: '2px 0',
                      overflowY: 'auto'
                    }}
                    onBlur={() => {
                      setTimeout(() => {
                        window.scrollTo(0, 0);
                      }, 100);
                    }}
                  />
                  <div style={{ color: '#94a3b8', cursor: 'pointer', display: 'flex', alignItems: 'center' }} title="Emojis">
                    <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14H11v-2h2v2zm0-4H11V7h2v5z"/></svg>
                  </div>
                </div>

                <button 
                  type="submit" 
                  style={{ 
                    height: '42px', 
                    borderRadius: '50%', 
                    width: '42px', 
                    minWidth: '42px', 
                    padding: '0', 
                    display: 'flex', 
                    alignItems: 'center', 
                    justifyContent: 'center', 
                    background: '#4f46e5', 
                    border: 'none', 
                    color: '#ffffff', 
                    cursor: 'pointer',
                    boxShadow: '0 2px 8px rgba(79, 70, 229, 0.45)',
                    transition: 'transform 0.1s'
                  }}
                  onMouseDown={(e) => e.currentTarget.style.transform = 'scale(0.95)'}
                  onMouseUp={(e) => e.currentTarget.style.transform = 'scale(1)'}
                  title="Send message"
                >
                  <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" style={{ transform: 'rotate(45deg)' }}><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
                </button>
                </div>
              </form>
              )}
            </>
          ) : (
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', color: '#596a82', gap: '16px', padding: '24px', textAlign: 'center' }}>
              <div style={{
                background: 'rgba(79, 70, 229, 0.1)',
                width: '120px',
                height: '120px',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#4f46e5',
                fontSize: '4rem'
              }}>
                💬
              </div>
              <div>
                <h2 style={{ fontSize: '1.25rem', fontWeight: 600, color: '#ffffff', margin: '0 0 8px 0' }}>Yashcom Admin Chat Console</h2>
                <p style={{ fontSize: '13.5px', color: '#596a82', margin: 0, maxWidth: '350px', lineHeight: '1.5' }}>
                  Select an active class group or private student direct message conversation to manage and write replies.
                </p>
              </div>
            </div>
          )}
        </div>

      </div>

      {/* DM Modal Drawer */}
      {showDmModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.75)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div style={{ background: '#171a1f', border: '1px solid #222730', borderRadius: '12px', maxWidth: '480px', width: '100%', maxHeight: '80vh', display: 'flex', flexDirection: 'column', boxShadow: '0 4px 24px rgba(0,0,0,0.5)', color: '#ffffff' }}>
            
            <div style={{ padding: '16px 20px', borderBottom: '1px solid #222730', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: '#ffffff' }}>💬 Start Private Direct Message</h3>
              <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: '#94a3b8', lineHeight: 1 }} onClick={() => setShowDmModal(false)}>×</button>
            </div>

            <div style={{ padding: '12px 20px', borderBottom: '1px solid #222730' }}>
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search student code or name..."
                style={{ width: '100%', padding: '9px 12px', borderRadius: '8px', border: '1px solid #222730', background: '#1c2026', color: '#ffffff', fontSize: '16px', outline: 'none' }}
              />
            </div>

            <div style={{ flex: 1, overflowY: 'auto', padding: '10px' }}>
              {filteredStudents.length === 0 ? (
                <div style={{ color: '#596a82', fontSize: '13px', padding: '20px', textAlign: 'center' }}>No matches found.</div>
              ) : (
                filteredStudents.map(student => (
                  <div
                    key={student.studentCode}
                    onClick={() => handleStartDM(student.studentCode, student.name)}
                    style={{
                      padding: '10px 14px',
                      borderRadius: '8px',
                      cursor: 'pointer',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center',
                      transition: 'background 0.2s',
                      marginBottom: '4px'
                    }}
                    onMouseEnter={(e) => e.currentTarget.style.background = '#1c2026'}
                    onMouseLeave={(e) => e.currentTarget.style.background = 'transparent'}
                  >
                    <div>
                      <div style={{ fontSize: '13.5px', fontWeight: 600, color: '#ffffff' }}>{student.name}</div>
                      <div style={{ fontSize: '11px', color: '#596a82', marginTop: '2px' }}>Student</div>
                    </div>
                    <span style={{ fontSize: '12px', color: '#60a5fa', fontWeight: 600 }}>Chat →</span>
                  </div>
                ))
              )}
            </div>

          </div>
        </div>
      )}

      {/* Group Modal Drawer */}
      {showGroupModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.75)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div style={{ background: '#171a1f', border: '1px solid #222730', borderRadius: '12px', maxWidth: '480px', width: '100%', boxShadow: '0 4px 24px rgba(0,0,0,0.5)', color: '#ffffff' }}>
            
            <div style={{ padding: '16px 20px', borderBottom: '1px solid #222730', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: '#ffffff' }}>👥 Setup Batch Group Chat</h3>
              <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: '#94a3b8', lineHeight: 1 }} onClick={() => setShowGroupModal(false)}>×</button>
            </div>

            <form onSubmit={handleCreateGroup} style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '12px', fontWeight: 600, color: '#94a3b8' }}>Select Batch</label>
                <select
                  value={selectedBatchId}
                  onChange={(e) => {
                    setSelectedBatchId(e.target.value);
                    const bName = batchesList.find(b => b.id === e.target.value)?.name || '';
                    setGroupName(`${bName} Chat Group`);
                  }}
                  style={{ padding: '8px 10px', borderRadius: '6px', border: '1px solid #222730', background: '#1c2026', color: '#ffffff', fontSize: '16px', outline: 'none' }}
                >
                  {batchesList.map(b => (
                    <option key={b.id} value={b.id}>{b.name}</option>
                  ))}
                </select>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '12px', fontWeight: 600, color: '#94a3b8' }}>Group Name</label>
                <input
                  type="text"
                  required
                  value={groupName}
                  onChange={(e) => setGroupName(e.target.value)}
                  style={{ padding: '8px 10px', borderRadius: '6px', border: '1px solid #222730', background: '#1c2026', color: '#ffffff', fontSize: '16px', outline: 'none' }}
                />
              </div>

              <button 
                type="submit" 
                style={{ 
                  marginTop: '8px', 
                  padding: '10px', 
                  background: '#4f46e5', 
                  border: 'none', 
                  color: '#ffffff', 
                  fontSize: '13px', 
                  fontWeight: 600, 
                  borderRadius: '6px', 
                  cursor: 'pointer',
                  boxShadow: '0 2px 8px rgba(79, 70, 229, 0.45)',
                  transition: 'transform 0.1s'
                }}
                onMouseDown={(e) => e.currentTarget.style.transform = 'scale(0.98)'}
                onMouseUp={(e) => e.currentTarget.style.transform = 'scale(1)'}
              >
                Create Group Chat
              </button>

            </form>
          </div>
        </div>
      )}

      {/* Hyperlink Input Modal */}
      {showLinkModal && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(9, 14, 23, 0.85)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 10000,
          backdropFilter: 'blur(4px)',
          padding: '16px'
        }}>
          <div style={{
            background: '#1c2026',
            border: '1px solid #222730',
            borderRadius: '12px',
            padding: '20px',
            width: '320px',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px'
          }}>
            <h4 style={{ margin: '0 0 4px 0', fontSize: '14px', fontWeight: 'bold' }}>🔗 Insert Hyperlink</h4>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
              <span style={{ fontSize: '11px', color: '#94a3b8' }}>Link Address:</span>
              <input 
                type="text"
                value={linkUrl}
                onChange={(e) => setLinkUrl(e.target.value)}
                placeholder="https://example.com"
                style={{ padding: '8px', fontSize: '16px', borderRadius: '6px', border: '1px solid #222730', background: '#171a1f', color: '#ffffff', outline: 'none' }}
              />
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
              <span style={{ fontSize: '11px', color: '#94a3b8' }}>Display Text:</span>
              <input 
                type="text"
                value={linkLabel}
                onChange={(e) => setLinkLabel(e.target.value)}
                placeholder="Maharashtra Board Syllabus"
                style={{ padding: '8px', fontSize: '16px', borderRadius: '6px', border: '1px solid #222730', background: '#171a1f', color: '#ffffff', outline: 'none' }}
              />
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '8px' }}>
              <button
                type="button"
                onClick={() => {
                  setShowLinkModal(false);
                  setLinkUrl('');
                  setLinkLabel('');
                }}
                style={{ padding: '6px 12px', fontSize: '12px', border: '1px solid #222730', background: 'transparent', color: '#94a3b8', borderRadius: '6px', cursor: 'pointer' }}
              >
                Cancel
              </button>
              <button
                type="button"
                onClick={() => {
                  if (!linkUrl) return;
                  const display = linkLabel.trim() || linkUrl;
                  setInputText(prev => prev + ` [${display}](${linkUrl}) `);
                  setShowLinkModal(false);
                  setLinkUrl('');
                  setLinkLabel('');
                }}
                style={{ padding: '6px 14px', fontSize: '12px', border: 'none', background: '#4f46e5', color: '#ffffff', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}
              >
                Insert Link
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Read Receipts Modal */}
      {receiptsModalMessage && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(9, 14, 23, 0.85)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 10000,
          backdropFilter: 'blur(4px)',
          padding: '16px'
        }}>
          <div style={{
            background: '#1c2026',
            border: '1px solid #222730',
            borderRadius: '12px',
            padding: '20px',
            width: '340px',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px',
            maxHeight: '80%',
            overflowY: 'auto'
          }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h4 style={{ margin: 0, fontSize: '14px', fontWeight: 'bold' }}>✔️ Message Info (Read Receipts)</h4>
              <button 
                onClick={() => setReceiptsModalMessage(null)}
                style={{ background: 'transparent', border: 'none', color: '#94a3b8', fontSize: '16px', cursor: 'pointer' }}
              >
                ×
              </button>
            </div>
            
            <div style={{ padding: '10px', background: '#171a1f', borderRadius: '8px', fontSize: '12.5px', border: '1px solid #222730' }}>
              <div style={{ color: '#94a3b8', fontSize: '10px', textTransform: 'uppercase', marginBottom: '4px', fontWeight: 'bold' }}>Message Text</div>
              <div style={{ wordBreak: 'break-word', color: '#ffffff' }}>{receiptsModalMessage.text}</div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', marginTop: '4px' }}>
              <span style={{ fontSize: '11px', color: '#94a3b8', fontWeight: 'bold', textTransform: 'uppercase' }}>Read By</span>
              
              {(() => {
                const readBy = receiptsModalMessage.readBy || {};
                const details: Array<{ name: string; role: string; time: string }> = [];
                
                const parseReadReceiptTime = (timeVal: any): string => {
                  if (!timeVal) return '—';
                  let dateObj: Date | null = null;
                  
                  if (typeof timeVal === 'string') {
                    dateObj = new Date(timeVal);
                  } else if (typeof timeVal === 'object') {
                    if (typeof timeVal.seconds === 'number') {
                      dateObj = new Date(timeVal.seconds * 1000);
                    } else {
                      let currentVal = timeVal;
                      while (currentVal && typeof currentVal === 'object' && !Array.isArray(currentVal)) {
                        if (typeof currentVal.seconds === 'number') {
                          dateObj = new Date(currentVal.seconds * 1000);
                          break;
                        }
                        const keys = Object.keys(currentVal);
                        if (keys.length === 0) break;
                        currentVal = currentVal[keys[0]];
                      }
                      if (typeof currentVal === 'string') {
                        dateObj = new Date(currentVal);
                      }
                    }
                  }
                  
                  if (!dateObj || isNaN(dateObj.getTime())) {
                    return '—';
                  }
                  
                  const day = String(dateObj.getDate()).padStart(2, '0');
                  const month = String(dateObj.getMonth() + 1).padStart(2, '0');
                  const datePart = `${day}/${month}/${dateObj.getFullYear()}`;
                  return dateObj.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + ' ' + datePart;
                };

                Object.entries(readBy).forEach(([uid, timeStr]) => {
                  if (uid === receiptsModalMessage.senderId) return;
                  let name = participantNames[uid] || uid;
                  let role = 'student';
                  
                  if (uid.toLowerCase() === 'admin' || uid === firebaseUser?.uid) {
                    name = participantNames['admin'] || 'Admin';
                    role = 'admin';
                  } else if (uid.startsWith('PR-')) {
                    role = 'parent';
                    const emailOrId = uid.substring(3).toLowerCase().trim();
                    let student = studentsList.find((s: any) => s.parentEmail?.toLowerCase().trim() === emailOrId);
                    if (!student) {
                      student = studentsList.find((s: any) => s.studentCode === emailOrId);
                    }
                    if (student) {
                      name = `${student.name} (Parent)`;
                    } else if (name === uid || name.includes('@')) {
                      name = 'Parent (P)';
                    }
                  } else {
                    const student = studentsList.find((s: any) => s.studentCode === uid);
                    if (student) {
                      name = student.name;
                    } else if (name === uid || name.includes('@') || /^ST-\d{4}-\d+$/i.test(name)) {
                      name = 'Student';
                    }
                  }

                  details.push({
                    name,
                    role,
                    time: parseReadReceiptTime(timeStr)
                  });
                });

                if (details.length === 0) {
                  return <div style={{ fontSize: '12px', color: '#596a82', fontStyle: 'italic', textAlign: 'center', padding: '10px 0' }}>No one has read this message yet.</div>;
                }

                return details.map((reader, index) => (
                  <div key={index} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '6px 0', borderBottom: '1px solid #222730' }}>
                    <div style={{ display: 'flex', flexDirection: 'column' }}>
                      <span style={{ fontSize: '12.5px', fontWeight: 600, color: '#ffffff' }}>{reader.name}</span>
                      <span style={{ fontSize: '10px', color: '#94a3b8' }}>{reader.role.toUpperCase()}</span>
                    </div>
                    <span style={{ fontSize: '11px', color: '#596a82' }}>{reader.time}</span>
                  </div>
                ));
              })()}
            </div>
          </div>
        </div>
      )}

      {showPollModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.75)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div style={{ background: '#171a1f', border: '1px solid #222730', borderRadius: '12px', maxWidth: '400px', width: '100%', boxShadow: '0 4px 24px rgba(0,0,0,0.5)', color: '#ffffff', display: 'flex', flexDirection: 'column' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid #222730', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: '#ffffff' }}>📊 Create Interactive Poll</h3>
              <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: '#94a3b8', lineHeight: 1 }} onClick={() => setShowPollModal(false)}>×</button>
            </div>
            <form onSubmit={handleCreatePoll} style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                <label style={{ fontSize: '12px', fontWeight: 600, color: '#94a3b8' }}>Poll Question / Title</label>
                <input
                  type="text"
                  required
                  value={pollQuestion}
                  onChange={(e) => setPollQuestion(e.target.value)}
                  placeholder="e.g. Schedule extra revision class?"
                  style={{ padding: '8px 10px', borderRadius: '6px', border: '1px solid #222730', background: '#1c2026', color: '#ffffff', fontSize: '16px', outline: 'none' }}
                />
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                <label style={{ fontSize: '12px', fontWeight: 600, color: '#94a3b8' }}>Options (at least 2)</label>
                {pollOptionsInput.map((opt, idx) => (
                  <div key={idx} style={{ display: 'flex', gap: '6px' }}>
                    <input
                      type="text"
                      required={idx < 2}
                      value={opt}
                      onChange={(e) => {
                        const updated = [...pollOptionsInput];
                        updated[idx] = e.target.value;
                        setPollOptionsInput(updated);
                      }}
                      placeholder={`Option ${idx + 1}`}
                      style={{ flex: 1, padding: '8px 10px', borderRadius: '6px', border: '1px solid #222730', background: '#1c2026', color: '#ffffff', fontSize: '16px', outline: 'none' }}
                    />
                    {pollOptionsInput.length > 2 && (
                      <button
                        type="button"
                        onClick={() => {
                          setPollOptionsInput(prev => prev.filter((_, i) => i !== idx));
                        }}
                        style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.4)', color: '#f87171', borderRadius: '6px', padding: '0 8px', cursor: 'pointer' }}
                      >
                        ✕
                      </button>
                    )}
                  </div>
                ))}
                {pollOptionsInput.length < 5 && (
                  <button
                    type="button"
                    onClick={() => setPollOptionsInput(prev => [...prev, ''])}
                    style={{ alignSelf: 'flex-start', background: 'transparent', border: 'none', color: '#60a5fa', fontSize: '11px', fontWeight: 600, cursor: 'pointer', padding: '4px 0' }}
                  >
                    + Add Option
                  </button>
                )}
              </div>
              <button 
                type="submit" 
                style={{ 
                  marginTop: '8px', 
                  padding: '10px', 
                  background: '#4f46e5', 
                  border: 'none', 
                  color: '#ffffff', 
                  fontSize: '13px', 
                  fontWeight: 600, 
                  borderRadius: '6px', 
                  cursor: 'pointer',
                  boxShadow: '0 2px 8px rgba(79, 70, 229, 0.45)'
                }}
              >
                Send Poll to Chat
              </button>
            </form>
          </div>
        </div>
      )}

      {showStarredModal && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0, 0, 0, 0.75)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 9999, padding: '16px' }}>
          <div style={{ background: '#171a1f', border: '1px solid #222730', borderRadius: '12px', maxWidth: '480px', width: '100%', maxHeight: '85vh', display: 'flex', flexDirection: 'column', boxShadow: '0 4px 24px rgba(0,0,0,0.5)', color: '#ffffff' }}>
            <div style={{ padding: '16px 20px', borderBottom: '1px solid #222730', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700, color: '#facc15' }}>★ Starred Messages</h3>
              <button style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: '#94a3b8', lineHeight: 1 }} onClick={() => setShowStarredModal(false)}>×</button>
            </div>
            <div style={{ flex: 1, overflowY: 'auto', padding: '16px', display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {(() => {
                const starred = messages.filter(m => starredMessageIds[m.messageId]);
                if (starred.length === 0) {
                  return <div style={{ color: '#596a82', fontStyle: 'italic', fontSize: '13px', padding: '24px', textAlign: 'center' }}>No messages starred in this room.</div>;
                }
                return starred.map(msg => (
                  <div key={msg.messageId} style={{ background: '#1c2026', border: '1px solid #222730', borderRadius: '8px', padding: '12px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
                      <span style={{ fontSize: '12px', fontWeight: 600, color: '#60a5fa' }}>{msg.senderName}</span>
                      <span style={{ fontSize: '10px', color: '#596a82' }}>{(() => {
                        const d = new Date(msg.createdAt);
                        if (isNaN(d.getTime())) return '';
                        const day = String(d.getDate()).padStart(2, '0');
                        const month = String(d.getMonth() + 1).padStart(2, '0');
                        return `${day}/${month}/${d.getFullYear()}`;
                      })()}</span>
                    </div>
                    <div style={{ fontSize: '13px', color: '#ffffff', wordBreak: 'break-word' }}>
                      {msg.text}
                    </div>
                    <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end', marginTop: '6px' }}>
                      <button
                        onClick={() => toggleStarMessage(msg.messageId)}
                        style={{ background: 'transparent', border: 'none', color: '#ef4444', fontSize: '11px', cursor: 'pointer' }}
                      >
                        Unstar
                      </button>
                      <button
                        onClick={() => {
                          setShowStarredModal(false);
                          scrollToMessage(msg.messageId);
                        }}
                        style={{ background: 'rgba(96, 165, 250, 0.15)', border: '1px solid rgba(96, 165, 250, 0.4)', borderRadius: '4px', color: '#60a5fa', fontSize: '11px', padding: '3px 8px', cursor: 'pointer' }}
                      >
                        Go to Message →
                      </button>
                    </div>
                  </div>
                ));
              })()}
            </div>
          </div>
        </div>
      )}

      {showReactorsModal && showReactorsModal.isOpen && (
        <div 
          style={{ 
            position: 'fixed', 
            inset: 0, 
            background: 'rgba(0, 0, 0, 0.75)', 
            backdropFilter: 'blur(4px)', 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            zIndex: 99999, 
            padding: '16px' 
          }}
          onClick={() => setShowReactorsModal(null)}
        >
          <div 
            style={{ 
              background: '#171a1f', 
              border: '1px solid #222730', 
              borderRadius: '12px', 
              maxWidth: '360px', 
              width: '100%', 
              boxShadow: '0 4px 24px rgba(0,0,0,0.5)', 
              color: '#ffffff', 
              display: 'flex', 
              flexDirection: 'column' 
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{ padding: '16px 20px', borderBottom: '1px solid #222730', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <h3 style={{ margin: 0, fontSize: '15px', fontWeight: 700 }}>Message Reactions</h3>
              <button 
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', fontSize: '1.5rem', color: '#94a3b8', lineHeight: 1 }} 
                onClick={() => setShowReactorsModal(null)}
              >
                ×
              </button>
            </div>
            <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px', maxHeight: '300px', overflowY: 'auto' }}>
              {showReactorsModal.thumbsup.length > 0 && (
                <div>
                  <h4 style={{ fontSize: '13px', fontWeight: 650, color: '#60a5fa', margin: '0 0 8px 0', display: 'flex', alignItems: 'center', gap: '6px' }}>
                    👍 Thumbs Up ({showReactorsModal.thumbsup.length})
                  </h4>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', paddingLeft: '8px' }}>
                    {showReactorsModal.thumbsup.map(uid => (
                      <div key={uid} style={{ fontSize: '13.5px', color: '#f1f5f9' }}>
                        • {participantNames[uid] || uid}
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {showReactorsModal.pray.length > 0 && (
                <div>
                  <h4 style={{ fontSize: '13px', fontWeight: 650, color: '#f59e0b', margin: '0 0 8px 0', display: 'flex', alignItems: 'center', gap: '6px' }}>
                    🙏 Folded Hands ({showReactorsModal.pray.length})
                  </h4>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '4px', paddingLeft: '8px' }}>
                    {showReactorsModal.pray.map(uid => (
                      <div key={uid} style={{ fontSize: '13.5px', color: '#f1f5f9' }}>
                        • {participantNames[uid] || uid}
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {showReactorsModal.thumbsup.length === 0 && showReactorsModal.pray.length === 0 && (
                <div style={{ color: '#94a3b8', fontSize: '13px', textAlign: 'center' }}>No reactions yet.</div>
              )}
            </div>
          </div>
        </div>
      )}

    </div>
  );
}
