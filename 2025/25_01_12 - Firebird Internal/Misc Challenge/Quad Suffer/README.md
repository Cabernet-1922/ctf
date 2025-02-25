# Quad Suffer [1000 points] (1 solves) (post-match solve)
Given a secret y value `db95c7eb0b7a29f10a0f9689fa00aeaf` which looks like a hash value, apply [preimage attack](https://en.wikipedia.org/wiki/Preimage_attack) here to get the input from hash:
```python
import hashlib
import string
import itertools

def try_preimage(target_hash):
    chars = string.ascii_letters + string.digits + string.punctuation
    for length_ in range(5): # Could be other length, but extra time is needed for longer length
        for i in range(1, length_ + 1):
            for suffix in itertools.product(chars, repeat=i):
                test_str = ''.join(suffix)
                test_hash = hashlib.md5(test_str.encode()).hexdigest()
                if test_hash == target_hash:
                    return test_str
    return None

target = "db95c7eb0b7a29f10a0f9689fa00aeaf"
result = try_preimage(target)
print(result)
# output x+94
```
As mentioned, that hash is y value, so the value of y will be $x+94$.\
Substitute $y=x+94$ to all the equations and solve the equation by quadratic equation:
```
[[7, 77], [0, 30], [9, 10], [6, 112], [9, 107], [9, 108], [2, 25], [9, 20], [6, 144], [2, 7], [3, 73], [3, 93], [9, 81], [1, 3], [8, 123], [2, 124], [2, 17], [4, 55], [3, 32], [4, 14], [1, 127], [6, 66], [0, 62], [5, 29], [2, 49], [8, 46], [9, 143], [0, 5], [5, 133], [6, 137], [8, 120], [3, 101], [1, 35], [9, 64], [7, 18], [0, 26], [3, 117], [3, 86], [9, 85], [9, 91], [7, 104], [6, 11], [9, 34], [8, 16], [7, 60], [6, 94], [0, 45], [6, 80], [0, 142], [2, 76], [8, 145], [3, 40], [0, 51], [0, 82], [5, 126], [7, 58], [8, 89], [3, 67], [8, 24], [2, 50], [4, 118], [0, 97], [0, 90], [9, 134], [2, 116], [4, 37], [5, 48], [8, 65], [7, 99], [5, 19], [4, 125], [9, 119], [1, 128], [6, 68], [8, 75], [1, 71], [1, 2], [1, 102], [3, 15], [7, 100], [0, 38], [0, 131], [0, 110], [6, 22], [4, 33], [8, 130], [7, 95], [2, 59], [3, 9], [6, 129], [2, 92], [9, 98], [2, 115], [0, 54], [9, 47], [0, 28], [7, 74], [4, 6], [1, 84], [0, 88], [5, 42], [1, 43], [0, 56], [7, 83], [2, 136], [4, 23], [7, 39], [0, 8], [2, 139], [0, 63], [5, 57], [0, 113], [9, 146], [1, 36], [4, 13], [8, 79], [0, 140], [4, 7], [6, 44], [3, 12], [0, 87], [8, 69], [4, 132], [6, 114], [4, 141], [6, 138], [6, 70], [3, 135], [1, 61], [5, 106], [5, 103], [9, 27], [5, 31], [3, 147], [9, 21], [2, 72], [4, 78], [4, 52], [1, 121], [6, 109], [6, 41], [5, 122], [6, 96], [4, 111], [1, 105], [5, 9], [3, 53]]
```
Sort the roots in ascending order by the second roots of each pair of equations:
```
[[1, 2], [1, 3], [0, 5], [4, 6], [2, 7], [4, 7], [0, 8], [3, 9], [5, 9], [9, 10], [6, 11], [3, 12], [4, 13], [4, 14], [3, 15], [8, 16], [2, 17], [7, 18], [5, 19], [9, 20], [9, 21], [6, 22], [4, 23], [8, 24], [2, 25], [0, 26], [9, 27], [0, 28], [5, 29], [0, 30], [5, 31], [3, 32], [4, 33], [9, 34], [1, 35], [1, 36], [4, 37], [0, 38], [7, 39], [3, 40], [6, 41], [5, 42], [1, 43], [6, 44], [0, 45], [8, 46], [9, 47], [5, 48], [2, 49], [2, 50], [0, 51], [4, 52], [3, 53], [0, 54], [4, 55], [0, 56], [5, 57], [7, 58], [2, 59], [7, 60], [1, 61], [0, 62], [0, 63], [9, 64], [8, 65], [6, 66], [3, 67], [6, 68], [8, 69], [6, 70], [1, 71], [2, 72], [3, 73], [7, 74], [8, 75], [2, 76], [7, 77], [4, 78], [8, 79], [6, 80], [9, 81], [0, 82], [7, 83], [1, 84], [9, 85], [3, 86], [0, 87], [0, 88], [8, 89], [0, 90], [9, 91], [2, 92], [3, 93], [6, 94], [7, 95], [6, 96], [0, 97], [9, 98], [7, 99], [7, 100], [3, 101], [1, 102], [5, 103], [7, 104], [1, 105], [5, 106], [9, 107], [9, 108], [6, 109], [0, 110], [4, 111], [6, 112], [0, 113], [6, 114], [2, 115], [2, 116], [3, 117], [4, 118], [9, 119], [8, 120], [1, 121], [5, 122], [8, 123], [2, 124], [4, 125], [5, 126], [1, 127], [1, 128], [6, 129], [8, 130], [0, 131], [4, 132], [5, 133], [9, 134], [3, 135], [2, 136], [6, 137], [6, 138], [2, 139], [0, 140], [4, 141], [0, 142], [9, 143], [6, 144], [8, 145], [9, 146], [3, 147]]
```
You may notice that first few pairs of roots do not start from `1,2,3...` but `2,3,5...` instead, and missing some number makes the sequence has repetitive order. Therefore, reverse some of the pair is needed (worship my boss Atopos for pointing out this🛐🛐):
```
[[3, 1], [1, 2], [9, 3], [7, 4], [0, 5], [4, 6], [2, 7], [0, 8], [5, 9], [9, 10], [6, 11], [3, 12], [4, 13], [4, 14], [3, 15], [8, 16], [2, 17], [7, 18], [5, 19], [9, 20], [9, 21], [6, 22], [4, 23], [8, 24], [2, 25], [0, 26], [9, 27], [0, 28], [5, 29], [0, 30], [5, 31], [3, 32], [4, 33], [9, 34], [1, 35], [1, 36], [4, 37], [0, 38], [7, 39], [3, 40], [6, 41], [5, 42], [1, 43], [6, 44], [0, 45], [8, 46], [9, 47], [5, 48], [2, 49], [2, 50], [0, 51], [4, 52], [3, 53], [0, 54], [4, 55], [0, 56], [5, 57], [7, 58], [2, 59], [7, 60], [1, 61], [0, 62], [0, 63], [9, 64], [8, 65], [6, 66], [3, 67], [6, 68], [8, 69], [6, 70], [1, 71], [2, 72], [3, 73], [7, 74], [8, 75], [2, 76], [7, 77], [4, 78], [8, 79], [6, 80], [9, 81], [0, 82], [7, 83], [1, 84], [9, 85], [3, 86], [0, 87], [0, 88], [8, 89], [0, 90], [9, 91], [2, 92], [3, 93], [6, 94], [7, 95], [6, 96], [0, 97], [9, 98], [7, 99], [7, 100], [3, 101], [1, 102], [5, 103], [7, 104], [1, 105], [5, 106], [9, 107], [9, 108], [6, 109], [0, 110], [4, 111], [6, 112], [0, 113], [6, 114], [2, 115], [2, 116], [3, 117], [4, 118], [9, 119], [8, 120], [1, 121], [5, 122], [8, 123], [2, 124], [4, 125], [5, 126], [1, 127], [1, 128], [6, 129], [8, 130], [0, 131], [4, 132], [5, 133], [9, 134], [3, 135], [2, 136], [6, 137], [6, 138], [2, 139], [0, 140], [4, 141], [0, 142], [9, 143], [6, 144], [8, 145], [9, 146], [3, 147]]
```
This makes there is no repetitive order in 147 pair of roots, and we can form a decimal number by using the first root of each pair and with `long_to_bytes` to get the flag.
```python
equations = """y = x^2 - 83x + 633
y = x^2 - 29x + 94
y = x^2 - 18x + 184
y = x^2 - 117x + 766
y = x^2 - 115x + 1057
y = x^2 - 116x + 1066
y = x^2 - 26x + 144
y = x^2 - 28x + 274
y = x^2 - 149x + 958
y = x^2 - 8x + 108
y = x^2 - 75x + 313
y = x^2 - 95x + 373
y = x^2 - 89x + 823
y = x^2 - 3x + 97
y = x^2 - 130x + 1078
y = x^2 - 125x + 342
y = x^2 - 18x + 128
y = x^2 - 58x + 314
y = x^2 - 34x + 190
y = x^2 - 17x + 150
y = x^2 - 127x + 221
y = x^2 - 71x + 490
y = x^2 - 61x + 94
y = x^2 - 33x + 239
y = x^2 - 50x + 192
y = x^2 - 53x + 462
y = x^2 - 151x + 1381
y = x^2 - 4x + 94
y = x^2 - 137x + 759
y = x^2 - 142x + 916
y = x^2 - 127x + 1054
y = x^2 - 103x + 397
y = x^2 - 35x + 129
y = x^2 - 72x + 670
y = x^2 - 24x + 220
y = x^2 - 25x + 94
y = x^2 - 119x + 445
y = x^2 - 88x + 352
y = x^2 - 93x + 859
y = x^2 - 99x + 913
y = x^2 - 110x + 822
y = x^2 - 16x + 160
y = x^2 - 42x + 400
y = x^2 - 23x + 222
y = x^2 - 66x + 514
y = x^2 - 99x + 658
y = x^2 - 44x + 94
y = x^2 - 85x + 574
y = x^2 - 141x + 94
y = x^2 - 77x + 246
y = x^2 - 152x + 1254
y = x^2 - 42x + 214
y = x^2 - 50x + 94
y = x^2 - 81x + 94
y = x^2 - 130x + 724
y = x^2 - 64x + 500
y = x^2 - 96x + 806
y = x^2 - 69x + 295
y = x^2 - 31x + 286
y = x^2 - 51x + 194
y = x^2 - 121x + 566
y = x^2 - 96x + 94
y = x^2 - 89x + 94
y = x^2 - 142x + 1300
y = x^2 - 117x + 326
y = x^2 - 40x + 242
y = x^2 - 52x + 334
y = x^2 - 72x + 614
y = x^2 - 105x + 787
y = x^2 - 23x + 189
y = x^2 - 128x + 594
y = x^2 - 127x + 1165
y = x^2 - 128x + 222
y = x^2 - 73x + 502
y = x^2 - 82x + 694
y = x^2 - 71x + 165
y = x^2 - 2x + 96
y = x^2 - 102x + 196
y = x^2 - 17x + 139
y = x^2 - 106x + 794
y = x^2 - 37x + 94
y = x^2 - 130x + 94
y = x^2 - 109x + 94
y = x^2 - 27x + 226
y = x^2 - 36x + 226
y = x^2 - 137x + 1134
y = x^2 - 101x + 759
y = x^2 - 60x + 212
y = x^2 - 11x + 121
y = x^2 - 134x + 868
y = x^2 - 93x + 278
y = x^2 - 106x + 976
y = x^2 - 116x + 324
y = x^2 - 53x + 94
y = x^2 - 55x + 517
y = x^2 - 27x + 94
y = x^2 - 80x + 612
y = x^2 - 9x + 118
y = x^2 - 84x + 178
y = x^2 - 87x + 94
y = x^2 - 46x + 304
y = x^2 - 43x + 137
y = x^2 - 55x + 94
y = x^2 - 89x + 675
y = x^2 - 137x + 366
y = x^2 - 26x + 186
y = x^2 - 45x + 367
y = x^2 - 7x + 94
y = x^2 - 140x + 372
y = x^2 - 62x + 94
y = x^2 - 61x + 379
y = x^2 - 112x + 94
y = x^2 - 154x + 1408
y = x^2 - 36x + 130
y = x^2 - 16x + 146
y = x^2 - 86x + 726
y = x^2 - 139x + 94
y = x^2 - 10x + 122
y = x^2 - 49x + 358
y = x^2 - 14x + 130
y = x^2 - 86x + 94
y = x^2 - 76x + 646
y = x^2 - 135x + 622
y = x^2 - 119x + 778
y = x^2 - 144x + 658
y = x^2 - 143x + 922
y = x^2 - 75x + 514
y = x^2 - 137x + 499
y = x^2 - 61x + 155
y = x^2 - 110x + 624
y = x^2 - 107x + 609
y = x^2 - 35x + 337
y = x^2 - 35x + 249
y = x^2 - 149x + 535
y = x^2 - 29x + 283
y = x^2 - 73x + 238
y = x^2 - 81x + 406
y = x^2 - 55x + 302
y = x^2 - 121x + 215
y = x^2 - 114x + 748
y = x^2 - 46x + 340
y = x^2 - 126x + 704
y = x^2 - 101x + 670
y = x^2 - 114x + 538
y = x^2 - 105x + 199
y = x^2 - 13x + 139
y = x^2 - 55x + 253"""

import re
import math
from Crypto.Util.number import long_to_bytes

root = []
for i in equations.splitlines():
    e_num = re.findall(r"\d*", i)
    b = -int(e_num[10]) - 1
    c = int(e_num[15]) - 94
    if (b ** 2 - 4 * c) >= 0:
        x_1 = int((-b - math.sqrt(b ** 2 - 4 * c)) / 2)
        x_2 = int((-b + math.sqrt(b ** 2 - 4 * c)) / 2)
        root.append([x_1, x_2])

root = sorted(root, key=lambda x: x[1])
root[0:9] = [[3, 1], [1, 2], [9, 3], [7, 4], [0, 5], [4, 6], [2, 7], [0, 8], [5, 9]]
flag = int("".join([str(i[0]) for i in root]))

print(long_to_bytes(flag).decode())
```