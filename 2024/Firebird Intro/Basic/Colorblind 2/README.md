# Colorblind 2 [225 points] (6 solves)
```txt
⡏⣭⡍⡇⣑⢴⠪⣌⢠⡅⠜⡹⠅⡏⣭⡍⡇⠧⠭⠥⠇⠔⣗⣝⢜⡜⠎⢝⠅⡄⠧⠭⠥⠇⡂⣳⠉⢕⠩⠉⣽⢝⡽⡷⢔⣎⢯⠆⠼⢰⠇⣼⠮⢃⢅⣳⣹⠪⠯⡆⣽⢡⡋⠿⡳⠑⠶⠇⠔⡬⡳⠵⢣⡚⠨⡖⠊⣵⣮⠁⢸⡱⡔⠿⠄⢔⠻⡀⢕⡛⠏⠺⠤⠇⠕⠇⠊⠃⠊⠗⠙⠀⡥⠤⠭⡍⣂⡪⣶⣀⣨⡤⠭⠠⡏⠍⡯⠪⡆⡇⠿⠇⡇⢍⠢⣢⠵⣃⡦⠥⢔⡯⢩⠇⢊⠄⠉⠉⠉⠁⠀⠉⠁⠉⠀⠉⠀⠈⠉⠉⠉⠉⠁
```
Look closely the given braille dot group.\
Seven Braille characters in a group, stack each group on top of the other, and you get a QR-code-like image below.
```txt
⡏⣭⡍⡇⣑⢴⠪⣌⢠⡅⠜⡹⠅⡏⣭⡍⡇
⠧⠭⠥⠇⠔⣗⣝⢜⡜⠎⢝⠅⡄⠧⠭⠥⠇
⡂⣳⠉⢕⠩⠉⣽⢝⡽⡷⢔⣎⢯⠆⠼⢰⠇
⣼⠮⢃⢅⣳⣹⠪⠯⡆⣽⢡⡋⠿⡳⠑⠶⠇
⠔⡬⡳⠵⢣⡚⠨⡖⠊⣵⣮⠁⢸⡱⡔⠿⠄
⢔⠻⡀⢕⡛⠏⠺⠤⠇⠕⠇⠊⠃⠊⠗⠙⠀
⡥⠤⠭⡍⣂⡪⣶⣀⣨⡤⠭⠠⡏⠍⡯⠪⡆
⡇⠿⠇⡇⢍⠢⣢⠵⣃⡦⠥⢔⡯⢩⠇⢊⠄
⠉⠉⠉⠁⠀⠉⠁⠉⠀⠉⠀⠈⠉⠉⠉⠉⠁
```
Use some tools like [qrazybox](https://merri.cx/qrazybox/) to draw the QR-code. Alternatively: 
```python
import cv2
import numpy as np

braille_pattern = [
    "⡏⣭⡍⡇⣑⢴⠪⣌⢠⡅⠜⡹⠅⡏⣭⡍⡇",
    "⠧⠭⠥⠇⠔⣗⣝⢜⡜⠎⢝⠅⡄⠧⠭⠥⠇",
    "⡂⣳⠉⢕⠩⠉⣽⢝⡽⡷⢔⣎⢯⠆⠼⢰⠇",
    "⣼⠮⢃⢅⣳⣹⠪⠯⡆⣽⢡⡋⠿⡳⠑⠶⠇",
    "⠔⡬⡳⠵⢣⡚⠨⡖⠊⣵⣮⠁⢸⡱⡔⠿⠄",
    "⢔⠻⡀⢕⡛⠏⠺⠤⠇⠕⠇⠊⠃⠊⠗⠙⠀",
    "⡥⠤⠭⡍⣂⡪⣶⣀⣨⡤⠭⠠⡏⠍⡯⠪⡆",
    "⡇⠿⠇⡇⢍⠢⣢⠵⣃⡦⠥⢔⡯⢩⠇⢊⠄",
    "⠉⠉⠉⠁⠀⠉⠁⠉⠀⠉⠀⠈⠉⠉⠉⠉⠁"
]


def get_dot_positions(char):
    code = ord(char) - 0x2800
    dots = []

    dot_map = [
        (0, 0),
        (1, 0),
        (2, 0),
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 0),
        (3, 1),
    ]

    for i in range(8):
        if code & (1 << i):
            dots.append(dot_map[i])
    return dots


def merge():
    res = np.full((33, 33, 3), 255, dtype=np.uint8)
    for row in range(len(braille_pattern)):
        for column in range(len(braille_pattern[row])):
            dot_map = get_dot_positions(braille_pattern[row][column])
            for j in range(len(dot_map)):
                res[row * 4 + dot_map[j][0]][column * 2 + dot_map[j][1]] = 0
    return res


cv2.imwrite('qrcode.png', merge())
```
Then, you will get a pastebin site, and a password is needed. Try to translate the original braille dot, the password follows the substring "pw-" and is all in lowercase.