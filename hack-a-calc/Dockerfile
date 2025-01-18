FROM python:3.9-alpine

WORKDIR /app

# Copy only necessary files
COPY src/ /app/

# Set proper permissions
RUN chown -R root:root /app
RUN chmod -R 755 /app
RUN chmod 744 /app/flag.txt

# Create non-root user for security
RUN addgroup -S app_group && adduser -S  flag-wonderfull_escapade -G app_group

# switch to this user
USER flag-wonderfull_escapade

ENV HOST=0.0.0.0
ENV PORT=${PORT:-1337}

EXPOSE $PORT

CMD ["python3", "challenge.py"]
