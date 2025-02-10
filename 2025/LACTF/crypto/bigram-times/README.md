# bigram-times [291 points] (187 solves)
```python
import itertools

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}~_"
flag = ""
shifted_flag = "jlT84CKOAhxvdrPQWlWT6cEVD78z5QREBINSsU50FMhv662W"

not_the_flag = "mCtRNrPw_Ay9mytTR7ZpLJtrflqLS0BLpthi~2LgUY9cii7w"
also_not_the_flag = "PKRcu0l}D823P2R8c~H9DMc{NmxDF{hD3cB~i1Db}kpR77iU"


def bigram_multiplicative_shift(bigram):
    assert (len(bigram) == 2)
    pos1 = characters.find(bigram[0]) + 1
    pos2 = characters.find(bigram[1]) + 1
    shift = (pos1 * pos2) % 67
    return characters[((pos1 * shift) % 67) - 1] + characters[((pos2 * shift) % 67) - 1]


for i in range(0, len(shifted_flag), 2):
    combinations = itertools.product(characters, repeat=2)
    for combo in combinations:
        payload = ''.join(combo)
        temp = bigram_multiplicative_shift(payload)
        if temp == shifted_flag[i:i + 2]:
            if payload != not_the_flag[i:i + 2] and payload != also_not_the_flag[i:i + 2]:
                flag += payload
                print(flag)
                break
```

flag: `lactf{mULT1pl1cAtiV3_6R0uPz_4rE_9RE77y_5we3t~~~}`