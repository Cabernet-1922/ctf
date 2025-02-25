# Zygote RSA [250 points] (6 solves)
```python
n = 0xda5e749cfb00ebb25c9974f0c2a741223c18529f18dd56128dfe1511f637ddc66c5444980312e27fa7777c97934dac3aa7b196e1b74c22b11703ba6b72523b4223e787a7db9dc13364117532cfec7e2c9b70b5a5668d3aaefaddecb9a010e9a6ec09ad68c92b63636c102d7d70b69abf76e10f20af4762ca451ad1d1c333e4f032f0378e4abfbab957a43be10c5fea35a982763d213918a05b62ec7fcedde485b80ea9122bb3d1a4db1a1c8c6a80bba0a721c035b9685c109f45292616c70d43b474fb367ce37bbd8fe9a575ea2cc34b92d02f075aa0fe7702f10d921171ead1ce97a8faf1c78374a9052535f2df5edff19a931de0404f877e546541f762c2d3
e = 0x10001
c = 0x63344759a2562573665e48cefdfa4db76a18a142f7c5380133b3dc38ccf99e5cbcf8e9f031523ca8317c5058730710e9081f68083073153efe664fed6558626580c12f03cf40f744db8fd1a0e6701140302c49af18d177aaa777848e2d98ce458e73dcc52fe9462a0c39e6fc299094768de9c72c09336f9d599cd5684600d5abd62e5fb32b3685b8da1426ebe5983401c8ca6f61c6f6cae47110444a93040efa4ddfe192d0c383339deb9e68b9d36199b2b4ff8fbaa36e4a457a8232c976a174a3278200aeae13fedb2fc9de4e6dec34d5bae02ed07b92c8af856675fadff679531a6d238b094dbf143cd524d97c9384a38b5e99a389a5e621688f523525c84a


def fermat_factorization(n):
    a = isqrt(n)
    b2 = a * a - n

    while not is_square(b2):
        a += 1
        b2 = a * a - n

    b = isqrt(b2)
    p = a + b
    q = a - b

    return int(p), int(q)

p, q = fermat_factorization(n)

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m).decode())
```
[Fermat's factorization method](https://en.wikipedia.org/wiki/Fermat%27s_factorization_method)

