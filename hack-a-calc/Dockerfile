FROM python:3.9-slim-buster

WORKDIR /app

# Copy only necessary files
COPY src/ /app/

# Set proper permissions
RUN chown -R root:root /app
RUN chmod -R 755 /app
RUN chmod 744 /app/flag.txt

# Create non-root user for security
# -m creates the home directory, -r the system account, -s sets the login shell
RUN useradd -m -r -s /bin/bash flag-wonderfull_escapade

# switch to this user
USER flag-wonderfull_escapade

ENV HOST=0.0.0.0
ENV PORT=${PORT:-1337}

EXPOSE $PORT

CMD ["python3", "challenge.py"]
