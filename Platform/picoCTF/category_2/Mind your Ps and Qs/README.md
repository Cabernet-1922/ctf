# Mind your Ps and Qs [Medium] (by Sara) - picoCTF 2021
> In RSA, a small <code>e</code> value can be problematic, but what about <code>N</code>? Can you decrypt this? <a href='//mercury.picoctf.net/static/2604f8b51a5cc62d38a3736938f19cef/values'>values</a>


```text
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537
```
With online RSA decoder, `c` is the ciphertext, and `n` is the public key value.


flag: `picoCTF{sma11_N_n0_g0od_13686679}`