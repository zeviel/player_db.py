# player_db.py
Web-API for playerdb.co JSON powered player fetching and caching service

## Example
```python3
import player_db
player_db = player_db.PlayerDB()
steam_account_info = player_db.steam_account_lookup(steam_id="")
print(steam_account_info)
```
