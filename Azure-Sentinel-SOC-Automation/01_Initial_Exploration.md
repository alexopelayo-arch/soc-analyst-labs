# Initial Table Exploration
To understand the structure of a table and view the most recent data within Microsoft Sentinel.

```kusto
AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(4h)
| take 10
