##### Server & Attacker IP
Flag Format: `KCTF{Serverip_Attackerip}`\
flag: `KCTF{192.168.1.10_192.168.1.9}`\

##### The Real Admin
Flag Format: KCTF{real admin's ip}\
flag: `KCTF{192.168.1.3}`\

##### The Intruder's Identity
Flag Format: KCTF{username_password}\
Apply filter: `http contains "username" && http.request.method=="POST"`\
flag: `KCTF{theexploiter_exploiter@test}`

##### Compromising the Admin
Apply filter: `http contains "admin" && http.request.method=="POST"`, then the one has same token with blog action.\
Alternatively do `http contains "_token=lj41L7Wk6N6hZd7K5twHMghHSkruvwzX3JcV5GLj" && http.request.method=="POST"`\
flag: `KCTF{admin@example.com_password}`\

##### Stealing the Sweet
Apply filter
flag: `KCTF{8881_xss}`

##### Malicious Uploads
flag: `KCTF{serverfile.php}`

#####
flag: ``

#####
Initial Reconnaissance
flag: `KCTF{nikto}`