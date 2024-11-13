# Docker CFT

## Setup Instructions

1. Install Docker (and Docker Compose)
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
   docker-compose up --build
   ```

5. Open the challenge in you browser

   [127.0.0.1:1337](http://127.0.0.1:1337)

## Solution

The `SOLUTION.md` can be found in the `exploits` folder of each challenge. There is also a script automating the exploit. For example, you can run :

```shell
python exploits/solve.py
```