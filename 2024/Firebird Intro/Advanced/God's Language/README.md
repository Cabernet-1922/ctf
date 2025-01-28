# God's Language [350 points] (8 solves)
`manual_enc.txt` simply tells the encryption, write it in python code would be like
```python
import base64
flag = "flag{.*}"
def encrypt(i):
    tmp = []
    for a in i:
        tmp.append(pow(ord(a), 101, 127))
    return base64.b64encode(bytes(tmp)).decode()
```
Given encrypted message `UBQnRD9XH2F9H2EXcn0lYWEKBU4fITN3`, construct the decryption script based on the encryption script above.
```python
import base64
def decrypt(encoded):
    encrypted = list(base64.b64decode(encoded))
    print(encrypted)
    decrypted = [pow(x, 5, 127) for x in encrypted]
    return ''.join(chr(x) for x in decrypted)
```
