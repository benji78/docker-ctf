import os
from flask import Flask, request, render_template_string, redirect, url_for
import sqlite3

# Flask App
app = Flask(__name__)

# SQLite3 Database Helper Function
def get_db_connection():
    # Connect to the SQLite database file
    conn = sqlite3.connect('ctf_db.db')  # The database file name is 'ctf_db.db'
    conn.row_factory = sqlite3.Row  # This allows us to access rows as dictionaries
    return conn

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CTF Login</title>
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
        <form action="/login" method="post">
            <div class="container">
                <label for="uname"><b>Username</b></label>
                <input type="text" placeholder="Username" name="uname" required>

                <label for="psw"><b>Password</b></label>
                <input type="password" placeholder="Password" name="psw" id="psw" required>
                
                <button type="button" id="togglePassword" onclick="togglePasswordVisibility()">Show Password</button>

                <button type="submit">Login</button>
                <label>
                    <input type="checkbox" checked="checked" name="remember"> Remember me
                </label>
            </div>
        </form>
    </body>
    </html>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['uname']
    print(username)
    password = request.form['psw']
    print(username,password)
    # Connect to the SQLite database
    conn = get_db_connection()
    cursor = conn.cursor()
    print(username,password)
    # Vulnerable query that is susceptible to SQL injection

    query = f"SELECT username, password FROM users WHERE username='{username}' AND password='{password}'"
    cursor.executescript(query)

    # i'm using sqlite3 for simplicity of installation, however it's one of the only database that doesn't support executing multiple statements (sqlite3.ProgrammingError: You can only execute one statement at a time.)
    # This would work with databases like mysql or postgresql. I added this line below for when form input is not malicious:
    query = f"SELECT username, password FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    print(query,username,password)

    conn.close()

    if user:
        return redirect(url_for('profile', profile=user[0]))  # user[0] corresponds to the username
    else:
        return "Invalid credentials. Try again."

@app.route('/profile')
def profile():
    profile_username = request.args.get('profile')
    
    # Fetch user data
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT username, password FROM users WHERE username=?', (profile_username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        if user['username'] == "user2":
            return f"Welcome to {user['username']}'s profile! Your password is: {user['password']}, your flag is flag1"
        else:
            return f"Welcome to {user['username']}'s profile! Your password is: {user['password']}"
    else:
        return "Invalid profile in URL."

if __name__ == '__main__':
    app.run(debug=True)
