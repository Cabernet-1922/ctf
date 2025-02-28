# Cryptic Pixels [200 points] (206 solves)
```bash
> binwalk -e CrypticPixels.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1600 x 1080, 8-bit/color RGBA, non-interlaced
91            0x5B            Zlib compressed data, compressed

WARNING: Extractor.execute failed to run external extractor 'jar xvf '%e'': [Errno 2] No such file or directory: 'jar', 'jar xvf '%e'' might not be installed correctly
753923        0xB8103         Zip archive data, encrypted at least v1.0 to extract, compressed size: 38, uncompressed size: 26, name: flag.txt
754121        0xB81C9         End of Zip archive, footer length: 22
```
Easy extract the hidden data, then rockyou.txt to crack the zip file. Password: `qwertyuiop`. Finally do caesar shift with `offset=17` to the encrypted flag.

flag: `ACECTF{h4h4_y0u'r3_5m4r7}`

