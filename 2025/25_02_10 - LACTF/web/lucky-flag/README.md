# lucky-flag [136 points] (664 solves)
```python
import re

source_code = """let enc = `"\\u000e\\u0003\\u0001\\u0016\\u0004\\u0019\\u0015V\\u0011=\\u000bU=\\u000e\\u0017\\u0001\\t=R\\u0010=\\u0011\\t\\u000bSS\\u001f"`"""
encoded_flag_match = re.search(r'let enc = `([^`]+)`', source_code)
encoded_flag = encoded_flag_match.group(1)
decoded_flag = [ord(char) ^ 0x62 for char in eval(encoded_flag)]
flag = ''.join(chr(char) for char in decoded_flag)
print(flag)
```

flag: `lactf{w4s_i7_luck_0r_ski11}`