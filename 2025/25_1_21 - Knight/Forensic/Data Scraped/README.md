Unzip the `.ova` file, we get `kali-linux-2024-disk001.vmdk`. With Autospy, easy to find that there is 6 user folder under `/home`:
```dirtree
home
├── alice
├── bob
├── intruder
├── kali
├── robot
├── siam
```
There is two sussy zip files under `/home/bob/Downloads`,
```dirtree
home
├── bob
│   ├── Downloads
│   │   ├── challenge_final.zip
│   │   ├── pass.zip
```
This may imply the password of `challenge_final.zip` is inside `pass.zip`. There is a picture inside `pass.zip`, extract the password by using aperi'Solve: `Null_V4luE_M3`.
Extract the image from challenge_final.zip with password, then extract the flag with stegseek:
```bash
>stegseek challenge_final.jpg -wl rockyou.txt

StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "password123"
[i] Original filename: "flag.txt".
[i] Extracting to "challenge_final.jpg.out".
```

flag: `KCTF{it_w4s_L0n9_Pr0c3s5}`
