# Linux File Permissions & Security Hardening

## Overview
Understanding and managing file permissions is a fundamental pillar of Linux security. This lab demonstrates how to identify insecure permission settings and apply the **Principle of Least Privilege (PoLP)** to protect sensitive data.

## Permission Audit: Identifying Risks
In the provided evidence, we can identify a significant security risk. The file `access.log` has **777 permissions** (`rwxrwxrwx`), highlighted in **green**. This is dangerous because it allows any user on the system to Read, Write, and Execute the file, potentially leading to data tampering or unauthorized access.

| Numeric | Symbolic | Security Context |
| :--- | :--- | :--- |
| **777** | `rwxrwxrwx` | **CRITICAL RISK.** Full access for everyone. |
| **755** | `rwxr-xr-x` | Safe for shared scripts (Owner can write). |
| **644** | `rw-r--r--` | Standard for configuration files. |
| **700** | `rwx------` | **Secure.** Full access for owner only. |

## Practical Exercise: Hardening Access Control
To secure this file and ensure that only the owner has full control, the following command is used to remove global access:

```bash
# Securing the sensitive log file
chmod 700 access.log

# Verifying the new security posture
ls -l access.log
