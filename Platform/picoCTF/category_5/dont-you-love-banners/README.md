# dont-you-love-banners [Medium] (by Loic Shema / syreal) - picoCTF 2024
> <p>Can you abuse the banner?</p>


There is two remote server, one is for the leaked password, one is the server we would like to exploit. First, get the password from first server: `SSH-2.0-OpenSSH_7.6p1 My_Passw@rd_@1234`, where `My_Passw@rd_@1234` is the password.
Connect the second server, we have three questions that need to answer (two of them can get the answer from internet):
```text
what is the password?
- My_Passw@rd_@1234
What is the top cyber security conference in the world?
- DEF CON
the first hacker ever was known for phreaking(making free phone calls), who was it?
- JOHN DRAPER
```
Then, use `ls` we know that there is two file `banner` and `text`. And as the description states, the flag is in the `/root`: `flag.txt` and `script.py`.
However, we can not access `flag.txt` because of permission denied. But `script.py`:
```python
import os
import pty

incorrect_ans_reply = "Lol, good try, try again and good luck\n"

if __name__ == "__main__":
    try:
      with open("/home/player/banner", "r") as f:
        print(f.read())
    except:
      print("*********************************************")
      print("***************DEFAULT BANNER****************")
      print("*Please supply banner in /home/player/banner*")
      print("*********************************************")

try:
    request = input("what is the password? \n").upper()
    while request:
        if request == 'MY_PASSW@RD_@1234':
            text = input("What is the top cyber security conference in the world?\n").upper()
            if text == 'DEFCON' or text == 'DEF CON':
                output = input(
                    "the first hacker ever was known for phreaking(making free phone calls), who was it?\n").upper()
                if output == 'JOHN DRAPER' or output == 'JOHN THOMAS DRAPER' or output == 'JOHN' or output== 'DRAPER':
                    scmd = 'su - player'
                    pty.spawn(scmd.split(' '))

                else:
                    print(incorrect_ans_reply)
            else:
                print(incorrect_ans_reply)
        else:
            print(incorrect_ans_reply)
            break

except:
    KeyboardInterrupt
```

One thing to note is that the at the very beginning of program, it tries to open the `banner` file. So a symlink is needed here: `ln -sf /root/flag.txt banner` to force a symlink. Then, we reconnect to the remote server,and it will access the symlink and print out the flag.

flag: `picoCTF{b4nn3r_gr4bb1n9_su((3sfu11y_218ef5d6}`