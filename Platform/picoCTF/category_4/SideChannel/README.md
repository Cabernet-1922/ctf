# SideChannel [Hard] (by Anish Singhani) - picoCTF 2022
> <p>There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?</p>
<p>Download the PIN checker program here <a href='https://artifacts.picoctf.net/c/74/pin_checker' download>pin_checker</a></p>

```python
import os
import time
test_count = 5
numbers = "0123456789"
res = ""
# temp = ""
for i in range(8):
    pool = [.0] * len(numbers)
    for j in range(len(numbers)):
        single_digit_pool = [.0] * test_count
        for k in range(test_count):
            payload = str(res+numbers[j]).ljust(8,"0")
            # payload = str(temp+numbers[j]).ljust(8,"0")
            print(payload)
            start = time.time()
            os.system(f"echo {payload} | ./pin_checker > /dev/null")
            single_digit_pool[k] = time.time()-start
        pool[j] = min(single_digit_pool)
    res += str(pool.index(max(pool)))
    # temp += "0"

print(res)
```
After running the program, we can see all the correct digit of the pin, which is `48390513`

flag: `picoCTF{t1m1ng_4tt4ck_914c5ec3}`

Reference:
[Time-based attack](https://en.wikipedia.org/wiki/Timing_attack)