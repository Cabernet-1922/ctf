# Homework 1-1 Finding grepo [100 points] (56 solves)
The condition we need to meet:
- The flag begins with flag{ and ends with }.
- The flag is 33 characters long (including the "flag{}")
- The 31th char is either G, R, E, or P.
- The 8th and 16th char are non-alphanumeric, but there are still 2 non-alphanumeric characters hidden inside. UwU
- The 18th and the 27th char are of the same characters but are also case-insensitive.
- The 14th and 24th char are the same.

You are expected to run the script under linux, since there are some forbidden character `* " / \ < > : | ?` in windows for naming folder or file. When unzip such file under windows, those illegal character will automatically be changed to `_`, which will eventually get a wrong flag.

```python
import os,re

dir = "HW1-1\\flag{"
for root, dirs, files in os.walk(dir):
    flag = re.sub(r"\\","",root.lstrip("HW1-1\\"))
    if len(flag) == 33:
        if flag[13] == flag [23]:
            if flag[17].upper() == flag[26].upper():
                if flag[30] in ['G','R','E','P']:
                    print(flag)
```
