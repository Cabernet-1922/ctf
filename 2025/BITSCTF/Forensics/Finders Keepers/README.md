# Finders Keepers [120 points] (139 solves)
If you check the image file, you may find that there are additional data after IEND chunk,
```bash
$ pngcheck weird.png
zlib warning:  different version (expected 1.2.13, using 1.3)

weird.png  additional data after IEND chunk
ERROR: weird.png

$ zsteg weird.png
[?] 631143 bytes of extra data after image end (IEND), offset = 0x12005
extradata:0         .. file: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1280x1000, components 3
```
Therefore, you can either extract the hidden `jpg` file by using `foremost` or `dd`:
```
$ dd if=weird.png bs=1 skip=$((0x12005)) of=hidden.jpg

$ foremost -i weird.png
```
But, it is recommended that use `foremost` since it will also extract another hidden audio file from the extracted `jpg` file.\
Import that audio file to audacity to view the spectrogram, it shows a sequence of morse code. Decode the morse code to get the flag.

flag: `BITSCTF{snoooooopppppppp}`