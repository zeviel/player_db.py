from requests import get


class PlayerDB:
	def __init__(self):
		self.api = "https://playerdb.co/api"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
		}
	
	def minecraft_account_lookup(self, username: str):
		return get(
			f"{self.api}/player/minecraft/{username}",
			headers=self.headers).json()
		
	def steam_account_lookup(self, steam_id: str):
		return get(
			f"{self.api}/player/steam/{steam_id}",
			headers=self.headers).json()
	
	def xbox_account_lookup(self, username: str):
		return get(
			f"{self.api}/player/xbox/{username}",
			headers=self.headers).json()
