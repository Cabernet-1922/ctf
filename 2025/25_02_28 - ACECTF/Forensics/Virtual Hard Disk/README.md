# Virtual Hard Disk [200 points] (100 solves)
Open the disk image to Autospy, you can see two suspicious file `66c61672e747874.jpg:Flag` and `666c61672e747874.jpg:Key` where gives an encrypted flag and a key respectively:
```text
CTCHHW{7t3_h1hw3p3sq3_s37i33r_a0l_4li_a3}

Key='cryforme'
```
This appears to be `VIGENERE CYPHER`, so just use whatever online decoder to recover the original flag.

flag: `ACECTF{7h3_d1ff3r3nc3_b37w33n_y0u_4nd_m3}`