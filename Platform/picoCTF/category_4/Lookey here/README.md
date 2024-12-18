# Lookey here [Medium] (by LT 'syreal' Jones / Mubarak Mikail) - picoCTF 2022
> <p>Attackers have hidden information in a very large mass of data in the past,
maybe they are still doing it.</p>
<p>Download the data <a href='https://artifacts.picoctf.net/c/124/anthem.flag.txt' download>here</a>.</p>

```bash
cat anthem.flag.txt | grep -oP "picoCTF{.*}"
```


flag: `picoCTF{gr3p_15_@w3s0m3_4c479940}`