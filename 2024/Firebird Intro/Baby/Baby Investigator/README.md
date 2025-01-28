# Baby Investigator [100 points] (51 solves)
flag hide in one of `.xml` file.
```python
import os,re
os.chdir("q14")
for i in os.listdir():
    with open(i,"r",encoding='utf-8',errors="ignore") as f:
        text = str(f.readlines())
        if "flag{" in text:
            print(re.findall(r"flag\{.*\}",text)[0])
```