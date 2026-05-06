# Filtering and Selection
Refining search results by filtering for specific conditions (successful sign-ins) and selecting only the most relevant columns for analysis.

```kusto
AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(24h)
| where ResultType == 0
| project TimeGenerated, UserPrincipalName, AppDisplayName
