# Disk, disk, sleuth! [Medium] (by syreal) - picoCTF 2021
> Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: <a href='//mercury.picoctf.net/static/ac394d24f88e51a09cc909687cf6d853/dds1-alpine.flag.img.gz'>dds1-alpine.flag.img.gz</a>


```bash
strings dds1-alpine.flag.img | grep -oP "picoCTF{.*}"
```

flag: `picoCTF{f0r3ns1c4t0r_n30phyt3_dcbf5942}`