/**
 * Canonical Chat Type Definitions (SSOT).
 */

export interface ChatRoom {
  roomId: string;
  type: 'group' | 'dm';
  name: string;
  participants: string[];
  unreadCounts: Record<string, number>;
  isMutedForStudents?: boolean;
  isMutedForParents?: boolean;
  lastMessage?: { text: string; senderName: string; timestamp: string };
  pinnedMessage?: { messageId: string; text: string; senderName: string; timestamp: string } | null;
  [key: string]: any;
}

export interface Message {
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
    [key: string]: any;
  };
  [key: string]: any;
}
