# WPA-ing Out [Medium] (by MistressVampy)
> <p>I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.</p>
<p>Use this '<a href='https://artifacts.picoctf.net/c/41/wpa-ing_out.pcap' download>pcap file</a>' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.</p>

With `aircrack-ng wpa-ing_out.pcap -w rockyou.txt`, we can get the key is `mickeymouse`, wrap it into the flag format.

flag: `picoCTF{mickeymouse}`

reference:
- [Aircrack-ng](https://www.aircrack-ng.org/doku.php?id=aircrack-ng)
