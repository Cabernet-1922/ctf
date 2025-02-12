# just read the flag [1000 points] (1 solves) (Post-Match Solve)
The magic in this challenge is use comment to specify `utf-7` encoding, allowing us to encode restricted characters using allowed sequences. Then, encode restricted characters like `(`, `)`, `'`, `.` using UTF-7 sequences: 
```
`ACg` -> `(`
`ACk` -> `)`
`ACI` -> `'`
`AC4` -> `.`
```
Full payload:
```bash
Just read the flag.txt! Very simple!
> # -*- coding: utf-7 -*-
> print+ACg-open+ACg-+ACI-flag+AC4-txt+ACI-+ACk-+AC4-read+ACg-+ACk-+ACk-
>
firebird{v3ry_51mpl3_70_r34d_7h3_fl46,_r16h7?}
```
