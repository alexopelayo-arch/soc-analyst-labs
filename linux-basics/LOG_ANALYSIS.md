# Linux Log Analysis for Security Investigations

## Overview
This lab demonstrates the use of Linux command-line tools to parse and analyze system logs. As a SOC Analyst, investigating logs via the terminal is a critical skill for incident response and tracking user activity.

## Key Commands Used
* **grep**: Used to filter specific patterns (e.g., "session opened") within log files.
* **head**: Used to examine the most recent entries in the authentication log.

## Practical Example: Monitoring User Sessions
The following command is used to track successful login sessions and privilege escalations in `auth.log`:

```bash
grep "session opened" /var/log/auth.log | head -n 10
