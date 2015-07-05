# imports
import requests
import json
from collections import Counter
import time 

# database name
db = "db_june"

# api url
next_url = "https://api.instagram.com/v1/locations/2593354/media/recent?client_id=898dbce5998d4f1f99ad9e3a74da1c2a"

# current time
created_time = time.time()

# while the time is after the 1st of June
while int(created_time) >= 1433109600 :
	# get request
	r = requests.get(next_url)

	# parse response
	r = json.loads(r.text)

	# get next url (pagination)
	next_url = r["pagination"]["next_url"]

	# read data
	r = r["data"]

	# write in db
	f = open(db,"a")
	for picture in r : 
		if picture["caption"] != None :
			pid = picture["id"]
			created_time = picture["caption"]["created_time"]
			url = picture["images"]["standard_resolution"]["url"]
			f.write('%s,%s,"%s"\n' % (pid,created_time,url))
	f.close()
