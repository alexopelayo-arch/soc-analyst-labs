# Data Aggregation and Counts
Using the `summarize` operator to calculate the total number of sign-in attempts grouped by application name. This helps identify which applications have the highest volume of activity.

```kusto
AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(24h)
| summarize Count = count() by AppDisplayName
| sort by Count desc
