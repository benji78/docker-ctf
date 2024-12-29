import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('ctf_db.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert default users
cursor.executemany('''
INSERT INTO users (username, password)
VALUES (?, ?)
''', [
    ('admin', 'admin'),
    ('user1', 'user1pass'),
    ('user2', 'Superhardpassword4*')
])

conn.commit()
conn.close()

print("Database and users table created successfully.")
