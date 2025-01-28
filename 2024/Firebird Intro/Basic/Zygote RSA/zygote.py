import gmpy2
from crypto.Util import number
from flag import flag


def gen_key(key_size=1024, e=65537):
    p = number.getPrime(key_size)
    q = p + (number.getRandomInteger(key_size // 2) << 1)
    while not number.isPrime(q):
        q += 2
    n = p * q
    phin = (p - 1) * (q - 1)
    d = number.inverse(e, phin)
    return n, d


def encrypt(m, n, e):
    return gmpy2.powmod(m, e, n)


e = 65537
n, _ = gen_key(e=e)
m = int.from_bytes(flag, 'big')
c = encrypt(m, n, e)
print(f"n = {hex(n)}\n")
print(f"e = {hex(e)}\n")
print(f"c = {hex(c)}")
