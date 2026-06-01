# Use official Bun image
FROM oven/bun:1.1 AS builder

WORKDIR /app

# Copy dependency files
COPY package.json bun.lockb ./

# Install dependencies
RUN bun install --frozen-lockfile

# Copy application code
COPY . .

# Build the Next.js application
RUN bun run build

# Final stage
FROM oven/bun:1.1-slim

WORKDIR /app

# Copy built assets from builder
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/node_modules ./node_modules

# Expose port
EXPOSE 3000

# Start the application
CMD ["bun", "run", "start"]
