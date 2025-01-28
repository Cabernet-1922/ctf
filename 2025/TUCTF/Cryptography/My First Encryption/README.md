# My First Encryption [50 points] (263 solves)
The challenge given a corrupted `.jpg` file, check its header to know what's wrong:
```bash
$ xxd flag.jpeg | head

cfe8 cfd0 3020 7a76 7976 3031 3131 3048
```
As we know, the correct `jpg` header should be `FF D8 FF E0`. Since the description of the challenge suggest `xor`, try to xor two header and you may get `0x30`. This means the whole image was xored with key `0x30`, now xor back to original image:
```python
input_file = "flag.jpeg"
output_file = "recovered_file.jpeg"
xor_key = 0x30  

with open(input_file, "rb") as f:
    corrupted_data = f.read()

recovered_data = bytearray([byte ^ xor_key for byte in corrupted_data])

with open(output_file, "wb") as f:
    f.write(recovered_data)
```
flag: `TUCTF{kn0wn_pl@1nt3xt_15_dang3r0us}`