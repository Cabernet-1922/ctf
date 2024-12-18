# Packets Primer [Medium] (by LT 'syreal' Jones) - picoCTF 2022
> <p>Download the packet capture file and use packet analysis software to find the
flag.</p>
<ul>
<li><a href='https://artifacts.picoctf.net/c/194/network-dump.flag.pcap' download>Download packet capture</a></li>
</ul>


```bash
strings network-dump.flag.pcap | tr -d ' ' | grep -oP "picoCTF{.*}"
```

flag: `picoCTF{p4ck37_5h4rk_ceccaa7f}`