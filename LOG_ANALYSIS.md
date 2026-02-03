# Log Analysis with cut and awk
## Files
- `/var/log/auth.log` → Authentication events
- `/var/log/syslog` → System events
## cut examples
```bash
cut -d':' -f1-3 /var/log/auth.log
Extracts date and time.

#awk '/Failed password/ {print $9}' /var/log/auth.log | sort | uniq -c
Shows failed login attempts per used

## syslog analysis
### Show which services write to the log and how many times
```bash
awk '{print $5}' /var/log/syslog | sort | uniq -c
##This command extracts the fifth field from each line in  (usually the service name), sorts the output, and then counts unique occurrences.
It shows which services are writing messages to the log and how many times each appears.

##*`cut` extracts specific fields from log lines.*  
- *`awk` processes logs with conditions, counts, and formatting.*  
- *Use them together to analyze `auth.log` and `syslog` for security and system events.*  

