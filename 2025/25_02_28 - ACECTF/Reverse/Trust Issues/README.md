# Trust Issues [200 points] (145 solves)
```python
target = "GRX14YcKLzXOlW5iaSlBIrN7"
xor_key = [0x06, 0x11, 0x1d, 0x72, 0x60, 0x1f, 0x18, 0x7c, 0x3e, 0x0f] + [ord(c) for c in 'mx35@^>%_0x'] + [0x14, 0x37, 0x4a]
print(''.join(chr(ord(t) ^ k) for t, k in zip(target, xor_key)))
```

flag: `ACECTF{7ru57_bu7_v3r1fy}`