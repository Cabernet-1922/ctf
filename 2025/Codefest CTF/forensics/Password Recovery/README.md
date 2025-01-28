# Password Recovery [100 points] (57 solves)
Since the password was generated on Republic Day of India 2019, the timestamp for `2019-01-26 00:00:00` is `1548432000`, so it is possible to have all the possible password generated in that day:
```python
import os 
import time
from pwn import *

start_time = 1548432000

context.log_level = "CRITICAL"
with open("wordlist.txt","w") as f:
    for i in range(86400):
        start_time += 1
        os.system(f"sudo date --set=@{start_time}>/dev/null 2>&1")
        p = process("./passgen")
        passphrase = p.recvline_contains(b"HERE IS YOUR SECURELY GENERATED PASSWORD: ").decode().strip()[-15:]
        p.close()
        f.writelines(passphrase+"\n")

f.close()
```
Then, with wordlist and [password attack script](https://raw.githubusercontent.com/PythonPhreak/dictionary-attack.py/refs/heads/main/dictionary-attack-zip.py) will be able to get the password, which is `kFEbD1Pzxyu69Yw`.

flag: `CodefestCTF{rand_15_n07_4c7ua11y_r4nd0m}`