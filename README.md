# Docker CFT

## Setup Instructions

1. Install Docker (and Docker Compose if you have an old version of docker)
2. Clone this repository

    ```shell
    # using SSH
    git clone git@github.com:benji78/docker-ctf.git
    # or HTTP (if you did not setup ssh keys)
    git clone https://github.com/benji78/docker-ctf.git
    ```

3. go to the challenge folder

   ```shell
   cd docker-ctf/example
   ```

4. Build and run the challenge

   ```shell
   docker-compose up --build -d
   ```

5. Open the challenge in you browser

   [127.0.0.1:1337](http://127.0.0.1:1337)

The objective is to find as many flags as possible for each challenge. CTF flags use the format `flag{...}` to clearly identify the solution to a challenge. The text within the curly braces is the specific answer you've found.

## Solution

A solution to each challenge can be found in the `solution` folder of each challenge and details are provided in the `README.md`. There is also a script automating the exploit. For example, you can run :

```shell
python solution/solve.py
```