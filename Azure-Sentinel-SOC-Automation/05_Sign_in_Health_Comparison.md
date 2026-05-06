# Sign-in Health Comparison
Using conditional counting with `countif` to compare successful sign-ins against failed attempts per application. This dashboard-style query helps security analysts quickly spot applications with unusual failure rates.

```kusto
AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(24h)
| summarize 
    Success = countif(ResultType == 0), 
    Failed = countif(ResultType != 0) 
    by AppDisplayName
| sort by Success desc
