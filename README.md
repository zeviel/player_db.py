# playerdb.py
Web-API for playerdb.co JSON powered player fetching and caching service

## Example
```python3
import playerdb
playerdb = playerdb.PlayerDB()
steam_account_info = playerdb.steam_account_lookup(steam_id="")
print(steam_account_info)
```
