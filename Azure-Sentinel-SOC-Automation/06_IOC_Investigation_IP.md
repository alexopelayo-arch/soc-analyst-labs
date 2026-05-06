# IOC Investigation: Specific IP Address
Investigating a specific Indicator of Compromise (IOC). This query filters logs for a suspicious IP address (`187.204.92.150`) to determine which applications were targeted and the total number of attempts made from this source.

```kusto
AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(24h)
| where IPAddress == "187.204.92.150"
| summarize TotalAttempts = count() by AppDisplayName
