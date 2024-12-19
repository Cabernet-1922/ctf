# basic-mod2 [Medium] (by Will Hong) - picoCTF 2022
> <p>A new modular challenge!</p>
<p>Download the message <a href='https://artifacts.picoctf.net/c/180/message.txt' download>here</a>.</p>
<p>Take each number mod 41 and find the modular inverse for the result. Then map
to the following character set: 1-26 are the alphabet, 27-36 are the decimal
digits, and 37 is an underscore.</p>
<p>Wrap your decrypted message in the picoCTF flag format
(i.e. <code>picoCTF{decrypted_message}</code>)</p>


```text
268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131 
```


We can reuse and modify the solve script in [basic-mod1](../basic-mod1):
```python
res = []
for i in "268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131".split(" "):
    if 1 <= pow(int(i),-1,41) <= 26:
        res.append(chr(pow(int(i),-1,41) + 96))
    elif 27 <= pow(int(i),-1,41) <= 36:
        res.append(str(pow(int(i),-1,41) - 27))
    elif pow(int(i),-1,41) == 37:
        res.append("_")


print('picoCTF{'+''.join(res)+'}')
```

flag: `picoCTF{1nv3r53ly_h4rd_8a05d939}`