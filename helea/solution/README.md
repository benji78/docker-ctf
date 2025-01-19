# SQLi(njec)te CFT challenge

## Steps to exploit

This CTF challenges your skills in exploiting vulnerabilities in web applications. Here's how to conquer each of the 5 challenges (plus one bonus):

1. Default login credentials

    Many applications have a default username and password combination that hackers can exploit. In this challenge, you can log in as the administrator by using `admin:admin` as the credentials.

2. Bruteforce password

    The challenge provides an opportunity to brute-force the password for `user1`. Since the password is quite commun (included in the `rockyou.txt` wordlist), you can crack it using a brute-force attack tool.

3. SQL injection

    You can bypass the login by injecting `OR 1=1`. This query tricks the application into evaluating to true, allowing you to log in as the first user in the database, regardless of their actual username or password. It logs you in as the first entry in the `users` table:
    Username: anything
    Password: 'OR '1=1

4. Reflected XSS Vulnerability

    Once logged in, you can exploit a reflected XSS vulnerability present in the profile URL parameter. To do this, you can modify the URL to include a malicious script, such as:

    ```/profile?profile=<iframe src="javascript:alert(`xss`)"></iframe>```
    
    When another user clicks on this link, the malicious script will be executed in their browser, potentially revealing sensitive information or hijacking their session.

5. Malicious SQL injection to delete `users` table

    By crafting a specially crafted username and password combination like:
    ```sql
    Username: anything
    Password: '; DROP TABLE 'users
    ```
    you can inject a query that deletes the entire `users` table from the database.

6. Retrieve a user's passwords

    Now that we know we can execute anything on the database (blindly though), we could create a new user from `user2`'s password as the new username and a specific password which we can then use to select the 
    Unfortunatly for the purposes of this CTF's security the in-memory database is not persist in between requests but the attack could be pull off.
    We could even suppose that if the passwords were hashed a rainbow table could be used to find the plaintext password from the extracted hash (as loong as it is not too complex).

## Automated script

```shell
python exploits/solve.py
```

In addition there is a Proof-of-Concept of flag 6 which creates a `test.db` file in the current directory.

```shell
python exploits/poc.py
```
