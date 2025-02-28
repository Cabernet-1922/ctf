# Significance of Reversing [200 points] (189 solves)
```python
with open('Reverseme.png', 'rb') as file:
    data = file.read()

open('Reverseme.png', 'wb') as file:
    file.write(data[::-1])
```
Reverse the bytes of the file to a `.elf` file, then run it to get the flag.

flag: `ACECTF{w3_74lk_4b0u7_r3v3r53}`