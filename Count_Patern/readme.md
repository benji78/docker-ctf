# Count Pattern

![category](https://img.shields.io/badge/category-web-purple)
[![author](https://img.shields.io/badge/author-keauranthain-blue)](https://github.com/keauranthain)

## How to setup
1) Launch `setup.bat`.
2) Run `server.js`, which will send you directly to the website.

## Useful Data
- The website user account credentials are: username: "user", password: "1234".
- Tools are required for some flags.
- The database is stored in a CSV file.

## Presentation
This challenge includes four flags:
1) The first flag is pretty simple. It's not really a vulnerability but rather a way to make the website crash. Inspecting the right place can also reveal the flag.
2) The second flag is simple, but not as easy as the first. You need to find a hidden page on the website. No tools are required.
3) The third flag is of medium difficulty. Again, you need to find a page, but for this one, a tool is necessary (or a lot of intuition).
4) The fourth flag is harder. You need to find the admin password. The third flag could help you. Tools are mandatory.

## Hints

<details>
    <summary>Hint for Flag 1: Click me!</summary>

What are the limits of the fields in user page?
</details>

<details>
    <summary>Hint for Flag 2: Click me!</summary>

There is a text file that practically every website has, containing a list of webpage names. Maybe there's a secret file.
</details>

<details>
    <summary>Hint for Flag 3: Click me!</summary>

Maybe a software like ZAP can check for hidden fields with common names...
</details>

<details>
    <summary>Hint for Flag 4: Click me!</summary>

Using the previous ZAP hint, there is a `.csv` file containing all usernames and passwords. Maybe we can crack the code...
</details>

## Solution

<details>
    <summary>Solution for Flag 1: Click me!</summary>

On the user page, enter more than 10,000 characters into a field.
</details>

<details>
    <summary>Solution for Flag 2: Click me!</summary>

The `robots.txt` file contains a page named `secret_page_that_definitely_doesnt_have_a_flag_hide_inside.html`. The flag is there.
</details>

<details>
    <summary>Solution for Flag 3: Click me!</summary>

Software like ZAP can look for commonly named pages. In ZAP, if you perform a Forced Browse Directory scan, you can find a page named `secret.html`.
</details>

<details>
    <summary>Solution for Flag 4: Click me!</summary>

From the previous hint, you can find a file named `db.csv`. When you download it, all passwords are encrypted. The passwords for "user" and "admin" are 32 characters long. These passwords are hashed with MD5, which can be cracked using common online tools or a brute force tool.
</details>
