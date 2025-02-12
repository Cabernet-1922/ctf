# Powerplay [50 points] (95 solves)
```python
from sympy.ntheory.primetest import is_square
from gmpy2 import *

a = 4294967296
for j in range(1, 25):
    for i in range(1000000):
        if is_square(a * i - j):
            print(j, i, "->", int(sqrt(a * i - j)))
```
The initial power will be 34716455.

flag: `ENO{d0_n0t_be_s0_neg4t1ve_wh3n_y0u_sh0uld_be_pos1t1ve}`