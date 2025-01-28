# Packet Detective [50 points] (350 solves)
In wireshark, follow the last tcp stream you can see the flag. Alternatively: 
```bash
tshark -r traffic_analysis.pcap -q -z "follow,tcp,ascii,99"
```
flag: `TUCTF{N3tw0rk_M4st3r}`