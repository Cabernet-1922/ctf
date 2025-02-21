# Tick Tock [499 points] (13 solves)
As the image implies, extract LSB of 1 and 5 bits for all three colour, then replace `tick` to `0` and `tock` to `1`. Convert the result binary to ascii character and do caesar shift with offsets 11.
```python
a = """ticktocktocktock
ticktickticktock
 ticktocktocktic
kticktocktocktoc
k ticktocktockti
ckticktocktickti
ck ticktocktockt
icktickticktockt
ock ticktocktock
tocktickticktock
tick ticktocktoc
ktickticktocktic
ktick ticktockto
cktocktocktickto
cktock ticktockt
ocktockticktockt
icktock ticktock
tocktocktocktick
ticktick ticktoc
ktockticktocktic
ktocktock tickto
cktocktocktickto
ckticktick tickt
ockticktocktockt
ocktocktock tick
tocktockticktick
ticktocktick tic
ktocktocktocktoc
ktickticktick ti
cktocktocktickti
ckticktocktock t
icktocktocktickt
ockticktocktick 
ticktocktocktick
tocktickticktock
 ticktocktocktoc
kticktockticktic
k ticktocktockti
cktockticktickti
ck ticktocktickt
ocktocktocktockt
ock ticktocktock
ticktockticktock
tick ticktocktoc
kticktickticktoc
ktock ticktockto
ckticktocktickti
cktock ticktockt
ocktocktocktickt
icktick ticktock
tocktickticktick
ticktock ticktoc
kticktocktocktoc
ktocktock tickto
cktockticktickti
cktocktick tickt
ocktocktocktockt
ickticktick tick
tocktocktocktick
ticktocktock tic
ktocktockticktic
kticktocktock ti
cktocktocktockto
cktickticktick t
icktocktocktockt
icktocktocktick 
ticktocktocktock
ticktocktocktock
 ticktocktocktic
ktocktickticktoc
k ticktocktockto
cktocktocktickto
ck"""

import re

def shift(c, n): return chr((ord(c) - 97 + n) % 26 + 97)

k = "".join(a.splitlines()).replace('tick', '0').replace('tock', '1')
flag = ''.join([chr(int(i, 2)) if not chr(int(i, 2)).isalnum() else shift(chr(int(i, 2)), 11) for i in k.split(" ")])

print(flag)
```

flag: `bronco{five_minutes_until_midnight}`