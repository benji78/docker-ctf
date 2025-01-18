# Example CFT challenge

## Steps to exploit

1. The first flag is base64 encoded in the response of a successful post request. It is therefore enough, using a browser to display the network tab of the development tools (F12) and click on the POST request previously made. The User-Agent header, which should not be returned to the client, contains a string that can be decoded like so:

```shell
echo "ZmxhZ3t9Cg==" | base64 -d
```

2. The second flag requires bypassing the client frontend which has a slightly different input validation and use tools like curl, postman or a custom script to send a POST request with the correct parameters to retrieve the `flag.txt`'s contents. Python's `open()` function can be used to read a file.

3. The third flag uses the same setup as the second. This time, the difficulty is to find a way to execute the `whoami` command on the server while spaces are not allowed and in under 50 characters. Using `__import__('os')` might be a good first try but as it turns out the server return only the last ouput line which would be the exit code (`0` if successful). Using `subprocess` is therefore needed and the entire command fits in at just 47 out of 50 characters.

## Automated script

```shell
python solution/solve.py
```
