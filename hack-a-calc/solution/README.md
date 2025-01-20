# Hack-a-Calc Boundary Escapade

## Steps to exploit

1. The first flag is base64 encoded in the response of a successful POST request. It is therefore enough, using a browser to display the network tab of the development tools (F12) and click on the POST request previously made. The User-Agent header, which should not be returned to the client, contains a string that can be decoded like so:

    ```shell
    echo "ZmxhZ3t9Cg==" | base64 -d
    ```

    This is to demonstrate that many servers return informations that would be best kept hidden from users view. For example, not hiding the `Server` response header may leak information about the server's software and version, potentially exposing **known vulnerabilities**.

2. The second flag requires bypassing the client frontend which has a slightly different input validation. Using tools like curl, postman or a custom script to send a POST request with the correct parameters to retrieve the `flag.txt`'s contents. Python's `open()` function can be used to read this file.

3. The third flag uses the same setup as the second. This time, the challenge is to find a way to execute the `whoami` command on the server, in under 50 characters while spaces and a few other characters are not allowed. Using `__import__('os').system()` is a very good first try but as it turns out the server return only the last ouput line which would be the exit code (`0` if successful). Using `subprocess` is therefore required and the entire command fits in at just 47 out of 50 characters.

    ```py
    __import__('subprocess').check_output()
    ```

## Automated script

```shell
python solution/solve.py
```
