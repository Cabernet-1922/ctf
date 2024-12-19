# credstuff [Medium] (by Will Hong / LT 'syreal' Jones) - picoCTF 2022
> <p>We found a leak of a blackmarket website's login credentials. Can you find the
password of the user <code>cultiris</code> and successfully decrypt it?</p>
<p>Download the leak <a href='https://artifacts.picoctf.net/c/151/leak.tar' download>here</a>.</p>
<p>The first user in <code>usernames.txt</code> corresponds to the first password in
<code>passwords.txt</code>. The second user corresponds to the second password, and so on.</p>


The username `cultiris` is in line 378, the corresponding password is `cvpbPGS{P7e1S_54I35_71Z3}`. Decode it by using rot13.

flag: `picoCTF{C7r1F_54V35_71M3}`