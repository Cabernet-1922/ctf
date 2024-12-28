# tunn3l v1s10n [Medium] (by Danny) - picoCTF 2021
> We found this <a href='//mercury.picoctf.net/static/d0129ad98ba9258ab59e7700a1b18c14/tunn3l_v1s10n'>file</a>. Recover the flag.

With `exiftool`, we know the file type is actually `bmp`, but change the extension of the file will still not allow to view the image. Look at the hexdump of the file, the header is corrupted. Modify the header:
```text
42 4D 8E 26 2C 00 00 00 00 00 BA D0 00 00 BA D0 00 00 6E 04 00 00 32 01 00 00

↓

42 4D 8E 26 2C 00 00 00 00 00 36 00 00 00 28 00 00 00 6E 04 00 00 52 03 00 00
```
`36 00 00 00` for the offset to pixel data, and `28 00 00 00` for DIB header size. And adjust the width `6E 04` and height `52 03` . This will correctly display the flag.

flag: `picoCTF{qu1t3_a_v13w_2020}`