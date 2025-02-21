# Padding Oracle [325 points] (3 solves)
```python
import requests
import re
token_ = requests.get("http://chal.firebird.sh:32000/Padding_Oracle/index.php").url.split('token=')[1]

def pkcs7_pad(data, block_size=16):
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)

def main(token):
    print(f"Token requested: {token}")
    iv_hex = token[:32]
    ciphertext_hex = token[32:]
    iv = bytes.fromhex(iv_hex)
    guest = b"Guest"
    padded_guest = pkcs7_pad(guest, 16)
    admin = b"Admin"
    padded_admin = pkcs7_pad(admin, 16)
    intermediate = bytes([a ^ b for a, b in zip(padded_guest, iv)])
    new_iv = bytes([a ^ b for a, b in zip(intermediate, padded_admin)])
    new_token = new_iv.hex() + ciphertext_hex
    print("New token:", new_token)
    res = requests.get(f"http://chal.firebird.sh:32000/Padding_Oracle/index.php?token={new_token}").text
    print("flag: ",re.findall(r"flag\{.*\}",res)[0])


main(token_)
```