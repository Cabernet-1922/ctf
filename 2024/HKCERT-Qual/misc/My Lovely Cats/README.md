# My Lovely Cats [200 points] (62 solves)
Get the reverse base64 strings from `.mov` file and decode it, get the url inside the message and view the txt file. The flag is in the txt file, use one line command to get the flag: \
```bash
strings DCIM_0017.mov.lnk | grep -oP '[A-Za-z0-9+/=]{20,}' | awk 'NR==2' | rev | base64 --decode | grep -oP 'https?://[^\s]+txt' | xargs curl | grep -oP 'hkcert24{.*}'
```