# rail-fence [Medium] (by Will Hong) - picoCTF 2022
> <p>A type of transposition cipher is the rail fence cipher, which is described
<a href="https://en.wikipedia.org/wiki/Rail_fence_cipher">here</a>. Here is one such
cipher encrypted using the rail fence with 4 rails. Can you decrypt it?</p>
<p>Download the message <a href='https://artifacts.picoctf.net/c/190/message.txt' download>here</a>.</p>
<p>Put the decoded message in the picoCTF flag format, <code>picoCTF{decoded_message}</code>.</p>


As the description states, the message is encoded with rail-fence-cipher with 4 rails. 
Throw the ciphertext into cyberchef to auto cook for us:
```text
The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3
```

flag: `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}`