# shark on wire 1 [Medium] (by Danny) - picoCTF 2019
> We found this <a href='//jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap'>packet capture</a>. Recover the flag.

Right-click a random UDP protocol packet and select follow UDP stream, then in the interactive page select stream 6. 
Alternatively: 
```bash
tshark -r capture.pcap -Y "udp.stream eq 6" -T fields -e data | xxd -r -p
```

flag: `picoCTF{StaT31355_636f6e6e}`