# Wireshark doo dooo do doo... [Medium] (by Dylan) - picoCTF 2021
> Can you find the flag? <a href='//mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng'>shark1.pcapng</a>.

```bash
strings shark1.pcapng | grep -oP "[a-zA-Z]+{.*}
```
And we get `cvpbPGS{c33xno00_1_f33_h_qrnqorrs}`, and decode it with rot13.

flag: `picoCTF{p33kab00_1_s33_u_deadbeef}`