# Unique Users per Application
Utilizing the `dcount` function to identify the number of unique users accessing each application. This metric is essential for understanding user behavior and identifying potential shared account usage.

```kusto
AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(24h)
| summarize UniqueUsers = dcount(UserPrincipalName) by AppDisplayName
