# basic-mod1 [Medium] (by Will Hong) - picoCTF 2022
> <p>We found this weird message being passed around on the servers, we think we
have a working decryption scheme.</p>
<p>Download the message <a href='https://artifacts.picoctf.net/c/129/message.txt' download>here</a>.</p>
<p>Take each number mod 37 and map it to the following character set: 0-25 is the
alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.</p>
<p>Wrap your decrypted message in the picoCTF flag format
(i.e. <code>picoCTF{decrypted_message}</code>)</p>


```text
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213
```

```python
res = []
for i in "350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213".split(" "):
    if int(i) % 37 <= 25:
        res.append(chr((int(i) % 37) + 97))
    elif 26 <= int(i) % 37 <= 35:
        res.append(str((int(i) % 37) - 26))
    else:
        res.append("_")


print('picoCTF{'+''.join(res)+'}')
```

flag: `picoCTF{r0und_n_r0und_add17ec2}`