# No Padding, No Problem [Medium] (by Sara) - picoCTF 2021
> Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it? Connect with <code>nc mercury.picoctf.net 33780</code>.

```python
from pwn import *
from Crypto.Util.number import long_to_bytes
context.log_level = 'CRITICAL'
p = remote('mercury.picoctf.net', 33780)
p.recvuntil(b'n: ')
n = int(p.recvline().decode().strip())
e = int(p.recvline()[3:].decode().strip())
c = int(p.recvline()[12:].decode().strip())

c_2 = pow(2, e, n)
c_2m = c_2 * c
p.recvuntil(b"Give me ciphertext to decrypt: ")
p.sendline(str(c_2m).encode())
p.recvuntil(b"Here you go: ")

m = int(p.recvline().decode().strip()) // 2

print(long_to_bytes(m).decode())
```
$RSA.enc(a)*RSA.enc(m) = RSA.enc(a*m)$\
$RSA.dec(a'*m')//RSA.dec(a')=(a*m)//a=m$

flag: `picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_0801973}`


Reference:
- [Unpadded RSA](https://en.wikipedia.org/wiki/Homomorphic_encryption#Partially_homomorphic_cryptosystems)