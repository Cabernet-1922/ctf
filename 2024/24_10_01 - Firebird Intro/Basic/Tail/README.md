# Tail [250 points] (8 solves)
First, we can use `binwalk tail.jpg` to get below result.
```txt
/usr/lib/python3/dist-packages/binwalk/core/magic.py:431: SyntaxWarning: invalid escape sequence '\.'
  self.period = re.compile("\.")

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
4842          0x12EA          Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
284238        0x4564E         Zip archive data, encrypted at least v2.0 to extract, compressed size: 67, uncompressed size: 47, name: flag.txt
284471        0x45737         End of Zip archive, footer length: 22
```
From this, we can observe that there is a zip file inside the `.jpg` file, we can simply use `binwalk -e tail.jpg` to extract the zip file from image.\
Then, the zip file password is needed. `strings tail.jpg | less` will get all the printable strings, let's look the first few string
```txt
JFIF
jExif
cKwuVxAg0zliQFvN
Adobe Photoshop CC (Windows)
2020:08:17 01:16:06
ICC Profile
2020:08:07 14:42:55
2020:08:07 14:42:55
XICC_PROFILE
HLino
mntrRGB XYZ 
acspMSFT
IEC sRGB
```
Use some dictionary tool to crack the zip file with wordlist above, or you may directly choose the right password by luck.