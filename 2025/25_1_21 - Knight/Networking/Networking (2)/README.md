##### The Overseer
In packet 31, `/cockpit/login` reveals the tool.
flag: `KCTF{cockpit}`

##### The Gatekeeper
flag: `KCTF{9090}`

##### The Server's Identity
Apply filter `http contains "hostname` will display only one packet, follow the stream and search hostname in the stream.
flag: `KCTF{localhost.localdomain}`

#### Tareq's Secret
Apply filter `http contains "auth" || http contains "login" || http contains "Basic"`, the last packet will contain the password.
flag: `KCTF{SecurePass}`