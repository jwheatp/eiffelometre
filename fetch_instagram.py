import requests
import json
from collections import Counter
import time 

db = "db_june"

next_url = "https://api.instagram.com/v1/locations/2593354/media/recent?client_id=898dbce5998d4f1f99ad9e3a74da1c2a"

created_time = time.time()

while int(created_time) >= 1433109600 :
	r = requests.get(next_url)
	r = json.loads(r.text)

	if r["meta"]["code"] != 200 :
		print("problem")
		break

	next_url = r["pagination"]["next_url"]

	r = r["data"]

	f = open(db,"a")
	for picture in r : 
		if picture["caption"] != None :
			pid = picture["id"]
			created_time = picture["caption"]["created_time"]
			url = picture["images"]["standard_resolution"]["url"]
			f.write('%s,%s,"%s"\n' % (pid,created_time,url))
	f.close()
