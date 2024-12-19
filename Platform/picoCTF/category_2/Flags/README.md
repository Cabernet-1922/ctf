# Flags [Medium] (by Danny) - picoCTF 2019
> What do the <a href='//jupiter.challenges.picoctf.org/static/fbeb5f9040d62b18878d199cdda2d253/flag.png'>flags</a> mean?

The flags in the image is [International Maritime Signal Flags](https://www.anbg.gov.au/flags/signal-meaning.html), let's decode the flag one by one.

Since the flag format is `picoCTF{.*}`, it follows that some of the flag characters are already known:
```text
picoCTF{F________T_FF}
```
With the maritime signal flags mapping, further get more chars:
```text
picoCTF{F_AG_AND_TUFF}
```
However, three of the mapping attempts is incorrect. After some trial and error, a mapping with similar pattern could complete the decoding.
```text
picoCTF{F1AG5AND5TUFF}
```


flag: `picoCTF{F1AG5AND5TUFF}`