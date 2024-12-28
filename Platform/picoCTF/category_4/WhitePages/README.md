# WhitePages [Medium] (by John Hammond) - picoCTF 2019
> I stopped using YellowPages and moved onto WhitePages... but <a href='//jupiter.challenges.picoctf.org/static/95be9526e162185c741259a75dffa0ab/whitepages.txt'>the page they gave me</a> is all blank!

```bash
xxd -p | tr -d '\n' | sed 's/e28083/0/g' | sed 's/20/1/g' | perl -lpe '$_=pack("B*",$_)'
```
```text
picoCTF
SEE PUBLIC RECORDS & BACKGROUND REPORT
5000 Forbes Ave, Pittsburgh, PA 15213
picoCTF{not_all_spaces_are_created_equal_7100860b0fa779a5bd8ce29f24f586dc}
```
flag: `picoCTF{not_all_spaces_are_created_equal_7100860b0fa779a5bd8ce29f24f586dc}`