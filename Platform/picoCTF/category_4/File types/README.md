# File types [Medium] (by Geoffrey Njogu) - picoCTF 2022
> This file was found among some files marked confidential but my pdf reader
cannot read it, maybe yours can.
You can download the file from <a href='https://artifacts.picoctf.net/c/80/Flag.pdf' download>here</a>.

The most stupid challenge in picoCTF, basically use different tools to extract the nested files. In the last file we get:
```text
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33633739633562617d0a
```
Then, convert the hex to ascii characters.

flag: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}`