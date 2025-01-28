# Security Rocks [50 points] (143 solves)
```bash
$ aircrack-ng dump-05.cap -w rockyou.txt

Reading packets, please wait...
Opening dump-05.cap
Read 12522 packets.

   #  BSSID              ESSID                     Encryption

   1  D8:3A:DD:07:AA:5A  securityRocks             WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening dump-05.cap
Read 12522 packets.

1 potential targets

                               Aircrack-ng 1.7

      [00:01:19] 2298608/14344391 keys tested (29315.95 k/s)

      Time left: 6 minutes, 50 seconds                          16.02%

                       KEY FOUND! [ youwontguessit92 ]


      Master Key     : FF 3E DD AB A0 BB C3 90 43 83 1B 53 57 93 8B 91
                       CB 5E DE BB 32 72 1E 51 78 71 DF 67 BA 5A 18 29

      Transient Key  : 3F 6F F4 92 3E FE D7 AC D1 FC 9F E9 A8 EE 49 F3
                       F5 48 99 9D C0 C5 AB 39 0B 9C 4C A4 44 DB D1 55
                       9D 87 DB 2B B2 EF C6 4D 42 02 B9 88 40 73 3C 9D
                       B8 4D FF 7B 93 D7 6C 66 7B 2B 52 3D 7B 76 8B 71

      EAPOL HMAC     : 23 C4 4E 94 C2 27 44 F6 42 46 99 1A FB 6E 94 12
```
From this, we know the SSID is `securityRocks`(it also appears everywhere in the packets) and the password found is `youwontguessit92`. Then, try to decrypt the packets!\
In Wireshark, `Edit`->`Preferences`, expand `Protocols` in the menu, scroll down and select `IEEE 802.11`. Choose `Decryption keys Edit`, key type = `wpa-pwd` and key would be `youwontguessit92:securityRocks`, the traffic will then be decrypted. \
Back to the main page, browse some streams, and may find `secret.txt` exist in TCP stream. So, `File`->`Export Objects`->`FTP` to export `secret.txt`:
```text
Heres my super secret flag, I made it extra secure ;)
1KZTi2ZV7tO6yNxslvQbjRGL54BsPVyskwv4QaR29UMKj
```
Decode from base62.

flag: `TUCTF{w1f1_15_d3f1n173ly_53cure3}`


reference list:
- https://networklessons.com/wireless/wpa-and-wpa2-4-way-handshake
- https://wiki.wireshark.org/HowToDecrypt802.11
- https://hackmd.io/@SBK6401/Skg917MAo