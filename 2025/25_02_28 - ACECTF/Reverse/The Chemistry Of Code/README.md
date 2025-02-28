# The Chemistry Of Code [200 points] (210 solves)
Only two line of rust code is useful:
```rust
const FERROUS_OXIDE_USERNAME: &str = "AdminFeroxide";
const ANIONIC_PASSWORD: &str = "NjQzMzcyNzUzNTM3MzE2Njc5MzE2ZTM2";
```
ANIONIC_PASSWORD is a base64 strings, decode it to plaintext. Then, we have the username and password in our hand:
```bash
./chemistryofcode
Introduce the Catalyst: AdminFeroxide
Introduce the Reagent: d3ru571fy1n6
Crystallized Flag (ASCII): ACECTF{4ppr3n71c3_w4l73r_wh1t3}
```

flag: `ACECTF{4ppr3n71c3_w4l73r_wh1t3}`