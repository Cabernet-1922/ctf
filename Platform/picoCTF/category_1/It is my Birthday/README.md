# It is my Birthday [Medium] (by madStacks) - picoCTF 2021
> I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. <a href="http://mercury.picoctf.net:20277/">http://mercury.picoctf.net:20277/</a>


It's a challenge about hash collision, we just need to find [two pdf file](https://github.com/corkami/collisions/blob/master/examples/free/README.md) with same md5 hash.
After the file is uploaded, we can see the source code of the `.php` file, and the flag is commented in the source code.

flag: `picoCTF{c0ngr4ts_u_r_1nv1t3d_da36cc1b}`