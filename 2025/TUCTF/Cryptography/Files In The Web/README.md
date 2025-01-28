# Files In The Web [50 points] (127 solves)
Two special event in the event log: `ID=659,1000`:
```text
659: File nzsodanrot.txt encrypted with key
1000: Command run: .\tornado.py --key UIYfpIrqvzvTedjR1qFm66K1MYYlwNgUQlgpZPfLs3k=
```
In the `nzsodanrot.txt`:
```text
gAAAAABnSr5MS-gH-RLqtV1ltw_hBuwujvt6S-Ku3pOdgSpAiby55EGOI3JMpv3JX6ptlhnC8cT4UdfqiIck6RDgobhASUKPJlZMkV0Js82Xx-kIHKywirHeGBqKQimJ672sPnbeWL1e
```
This prefix `gAAAAA` implies this is fernet encryption. For the reason why it always starts with `gAAAAA`, you may refer to [this](https://stackoverflow.com/questions/28775567/why-does-a-fernet-encryption-token-always-start-with-the-same-sequence-python).\
Therefore, decrypt it to get the flag:
```python
from cryptography.fernet import Fernet

key = "UIYfpIrqvzvTedjR1qFm66K1MYYlwNgUQlgpZPfLs3k="
encrypted_data = "gAAAAABnSr5MS-gH-RLqtV1ltw_hBuwujvt6S-Ku3pOdgSpAiby55EGOI3JMpv3JX6ptlhnC8cT4UdfqiIck6RDgobhASUKPJlZMkV0Js82Xx-kIHKywirHeGBqKQimJ672sPnbeWL1e"

f = Fernet(key)
decrypted_data = f.decrypt(encrypted_data.encode())
print(decrypted_data.decode())
```
flag: `TUCTF{1T$__t0rn@d0$zn__nz$0d@nr0t__$T1}`