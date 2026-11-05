FROM mirror.gcr.io/library/node:20-alpine AS base

# Step 1: Install dependencies
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm install --legacy-peer-deps

# Step 2: Build the source code
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . ./

ENV NEXT_TELEMETRY_DISABLED=1
ENV NEXT_PUBLIC_FIREBASE_PROJECT_ID="ai-yashcom"
ENV FIREBASE_PROJECT_ID="ai-yashcom"
ENV NEXT_PUBLIC_FIREBASE_API_KEY="AIzaSyAV2-YqCyBURq2uzB-X8vJnAGpZQSj3SVg"
ENV NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN="ai-yashcom.firebaseapp.com"
ENV NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET="ai-yashcom.firebasestorage.app"
ENV NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID="236075352424"
ENV NEXT_PUBLIC_FIREBASE_APP_ID="1:236075352424:web:665d88c97bdf117cfe56dd"
ENV NEXT_PUBLIC_FIREBASE_DATABASE_URL="https://ai-yashcom-default-rtdb.asia-southeast1.firebasedatabase.app/"
ENV NEXT_PUBLIC_FIREBASE_VAPID_KEY="BJaf-iluYddPeha6KBAKi0MXQwbaONu2SkBT6skTmlcj2u508XjScXCnAXIedu1DCTBBHYoMNhZ3ycxeZnAKho4"

RUN npm run build

# Step 3: Production runner
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
ENV PORT=8080
ENV HOSTNAME="0.0.0.0"

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public

# Automatically leverage output traces to reduce image size
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 8080

CMD ["node", "server.js"]
