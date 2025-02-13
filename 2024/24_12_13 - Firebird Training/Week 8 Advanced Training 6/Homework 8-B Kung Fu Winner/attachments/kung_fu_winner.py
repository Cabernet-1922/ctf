from crypto.Util.number import *
from math import gcd
from secret import flag


def main():
    m = bytes_to_long(flag)
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q

    while True:
        d = getRandomNBitInteger(int(263.3))
        s = getRandomNBitInteger(int(463.3))
        d = d * s
        if d**4 > n and gcd(d, (p-1)*(q-1)) == 1: break

    e =  pow(d, -1, (p-1)*(q-1))
    c = pow(m, e, n)

    print(f'{n = }')
    print(f'{e = }')
    print(f'{c = }')

    c_list = []
    n_list = []
    for _ in range(3):
        p1 = getPrime(512)
        q1 = getPrime(512)
        n1 = p1*q1
        e1 = 3
        assert s < n1 and s**e1 > n1
        n_list.append(n1)
        c_list.append(pow(s, e1, n1))

    print("c1s = ", c_list)
    print("n1s = ", n_list)

if __name__ == '__main__':
    main()