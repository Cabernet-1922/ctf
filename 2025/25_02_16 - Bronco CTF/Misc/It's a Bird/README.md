# It's a Bird [448 points] (83 solves)
```bash
stegseek myBirb.jpg
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""6 MB)
[i] Original filename: "birb.csv".
[i] Extracting to "myBirb.jpg.out".
```
In that extracted `.csv` file, column R seems like ascii numbers. We can put our formula in any of the cells other than one in column R:
```csv
=TEXTJOIN("",TRUE,IF(R:R<>"",CHAR(R:R),""))
```

flag: `bronco{i<3planes}`