FROM python:3.9-alpine

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only necessary files
COPY backend.py /app

# Set proper permissions
RUN chown -R root:root /app
RUN chmod -R 755 /app

# Create non-root user for security
# -m creates the home directory, -r the system account, -s sets the login shell
RUN addgroup -S app_group && adduser -S app_user -G app_group

# switch to this user
USER app_user

ENV HOST 0.0.0.0
ENV PORT ${PORT:-5000}
ENV DEBUG ${DEBUG:-false}

EXPOSE $PORT

CMD ["python3", "backend.py"]