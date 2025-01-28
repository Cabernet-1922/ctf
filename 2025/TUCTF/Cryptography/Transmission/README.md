# Transmission [338 points] (61 solves)
Given two xor key, the second key is used in this challenge. When xor the key with our flag prefix `TUCTF{`: `The-Au`, `Au` here may mean `Automatons` after reading the challenge description. Keep going our word guessing:
```text
TUCTF{  ->  The-Au
The-Automatons  ->  TUCTF{With_Ste
TUCTF{With_Steel_  ->  The-Automatons-Wi
The-Automatons-Will  ->  TUCTF{With_Steel_Hea
TUCTF{With_Steel_Heart_  ->  The-Automatons-Will-Ris
The-Automatons-Will-Rise-  ->  TUCTF{With_Steel_Heart_an
TUCTF{With_Steel_Heart_and_  ->  The-Automatons-Will-Rise-Ag
The-Automatons-Will-Rise-Again  ->  TUCTF{With_Steel_Heart_and_Iro
TUCTF{With_Steel_Heart_and_Iron  ->  The-Automatons-Will-Rise-AgainT
```
Since character after Again start repetition, so we can stop here.\
flag: `TUCTF{With_Steel_Heart_and_Iron}`