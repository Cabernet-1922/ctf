# SamDisk [150 points] (21 solves)
Firstly, use tool `OfficeMalScanner.exe` to scan the `.xlsm` file
```
OfficeMalScanner.exe "GPA Calculator.xlsm" info
OfficeMalScanner.exe "GPA Calculator.xlsm" inflate
OfficeMalScanner.exe vbaProject.bin info
```
After this, you will get a `\VBAPROJECT.BIN-Macros` folder, two files `ThisWorkbook` and `Worksheet___1` are inside the folder. The password of the `classifier.rar` is inside the `Worksheet___1` which is `c4ZC5K6qUprNctGt`. \
Decompressed the `.rar` file, we will get a `flag` file, then we use command `binwalk flag`:
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1920 x 1080, 8-bit/color RGB, non-interlaced
91            0x5B            Zlib compressed data, compressed
```
This indicates that the `flag` file is actually a `.png` file, modify the extension of the file and then open the image will see the flag.