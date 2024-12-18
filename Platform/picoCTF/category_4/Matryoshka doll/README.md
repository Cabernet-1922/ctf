# Matryoshka doll [Medium] (by Susie/Pandu) - picoCTF 2021
> Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: <a href='//mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg'>this</a>

This challenge is similar to [like1000](../like1000), but we use `binwalk` in this challenge instead of `tar`.
Also, there is no need to write another solve script since `binwalk` has argument `--matryoshka` that recursively scan extracted files:
```bash
binwalk -qerM dolls.jpg
```
Then, we end up with a `flag.txt`: `p i c o C T F { a c 0 0 7 2 c 4 2 3 e e 1 3 b f c 0 b 1 6 6 a f 7 2 e 2 5 b 6 1 }`

flag: `picoCTF{ac0072c423ee13bfc0b166af72e25b61}`
