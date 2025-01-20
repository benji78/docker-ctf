# Hack-a-Calc Boundary Escapade

![category](https://img.shields.io/badge/category-WEB-purple)
[![author](https://img.shields.io/badge/author-benji78-blue)](https://github.com/benji78)

## Presentation

This challenge has three flags.\
![score](https://img.shields.io/badge/EASY-green)
The first is not too difficult to find so you probably don't need a hint if you know where to look.\
![score](https://img.shields.io/badge/MADIUM-yellow)
The second requires some trial and error to get your hands on a special txt file's content.\
![score](https://img.shields.io/badge/VERY_HARD-red)
The third and most difficult is the name of the user executing the python server process. (This flag's format is: `flag-...`)

## Setup

Build and run the challenge using docker compose

```shell
docker compose up --build -d
```

Open the challenge in you browser at [127.0.0.1:1337](http://127.0.0.1:1337)

## Hints

<details>
    <summary>Hint for Flag 1: Click me!</summary>

Sometimes servers leak information that should proably be best kept hidden from users. You may have found that this server is running Python and uses SimpleHTTP (unless it is running behing a reverse proxy and this information has been overwritten). But isn't there more info?
</details>
<details>
    <summary>Hint for Flag 2: Click me!</summary>

Client and server side validations are often managed separatly, with different programming languages, etc. leading to discrepancies in what is allowed. Go ahead and explore beyond browser-based restrictions! You are looking for a `flag.txt` file.
</details>
<details>
    <summary>Hint for Flag 3: Click me!</summary>

If you got the second flag, you should not be far off, but you may have realised spaces are not allowed! Remember, you are looking for the name of the user who is executing the python process.
</details>

## [Solution](solution/README.md)
