import os
import json
import shutil

def load_server_info(cookies: str):
	try: 
		with open(cookies) as f:
			data = json.load(f)
		return data["host"], data["port"]

	except:
		return "127.0.0.1", 1233

def store_server_info(cookies: str, host: str, port: int):
	server = {
		"host": host,
		"port": port
	}

	json_obj = json.dumps(server)
	with open(cookies, "w") as f:
		f.write(json_obj)

def saveImages(self, origin, destination):
	shutil.copy(origin, destination)

	return True