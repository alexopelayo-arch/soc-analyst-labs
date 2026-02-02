# Linux File Permissions (chmod)

## Purpose
This section documents common Linux file permissions and their security relevance from a SOC (Security Operations Center) perspective.

## chmod Reference Table

| Permission | Symbolic      | Typical Use Case (SOC)                | Security Risk |
|-----------|---------------|----------------------------------------|---------------|
| 644       | rw-r--r--     | Log files, configuration files         | Low           |
| 755       | rwxr-xr-x     | Executable scripts and system tools    | Low           |
| 700       | rwx------     | Private scripts (single user)          | Low           |
| 600       | rw-------     | Sensitive files (keys, credentials)    | Low           |
| 744       | rwxr--r--     | User-owned scripts (limited execution) | Medium        |
| 777       | rwxrwxrwx     | ❌ Not recommended                     | **High** 🚨   |

## SOC Insight
Improper file permissions can introduce serious security risks.  
Permissions such as **777** allow any user to modify and execute files and are considered a **red flag** during SOC investigations.
