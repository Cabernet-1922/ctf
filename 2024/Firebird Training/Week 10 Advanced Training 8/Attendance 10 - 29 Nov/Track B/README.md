# Attendance 10 - 29 Nov [1 points] (25 solves)
```bash
tshark -r 10b_attendance.pcapng -T fields -e ip.dst -Y ip.src==10.0.2.15 | tr '\n.' ' ' | xargs printf '%d ' | tr ' ' '\n' | awk '{printf "%c", $1}'
```