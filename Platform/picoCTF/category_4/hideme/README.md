# hideme [Medium] (by Geoffrey Njogu) - picoCTF 2023
> Every file gets a flag.\
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye <a href='https://artifacts.picoctf.net/c/261/flag.png' download>here</a>.

`strings flag.png` prints:
```text
lFm
;ss5
d|\H
I       ax
z/cc
P</==3
+(Lt
secret/UT
pVuaG
secret/flag.pngUT
```
`secret/flag.png` caught my attention. Then, with `binwalk -e flag.png` will extract this hidden flag file.

flag: `picoCTF{Hiddinng_An_imag3_within_@n_ima9e_96539bea}`