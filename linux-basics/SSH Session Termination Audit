# SSH & Authentication Tracking

## Overview
Monitoring authentication events is a core responsibility of a SOC Analyst. This lab demonstrates how to audit the `auth.log` file to track the status of the SSH daemon (sshd) and identify connection events, ensuring the system's remote access points are monitored.

## Technical Context
The `auth.log` file in Linux records all authentication attempts and service status changes. By auditing the SSH daemon, an analyst can verify if the service is listening on the correct ports and track when connections are established or terminated.

## Commands Used
To audit the SSH daemon activity and connection status:

```bash
grep "sshd" /var/log/auth.log | head -n 10
