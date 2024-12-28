# shark on wire 2 [Medium] (by Danny) - picoCTF 2019
> We found this <a href='//jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap'>packet capture</a>. Recover the flag that was pilfered from the network.

With the filter `ip.addr == 10.0.0.66` or `udp.port == 22`, and look at the info of these packets:
```text
5000 → 22 Len=5
5112 → 22 Len=5
5105 → 22 Len=5
5099 → 22 Len=5
5111 → 22 Len=5
5067 → 22 Len=5
5084 → 22 Len=5
5070 → 22 Len=5
5123 → 22 Len=5
5112 → 22 Len=5
5049 → 22 Len=5
5076 → 22 Len=5
5076 → 22 Len=5
5102 → 22 Len=5
5051 → 22 Len=5
5114 → 22 Len=5
5051 → 22 Len=5
5100 → 22 Len=5
5095 → 22 Len=5
5100 → 22 Len=5
5097 → 22 Len=5
5116 → 22 Len=5
5097 → 22 Len=5
5095 → 22 Len=5
5118 → 22 Len=5
5049 → 22 Len=5
5097 → 22 Len=5
5095 → 22 Len=5
5115 → 22 Len=5
5116 → 22 Len=5
5051 → 22 Len=5
5103 → 22 Len=5
5048 → 22 Len=5
5125 → 22 Len=5
5000 → 22 Len=3
```
`112, 105, 099 ..` are ascii numbers, which means we can yield the flag from these packet infos. To further process the data:
```bash
tshark -r capture.pcap -Y "ip.addr == 10.0.0.66" -T fields -e "_ws.col.Info" | awk '{print $1}' | awk '{printf "%c", $1-5000}'
```

flag: `picoCTF{p1LLf3r3d_data_v1a_st3g0}`