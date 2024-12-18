# PW Crack 5 [Medium] (by LT 'syreal' Jones) - Beginner picoMini 2022
> <p>Can you crack the password to get the flag?</p>
<p>Download the password checker <a href='https://artifacts.picoctf.net/c/31/level5.py' download>here</a> and you'll
need the encrypted <a href='https://artifacts.picoctf.net/c/31/level5.flag.txt.enc' download>flag</a> and the
<a href='https://artifacts.picoctf.net/c/31/level5.hash.bin' download>hash</a> in the same directory too. Here's a
<a href='https://artifacts.picoctf.net/c/31/dictionary.txt' download>dictionary</a> with all possible passwords based
on the password conventions we've seen so far.</p>


The fifth challenge of this `PW crack` series, this time we have to bruteforce all the password in the `dictionary.txt` that provided. Modify the function `level_5_pw_check` to make it auto check password:
```python
def level_5_pw_check():
    with open('dictionary.txt', 'r') as f:
        for i in f.readlines():
            user_pw = str(i.strip())
            user_pw_hash = hash_pw(user_pw)
            if( user_pw_hash == correct_pw_hash ):
                print("Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), user_pw)
                print(decryption)
                return
            print("That password is incorrect")
```

flag: `picoCTF{h45h_sl1ng1ng_36e992a6}`