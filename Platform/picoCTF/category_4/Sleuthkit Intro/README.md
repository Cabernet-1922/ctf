# Sleuthkit Intro [Medium] (by LT 'syreal' Jones) - picoCTF 2022
> <p>Download the disk image and use <code>mmls</code> on it to find the size of the Linux
partition. Connect to the remote checker service to check your answer and get
the flag.</p>
<p>Note: if you are using the webshell, download and extract the disk image into
<code>/tmp</code> not your home directory.</p>
<p><a href='https://artifacts.picoctf.net/c/164/disk.img.gz' download>Download disk image</a></p>

Follow the instruction: `mmls disk.img`, it prints out:

```text
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```
The remote server ask about `the What is the size of the Linux partition in the given disk image?`. Since the length of the linux sector is on the previous output, which is `0000202752`.

flag: `picoCTF{mm15_f7w!}`

