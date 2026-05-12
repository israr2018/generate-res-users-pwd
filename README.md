# install the followings
```
passlib


```



```
sudo apt update
sudo apt install python3-pip -y
pip3 install passlib
```

# Run the command
```
python3 generate_pwd.py

```

FIRST TIME (new machine)          NEXT TIME (same machine)
─────────────────────────         ────────────────────────
git clone <repo>                  cd gnerate-res-users-pwd
python3 -m venv venv              source venv/bin/activate
source venv/bin/activate          python3 script.py
pip install -r requirements.txt
python3 script.py