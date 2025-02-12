from crypto.Util.number import bytes_to_long, getPrime
from flag import flag

p, q = getPrime(1024), getPrime(1024)
print('n =', p*q)
print('enc_flag =', pow(bytes_to_long(flag), 0x10001, p*q))
