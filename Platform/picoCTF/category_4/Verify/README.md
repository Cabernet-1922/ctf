# Verify [Easy] (by Jeffery John) - picoCTF 2024
> <p>People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.</p>

```bash
sha256sum files/* | grep 467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02
```
Output:
```text
467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02  files/c6c8b911
```

```bash
./decrypt.sh files/c6c8b911
```

flag: `picoCTF{trust_but_verify_c6c8b911}`