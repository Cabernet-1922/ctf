# RSAaaS [255 points] (271 solves)
The RSA implementation is vulnerable to exploit if phi and e is not coprime, and will occur error lead to the printing of flag. Thus, to find out a set of p and q that will make phi is dividable by e: 
```python
from Crypto.Util.number import getPrime
from gmpy2 import *
e = 65537
for i in range(10000000):
    p = getPrime(64)
    q = getPrime(64)
    phi = (p - 1) * (q - 1)

    if gcd(phi, e) != 1:
        print(p,q)
```
A few sets of p and q:
```text
# 12355924549876153973 13154862774554295283
# 14787738905283900341 16426650592941868663
# 14143753128529143949 18140897410997293129
# 9627112014214432277 11328823623490381147
# 13426561959132332089 11339001216278449013
# 13220192626897171651 10698828738123099377
# 15947489352400409957 10468844924923550267
```

flag: `lactf{actually_though_whens_the_last_time_someone_checked_for_that}`