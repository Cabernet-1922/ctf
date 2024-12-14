# Nekovich and Laser Sport [150 points] (19 solves)
Start from `[rbp-64]`, the first five chars in ascii is `flag{`, which confirmed that this is the way to solve this challenge. Use python script to sort the rbp and use the ascii code after the rbp to get the full flag.

```python
import re

assembly = """
        mov     BYTE PTR [rbp-46], 112
        mov     BYTE PTR [rbp-64], 102
        mov     BYTE PTR [rbp-60], 123
        mov     BYTE PTR [rbp-63], 108
        mov     BYTE PTR [rbp-41], 82
        mov     BYTE PTR [rbp-35], 115
        mov     BYTE PTR [rbp-62], 97
        mov     BYTE PTR [rbp-34], 111
        mov     BYTE PTR [rbp-52], 99
        mov     BYTE PTR [rbp-40], 110
        mov     BYTE PTR [rbp-22], 95
        mov     BYTE PTR [rbp-26], 95
        mov     BYTE PTR [rbp-28], 114
        mov     BYTE PTR [rbp-27], 115
        mov     BYTE PTR [rbp-33], 95
        mov     BYTE PTR [rbp-37], 97
        mov     BYTE PTR [rbp-42], 101
        mov     BYTE PTR [rbp-55], 95
        mov     BYTE PTR [rbp-29], 101
        mov     BYTE PTR [rbp-49], 51
        mov     BYTE PTR [rbp-47], 95
        mov     BYTE PTR [rbp-24], 51
        mov     BYTE PTR [rbp-21], 80
        mov     BYTE PTR [rbp-45], 52
        mov     BYTE PTR [rbp-20], 101
        mov     BYTE PTR [rbp-53], 95
        mov     BYTE PTR [rbp-61], 103
        mov     BYTE PTR [rbp-19], 87
        mov     BYTE PTR [rbp-48], 121
        mov     BYTE PTR [rbp-23], 119
        mov     BYTE PTR [rbp-18], 125
        mov     BYTE PTR [rbp-43], 116
        mov     BYTE PTR [rbp-57], 101
        mov     BYTE PTR [rbp-30], 115
        mov     BYTE PTR [rbp-32], 108
        mov     BYTE PTR [rbp-44], 84
        mov     BYTE PTR [rbp-36], 108
        mov     BYTE PTR [rbp-25], 112
        mov     BYTE PTR [rbp-17], 0
        mov     BYTE PTR [rbp-50], 100
        mov     BYTE PTR [rbp-54], 117
        mov     BYTE PTR [rbp-59], 100
        mov     BYTE PTR [rbp-31], 52
        mov     BYTE PTR [rbp-56], 115
        mov     BYTE PTR [rbp-51], 95
        mov     BYTE PTR [rbp-39], 63
        mov     BYTE PTR [rbp-38], 95
        mov     BYTE PTR [rbp-58], 48
"""

print("".join([chr(int(str(i).split(",")[-1].strip())) for i in sorted(re.findall(r'\[.*', assembly), reverse=True)]))
```