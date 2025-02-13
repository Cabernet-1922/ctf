# Exercise 3-A CTF is Fun [100 points] (20 solves)
```python
from z3 import *

s = Solver()
x = BitVec('x', 64)
expr = RotateLeft(RotateLeft((RotateLeft(x ^ 0x29c4e0426e5ae53f, 32) - 0x40d8d1485e843ea8), 32) + 0x7204bb56150aa739, 32) ^ 0xd5912ad9c3bee799
s.add(expr == 0xD0F7AC93538AD5B5)

if s.check() == sat:
    sol = s.model()[x].as_long()
    print(sol.to_bytes(8, 'little').decode())
```
Add five random character in front of the printed string, input to the binary file will get you `:)`.