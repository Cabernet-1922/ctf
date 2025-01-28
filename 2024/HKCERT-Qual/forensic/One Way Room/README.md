# One Way Room [150 points] (87 solves)
flag: `hkcert24{h4v3_4_t4st3_0f_1inux_f0r3nsic_0r_b3ing_rickr011_4g4in}`
Basically we need to find out some answers from `.vmdk` file.
Questions:
- UUID of /dev/sda1
  - `b2bc2958-9c47-495a-8bab-3bae83cf9ca4`
- Backdoor URL
  - `https://t.ly/backdoor.sh`
- Password for user very-secure
  - `nokiasummer1990`
- Deleted file flag
  - `flag{th3_fi13_sh411_b3_d313t3d}`
- IP of login attempt
  - `192.166.246.54`


1. For UUID, we know that the UUID is formed with hex digit and `-`, so the character set is `[0-9a-f]` and `-`.
```bash
strings Lubuntu_64-bit.vmdk | grep -oP "UUID=[0-9a-f\-]*"
```
2. Backdoor URL, url usually formed with `http`, and that line may contain key word `backdoor` as well. So we can check:
```bash
strings Lubuntu_64-bit.vmdk | grep -i "backdoor" -B 1 -A 1
```

3. For password, put them into txt file. Then trial and error, get the correct password.
```bash
strings Lubuntu_64-bit.vmdk | grep -i "password" -B 1 -A 1 > passwords.txt
```



4. For deleted file flag, simply search flag format:
```bash
strings Lubuntu_64-bit.vmdk | grep -oP "flag{.*}"
```

5. For IP of login attempt, we need to first save all the ip in a file for convenient purpose. After we get the saved file, we know from the question, the username is `very-secure` which might be also related in this question, and we search a bit can get the ip.
```base
grep -E '\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?(\.|$)){4}\b'
```