# A Little Extra Knowledge Is Too Dangerous [200 points] (83 solves)
```python
enc_ = "QUNFQ1RGe/MV82dTM1NV95MHVfN3J1bmM0N/zNkXzdoM18zeDdyNF9rbjB3bDN/kNjNfcjRkMG1fNTdyMW42NjY2NjY2NjY2NjU1NTU1NTU1NV/94eHh4eHh4YmJieHh4eHh4Y2N/jY3h9"

import base64

flag = base64.b64decode("".join(enc_.split("/")[1:]))
print(flag)
```

flag: `ACECTF{1_6u355_y0u_7runc473d_7h3_3x7r4_kn0wl3d63_r4d0m_57r1n66666666666555555555_xxxxxxxbbbxxxxxxccccx}`
