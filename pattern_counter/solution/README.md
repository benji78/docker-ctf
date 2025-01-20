# Pattern Counter

## Steps to exploit

#### Solution for Flag 1

On the user page, enter more than 10,000 characters into a field.

#### Solution for Flag 2

The `robots.txt` file contains a page named `secret_page_that_definitely_doesnt_have_a_flag_hide_inside.html`. The flag can be found by navigating to it.

#### Solution for Flag 3

Software like ZAP can look for commonly named pages. In ZAP, if you perform a Forced Browse Directory scan, you can find a page named `secret.html`.

#### Solution for Flag 4

From the previous hint, you can find a file named `db.csv`. When you download it, all passwords are encrypted. The passwords for "user" and "admin" are 32 characters long. These passwords MD5 hashes, which can be brute force with rainbow tables.

## Automated script

```shell
python solution/solve.py
```
