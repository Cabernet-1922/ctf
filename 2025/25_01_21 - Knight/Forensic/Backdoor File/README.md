Inside alice's folder, we found `/home/alice/Projects/vulnerable`. 
```bash
strings vulnerable | grep -oP "KCTF{.*}"

KCTF{buff3r_0verfl0w_expl0it3d}
```

flag: `KCTF{buff3r_0verfl0w_expl0it3d}`