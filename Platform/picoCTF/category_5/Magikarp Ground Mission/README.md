# Magikarp Ground Mission [Easy] (by syreal) - picoCTF 2021
> Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`


Connect to the remote server, then `cat *`:
```text
picoCTF{xxsh_
Next, go to the root of all things, more succinctly `/`
```
Follow the instruction as `cd /`. Then, we have `2of3.flag.txt` and `instructions-to-3of3.txt` there. 
```text
0ut_0f_\/\/4t3r_
Lastly, ctf-player, go home... more succinctly `~`
```
Follow with `cd home/` and `cd ctf-player/`, we can see the last part of this challenge.
```text
3ca613a1}
```
After all, concatenate the three part together to get the flag.

flag: `picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}`