# HideToSee [Medium] (by Sunday Jacob Nwanyim) - picoCTF 2023
> <p>How about some hide and seek heh?</p>
<p>Look at this image <a href='https://artifacts.picoctf.net/c/237/atbash.jpg' download>here</a>.</p>

`steghide extract -sf atbash.jpg` will extract a `cipher.txt` file with content: `krxlXGU{zgyzhs_xizxp_05y2z65z}`, and we use the `atbash cipher` decoder to solve this challenge.

flag: `picoCTF{atbash_crack_05b2a65a}`