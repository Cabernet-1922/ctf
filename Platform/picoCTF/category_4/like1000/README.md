# like1000 [Medium] (by Danny) - picoCTF 2019
> This <a href='//jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar'>.tar file</a> got tarred a lot.


```python
import os

def unzip_all():
    while 1:
        for i in os.listdir('.'):
            if i.endswith('.tar'):
                os.system(f"binwalk {i}")
                print(i, open("filler.txt", "r").readlines()[0].strip())
                os.system(f"rm {i}")
                break

unzip_all()
```
Note that run the script in linux environment and there is no flag in filler.txt`

Basically you need to unzip until there is no tar file, and it ends up with a `flag.png` file. 


flag: `picoCTF{l0t5_0f_TAR5}`