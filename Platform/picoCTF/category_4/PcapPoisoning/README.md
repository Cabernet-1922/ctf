# PcapPoisoning [Medium] (by Mubarak Mikail) - picoCTF 2023
> <p>How about some hide and seek heh?</p>
<p>Download this <a href='https://artifacts.picoctf.net/c/377/trace.pcap' download>file</a> and find the flag.</p>


```bash
strings trace.pcap | grep -oP "picoCTF{.*}"
```

flag: `picoCTF{P64P_4N4L7S1S_SU55355FUL_31010c46}`