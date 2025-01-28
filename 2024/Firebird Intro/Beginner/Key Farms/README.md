# Key Farms [150 points] (14 solves)
> Some keys are strong, while some are not. 

Description implies p and q are weak keys, which means the p and q might be known. So we can factorise `n` in [factorDB](https://factordb.com/) to get the p and q instantly. \
Noted that you might get more than one combination of p and q, but only the one with same length will work (getPrime(1024)).\
After getting correct p and q, run the below script will get the flag:
```python
phi = (p - 1) * (q - 1)
e = 0x10001

d = inverse(e, phi)
dec_flag = pow(enc_flag, d, n)
flag = long_to_bytes(decrypted_flag)
print(flag.decode())
```