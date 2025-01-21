# SQLi(njec)te

![category](https://img.shields.io/badge/category-WEB-purple)
[![author](https://img.shields.io/badge/author-Hgriveau-blue)](https://github.com/Hgriveau)

## Presentation

This challenge has five flags, plus one bonus.\
![score](https://img.shields.io/badge/EASY-green)
The first flag involves exploiting a classic security oversight with default credentials.\
![score](https://img.shields.io/badge/MEDIUM-yellow)
The second flag requires you to use common password cracking techniques to gain unauthorized access.\
![score](https://img.shields.io/badge/MEDIUM-yellow)
The third flag tests your knowledge of basic SQL injection techniques to bypass authentication.\
![score](https://img.shields.io/badge/HARD-orange)
The fourth flag involves exploiting client-side vulnerabilities through cross-site scripting.\
![score](https://img.shields.io/badge/VERY_HARD-red)
The fifth flag challenges you to craft a destructive SQL injection that could compromise database integrity.

![score](https://img.shields.io/badge/VERY_HARD-red)
The bonus flag requires advanced SQL injection techniques to extract sensitive user information. However for the
purposes of this CTF, the database was made ephemeral which means on every request it is recreated and stored only
in-memory. As such this attack could be pulled off in this docker environment only if you disable the container's
read-only filesystem and give the SQLite database a file name. (A proof-of-concept is avaliable in the solution)

## Setup

Build and run the challenge using docker compose

```shell
docker compose up --build -d
```

Open the challenge in you browser at [127.0.0.1:5000](http://127.0.0.1:5000)

## [Solution](solution/README.md)
