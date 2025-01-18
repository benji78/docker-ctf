# Hack-a-Calc Boundary Escapade

![category](https://img.shields.io/badge/category-web-purple)
![score](https://img.shields.io/badge/score-100-blue)
[![author](https://img.shields.io/badge/author-benji78-blue)](https://github.com/benji78)

## Presentation

This challenge has three flags.\
The first is not too difficult to find so you probably don't need a hint if you know where to look.\
The second requires some trial and error to get your hands on the text.\
The third and most difficult is the name of the user executing the python server process.

## Hints

<details>
    <summary>Hint for Flag 1: Click me!</summary>

Sometimes servers leak information that should proably be best kept hidden from users. You may have found that this server is running Python and uses SimpleHTTP (unless it is running behing a reverse proxy and this information has been overwritten). But isn't there more info?
</details>
<details>
    <summary>Hint for Flag 2: Click me!</summary>

Client and server side validations are often managed separatly, with different programming languages, etc. leading to discrepancies in what is allowed. Go ahead and explore beyond browser-based restrictions! You are looking for a `flag` `txt` file.
</details>
<details>
    <summary>Hint for Flag 2: Click me!</summary>

If you got the second flag, you should not be far off, but you may have realised spaces are not allowed! Remember, you are looking for *who* is executing the python process.
</details>

## [Solution](exploits/SOLUTION.md)
