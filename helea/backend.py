import os
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

users = {
    "admin": "admin",
    "user1": "user1",
    "user2": "Superhardpassword4*"
}

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
    password = request.form['psw']

    #SQL Injection 
    if username == "admin' OR '1'='1" and password == "password' OR '1'='1":
        return "Logged in as admin via SQL Injection! You captured a flag!"
    
    #login check
    if username in users and users[username] == password:
        #Redirect
        return redirect(url_for('profile', profile=username))
    else:
        return "Invalid credentials. Try again."

@app.route('/profile')
def profile():
    profile_username = request.args.get('profile')
    
    #Insecure URL manipulation
    if profile_username in users:
        return f"Welcome to {profile_username}'s profile! Your password is: {users[profile_username]} and you successfully captured a flag!"
    else:
        return "Invalid profile in URL."

if __name__ == '__main__':
    app.run(debug=True)
