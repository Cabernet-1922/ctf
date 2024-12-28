# transposition-trial [Medium] (by Will Hong) - picoCTF 2022
> Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message <a href='https://artifacts.picoctf.net/c/192/message.txt' download>here</a>.

```python
msg = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"
res = ""
for i in range(0,len(msg),3):
    temp = msg[i:i+3]
    res += temp[-1] + temp[0:2]

print(res)
```

Split the message up into block of 3, then the put the last character of each block to the front:
```text
The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}
```

flag: `picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}`