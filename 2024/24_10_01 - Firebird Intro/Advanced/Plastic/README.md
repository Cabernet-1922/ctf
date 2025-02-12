# Plastic [350 points] (5 solves)
`pngcheck -v broken_plastic.png` shows that there are invalid image dimensions:
```txt
File: broken_plastic.png (16482 bytes)
  chunk IHDR at offset 0x0000c, length 13:  invalid image dimensions (3735929054x4277000826)
ERRORS DETECTED in broken_plastic.png
```
Then, we might need tools like [Corrupted PNG Dimensions Bruteforcer](https://github.com/cjharris18/png-dimensions-bruteforcer) to fix the corrupted png for us.
`./png_dimensions_bruteforce.py -f broken_plastic.png` will get us a fixed png, put it into [Aperi'Solve](https://www.aperisolve.com/), you will then clearly see the flag.
