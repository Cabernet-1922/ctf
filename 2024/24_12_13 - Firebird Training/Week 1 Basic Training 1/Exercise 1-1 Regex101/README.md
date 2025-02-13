# Exercise 1-1 Regex101 [100 points] (98 solves)
> Find the flag.
https://files.firebird.sh/chal-2024/01/regex_ex.txt
The flag has the following feature:\
1.Encoded in flag{...}\
2.Inside the {}, the length is 31\
3.Inside the {}, the characters are either number or alphabet except the twenty-first character\
4.Inside the {}, the third character is either “p”, “o”, “w”\
5.Inside the {}, the eighth character and the tenth character are the same as the third character\
6.Inside the {}, the seventh character and the fifteenth character are the same as the nineteenth character\
7.Inside the {}, the first character is not number\
8.The twenty-first character is "_"\

```python
import re
with open("regex_ex.txt","r") as f:
    for line in f.readlines():
        if line.strip()[5:-1][2] in ["p","o","w"]:
            if line.strip()[5:-1][2] == line.strip()[5:-1][7] and line.strip()[5:-1][2] == line.strip()[5:-1][9]:
                if line.strip()[5:-1][6] == line.strip()[5:-1][14] and line.strip()[5:-1][6] == line.strip()[5:-1][18]:
                    print(line.strip())
```