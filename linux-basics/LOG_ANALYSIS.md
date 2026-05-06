# Linux Log Analysis for Security Investigations

## Overview
This lab demonstrates the use of Linux command-line tools to parse and analyze system logs. As a SOC Analyst, being able to manually investigate logs via the terminal is a critical skill for incident response and threat hunting when a SIEM is not available.

## Key Commands Used
* **grep**: Used to filter specific patterns (e.g., "Failed password") within large log files.
* **awk**: Used to extract specific fields, such as IP addresses, timestamps, or usernames.
* **sort & uniq**: Used to aggregate data, count occurrences, and identify patterns of attack.
* **tail/head**: Used to examine the most recent or initial entries in a log file.

## Practical Example: Investigating Brute Force Attacks
The following command is used to identify the top 10 IP addresses with the most failed login attempts in the authentication log (`auth.log`), which is a primary indicator of a Brute Force attack:

```bash
sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -10
