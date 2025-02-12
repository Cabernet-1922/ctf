# Parrot [225 points] (20 solves)
Pretty simple overflow challenge, `buf[250]` implies the once the input overwrite the 250 byte, it will fail.
But actually after some tests, 263 bytes will right just overwrites.
So one of the possible input is `'A' * 263`