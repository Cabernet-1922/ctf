# Pitter, Patter, Platters [Medium] (by syreal) - picoCTF 2020 Mini-Competition
> 'Suspicious' is written all over this disk image. Download <a href='//jupiter.challenges.picoctf.org/static/47f3cb40aed42fbd74fd644e11d08007/suspicious.dd.sda1'>suspicious.dd.sda1</a>

After open the disk image in autospy, there is a file called `suspicious-file.txt-slack`, the reversed flag is inside:
```text
} 6 1 d 9 0 7 e c _ 3 < _ | L m _ 1 1 1 t 5 _ 3 b { F T C o c i p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
```
```bash
echo "} 6 1 d 9 0 7 e c _ 3 < _ | L m _ 1 1 1 t 5 _ 3 b { F T C o c i p" | rev | tr -d ' '
```

flag: `picoCTF{b3_5t111_mL|_<3_ce709d16}`