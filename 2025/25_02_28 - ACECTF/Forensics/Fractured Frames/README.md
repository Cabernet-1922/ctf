# Fractured Frames [300 points] (43 solves)
```bash
> exiftool challenge1.jpg
ExifTool Version Number         : 12.76
File Name                       : challenge1.jpg
Directory                       : .
File Size                       : 7.3 kB
File Modification Date/Time     : 2025:02:28 16:08:24+08:00
File Access Date/Time           : 2025:02:28 16:09:04+08:00
File Inode Change Date/Time     : 2025:02:28 16:09:03+08:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 72
Y Resolution                    : 72
Image Width                     : 182
Image Height                    : 255
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 182x255
Megapixels                      : 0.046
```
The `megapixels=0.046` reveals that the current image size is not the actual size. So try to modify the size in the header:
```bash
FF D8 FF E0 00 10 4A 46 49 46 00 01 01 00 00 48 00 48 00 00 FF DB 00 43 00 0A 07 07 08 07 06 0A 08 08 08 0B 0A 0A 0B 0E 18 10 0E 0D 0D 0E 1D 15 16 11 18 23 1F 25 24 22 1F 22 21 26 2B 37 2F 26 29 34 29 21 22 30 41 31 34 39 3B 3E 3E 3E 25 2E 44 49 43 3C 48 37 3D 3E 3B FF DB 00 43 01 0A 0B 0B 0E 0D 0E 1C 10 10 1C 3B 28 22 28 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B 3B FF C0 00 11 08 00 FF 00 B6 03 01 22 00 02 11 01 03 11```
Since the current size is 182x255, B6xFF in hex. Easy locate `00 FF 00 B6`, then simply modify it to `01 FF 00 B6` will be able to view the flag.

flag: `ACECTF{th1s_sh0uld_b3_en0u6h}`