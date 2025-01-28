import secrets
from Crypto.Util.number import isPrime as is_prime
import os


def get_prime(b):
    while True:
        p = secrets.randbits(b)
        if int(p).bit_length() < b:
            continue
        if is_prime(p):
            return p


def main():
    p = get_prime(1024)
    q = get_prime(1024)

    n = p * q
    e = 65537

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    m0 = secrets.randbits(1024)
    c = pow(m0, e, n)

    print(f"{n, e, c = }")

    err = int(input("🚨 "))
    assert 0 < err.bit_length() <= n.bit_length()

    m1 = pow(c, d + err, n + err)
    print(f"🔑 {m1}")

    m2 = int(input("💬 "))
    assert m0 == m2

    flag = os.getenv("FLAG", "firebird{test-flag}")

    print(f"🏁 {flag}")


if __name__ == "__main__":
    main()
