# Easy1 [Medium] (by Alex Fulton/Danny) - picoCTF 2019
> The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help <code>UFJKXQZQUNB</code> with the key of <code>SOLVECRYPTO</code>. Can you use this <a href='//jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt'>table</a> to solve it?. 

The provided table is Vigenère cipher table, therefore, we can use [online tool](https://www.cs.du.edu/~snarayan/crypt/vigenere.html) to decrypt the message.

flag: `picoCTF{cryptoisfun}`