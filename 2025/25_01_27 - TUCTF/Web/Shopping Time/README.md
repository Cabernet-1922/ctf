# Shopping Time [50 points] (160 solves)
```python
import hashlib
import random
import string


def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

target_prefix="c58360"
while True:
    random_string = generate_random_string()
    hash_value = hashlib.md5(random_string.encode()).hexdigest()
    if hash_value[:6] == target_prefix:
        print(random_string)
        print(hash_value)
```
Payload: `/review?item=istBc`

flag: `TUCTF{k1nd_0f_an_1d0r_vu1n!}`