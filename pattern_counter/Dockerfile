FROM node:20-alpine

WORKDIR /app

# Copy only necessary files
COPY public/ /app/public/
COPY server.js package.json package-lock.json /app/

RUN npm install

# Create non-root user for security
RUN addgroup -S express_group && adduser -S express_user -G express_group

# switch to this user
USER express_user

ENV HOST=0.0.0.0
ENV PORT=${PORT:-3000}

CMD ["node","server.js"]
