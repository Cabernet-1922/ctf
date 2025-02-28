# Broken Secrets [100 points] (275 solves)
```bash
> file Brokenfr
```
The attachment appear to be a 7-zip file, extract the files and browse around will see a suspicious file named `not_so_suspicious_file`.

```bash
> xxd not_so_suspicious_file | head
00000000: 122e d4a7 0d0a 1a0a 0000 000d 4948 4452  ............IHDR
00000010: 0000 015e 0000 00c8 0800 0000 0085 08d6  ...^............
00000020: 2c00 0000 0467 414d 4100 00b1 8f0b fc61  ,....gAMA......a
00000030: 0500 0000 2063 4852 4d00 007a 2600 0080  .... cHRM..z&...
00000040: 8400 00fa 0000 0080 e800 0075 3000 00ea  ...........u0...
00000050: 6000 003a 9800 0017 709c ba51 3c00 0000  `..:....p..Q<...
00000060: 0262 4b47 4400 00aa 8d23 3200 0000 0970  .bKGD....#2....p
00000070: 4859 7300 0000 4800 0000 4800 46c9 6b3e  HYs...H...H.F.k>
00000080: 0000 0007 7449 4d45 07e9 0113 0a2f 3255  ....tIME...../2U
00000090: 0fdd 1000 000b 7c49 4441 5478 daed 9a6b  ......|IDATx...k
```
This appears to be a png since it contains an `IHDR` chunk:
> A valid PNG image must contain an IHDR chunk 

Therefore, try to repair the header to make the image is viewable, and in fact, only the first four bytes of the header need to be fixed:
```
12 2e d4 a7  ->  89 50 4e 47
```
Lastly, change the extension to get the flag.

flag: `ACECTF{h34d3r_15k3y}`