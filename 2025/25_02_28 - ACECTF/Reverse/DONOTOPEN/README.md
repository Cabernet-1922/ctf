# DONOTOPEN [400 points] (154 solves)
```bash
> tail -n +$(awk '/^__ARCHIVE_BELOW__/ {print NR + 1; exit 0; }' DONTOPEN) DONTOPEN | gzip -d > extracted_script.py
```
Then, modify a bit of the extracted script to get the flag.

flag: `ACE{e2e3619b630b3be9de762910fd58dba7}`