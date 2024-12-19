# flag_shop [Medium] (by Danny) - picoCTF 2019
> There's a flag shop selling stuff, can you buy a flag? <a href='//jupiter.challenges.picoctf.org/static/253c4651d852ac6342752ff222cf2a83/store.c'>Source</a>. Connect with <code>nc jupiter.challenges.picoctf.org 9745</code>.



Basically enter a number to buy `1. Defintely not the flag Flag` that lead to an overflow since we are dealing with 32-bit integer. Minimum value for 32-int is `-2,147,483,648`, and we have an initial balance of `1100`, so we can do the calculation `|(-2147483648-1100)|/9000≈2386094.16444`. Therefore, we need `2386094+1` as quantity.\
After that, we have enough balance to buy a flag.

flag: `picoCTF{m0n3y_bag5_65d67a74}`