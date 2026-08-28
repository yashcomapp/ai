'use client';

import dynamic from 'next/dynamic';

const ChatView = dynamic(() => import('@/components/chat/ChatView'), { ssr: false });

export default function AdminChatPage() {
  return <ChatView role="admin" />;
}
