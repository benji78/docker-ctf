import os
import re
import sqlite3
from flask import Flask, request, render_template_string, redirect, url_for, session

# Flask App
app = Flask(__name__)

# Set a secret key for flask session management
app.secret_key = os.urandom(24)

# Database file (in memory database with `:memory:` but it won't persist between requests)
DATABASE = ':memory:'

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

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTF Login</title>
    <style>
        .error { color: red; margin: 10px 0; }
        .container { margin: 10px 0; }
        input { margin: 5px 0; padding: 5px; }
    </style>
    <script>
        function togglePasswordVisibility() {
            const passwordField = document.getElementById('psw');
            const toggleButton = document.getElementById('togglePassword');
            
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                toggleButton.textContent = 'Hide Password';
            } else {
                passwordField.type = 'password';
                toggleButton.textContent = 'Show Password';
            }
        }
    </script>
</head>
<body>
    <h2>Login CTF Challenge</h2>
    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}
    <form action="/login" method="post">
        <div class="container">
            <label for="uname"><b>Username</b></label><br>
            <input type="text" placeholder="Username" name="uname" pattern="^\\w+$" required><br>

            <label for="psw"><b>Password</b></label><br>
            <input type="password" placeholder="Password" name="psw" id="psw" required>
            <button type="button" id="togglePassword" onclick="togglePasswordVisibility()">Show Password</button>
        </div>
        <div class="container">
            <button type="submit">Login</button>
            <label>
                <input type="checkbox" checked="checked" name="remember"> Remember me
            </label>
        </div>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    """Display login page"""
    error = request.args.get('error')
    return render_template_string(HTML_TEMPLATE, error=error)

@app.route('/login', methods=['POST'])
def login():
    """Handle login attempts"""
    # Connect to the SQLite database
    db, error = init_db()
    if error:
        return redirect(url_for('index', error=error))

    try:
        username = request.form.get('uname', '')
        password = request.form.get('psw', '')
        print(username, password)

        if not username or not password:
            return redirect(url_for('index', error="Username and password are required"))
        if not re.match(r'^\w+$', username):
            return redirect(url_for('index', error="Username can only contain letters, numbers, and underscores"))

        # Vulnerable query that is susceptible to SQL injection
        query = f"SELECT username, password FROM users WHERE username='{username}' AND password='{password}'"
        db.executescript(query)
        try:
            cursor = db.execute(query)
            user = cursor.fetchone()
            print(username, password, user)
        except Exception as e:
            print(e)
            if str(e) == "no such table: users":
                return redirect(url_for('index', error=f"{str(e)}" + " flag{ToTal_DamaGe}"))
            else: raise Exception(e)

        if user:
            session['username'] = user['username'] # Set session
            return redirect(url_for('profile', profile=user['username']))
        else:
            return redirect(url_for('index', error="Invalid credentials"))

    except Exception as e:
        print(e)
        return redirect(url_for('index', error=f"An error occurred: {str(e)}"))
    finally:
        db.close()

@app.route('/profile')
def profile():
    """Display user profile"""
    # Connect to the SQLite database
    db, error = init_db()
    if error:
        return redirect(url_for('index', error=error))

    if 'username' not in session:
        return redirect(url_for('index', error="Please login first"))

    logoutBtn = '<br><br><form action="/logout"><input type="submit" value="LogOut" /></form>'

    username = request.args.get('profile')
    if '<iframe src="javascript:alert(`xss`)">' in username:
        logoutBtn += "<br>flag{RefLeCted_Xss}"
    elif 'alert(' in username:
        logoutBtn += 'Try again with the &lt;iframe …=&quot;…alert(`xss`)&quot;&gt; syntax'

    if session['username'] == 'default':
        logoutBtn = " flag{firstDBuser_InJecTed}<br>Have you found the admin?" + logoutBtn
    if session['username'] == 'admin':
        logoutBtn = " flag{admin_DefAultPaSS}<br>Have you found the FIRST user?" + logoutBtn
    if session['username'] == 'user1':
        logoutBtn = " flag{youRock_BRuTeFoRce}<br>Have you found the SECOND user?" + logoutBtn

    return f"Welcome {username}!" + logoutBtn

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    host=os.environ.get("HOST", "127.0.0.1")
    port=os.environ.get("PORT", "5000")
    debug=os.environ.get("DEBUG", "true").lower() in ("true", "1") # possible values: true, 1, false, 0 (converted to boolean)

    # A production appliation should for example use guincorn to be able to distribute the load with multiple threads, but this app will not receive much trafic
    app.run(host, port, debug)
