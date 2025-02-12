Input `D2C22A62DEA62CCE9EFA0ECC86CE9AFA4ECC6EFAC6162C3636CC76E6A6BE`to transformation function:
```c
uint64_t do_fight(uint8_t arg1) {
    uint8_t var_1c = arg1;
    char var_d = 0;
    
    for (int32_t i = 0; i <= 7; i++) {
        var_d = ((var_d << 1) | (var_1c & 1));
        var_1c >>= 1;
    }
    
    return var_d;
}
```

Then,
```python
def reverse_bits(b):
    return int('{:08b}'.format(b)[::-1], 2)

target = "D2C22A62DEA62CCE9EFA0ECC86CE9AFA4ECC6EFAC6162C3636CC76E6A6BE"
hex_pairs = [target[i:i+2] for i in range(0, len(target), 2)]
bytes_arr = [int(x, 16) for x in hex_pairs]
result = ""
for b in bytes_arr:
    result += chr(reverse_bits(b))
print(result)
```

flag: `KCTF{e4sy_p3asY_r3v_ch4ll3nge}`