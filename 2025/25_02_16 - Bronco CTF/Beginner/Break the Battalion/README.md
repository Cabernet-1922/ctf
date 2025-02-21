# Break the Battalion [10 points] (369 solves)
For every character of the input it does:
```c
arg1[i] ^= 0x50;
putchar(arg1[i]);
```
After the encryption, the modified input is compared with the literal `brigade`. If they match, the program prints "correct password"; otherwise, it prints "wrong password.

Input: `2"97145`

flag: `bronco{2"97145}`