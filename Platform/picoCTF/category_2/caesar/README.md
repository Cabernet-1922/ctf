# caesar [Medium] (by Sanjay C/Daniel Tunitis) - picoCTF 2019
> Decrypt this <a href='//jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext'>message</a>.


Given:
```text
picoCTF{ynkooejcpdanqxeykjrbdofgkq}
```
Using caesar cipher decoder and try different offset. With offset=4, we see the word `crossing` in the message. Therefore, the plaintext when offset=4 is the right one.


flag: `picoCTF{crossingtherubiconvfhsjkou}`