# Network & System Log Analysis in Linux

## Overview
A SOC Analyst must be able to correlate network activity with system logs to identify potential threats. This lab covers the use of basic networking tools and log inspection to monitor system connectivity and service health.

## Tools and Commands
* **netstat / ss**: Used to investigate active network connections and listening ports.
* **ifconfig / ip addr**: Used to verify network interface configurations.
* **systemctl**: Used to check the status of critical network services.

## Practical Exercise: Verifying Network Services
To ensure that only authorized services are communicating over the network, we can inspect active listening ports:

```bash
# Displaying all listening TCP/UDP ports
netstat -tuln
