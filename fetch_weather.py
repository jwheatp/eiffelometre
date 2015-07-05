# imports
import requests
import json
from collections import Counter
import time 
import pandas as pd

# database name
db = "db_june_weather"

# start (1st of June)
start = pd.to_datetime(1433109600, unit='s')

# end (30st of June)
end = pd.to_datetime(1435615200, unit='s')

# generate day list (in a datetime format)
days_list = pd.DatetimeIndex(pd.date_range(start, end, freq='d')).tz_localize('UTC').tz_convert('Europe/Paris')

# forecast dictionary
# we encode the weather in that way :
# 0 : clear (day or night)
# 1 : rain
# 2 : snow
# 3 : sleet
# 4 : wind
# 5 : fog
# 6 : cloudy
# 7 : partly cloudy (day or night)
forecast = {"clear-day" : '0', "clear-night" : '0', "rain" : '1', "snow" : '2', "sleet" : '3', "wind" : '4', "fog" : '5', "cloudy" : '6', "partly-cloudy-day" : '7', "partly-cloudy-night" : '7'}

# iterate on each day
for day in days_list :
	# convert the date to timestamp for the api
	timestamp = day.value//1000000000

	# call the api to get hourly weather forecast for this day, at the Eiffel tower
	r = requests.get("https://api.forecast.io/forecast/f5ca741e74685d3f2dd93dedda089af6/48.858844,2.294351,%s" % timestamp)

	# load response in json
	r = json.loads(r.text)

	# levels
	levels = []

	# get level for each hour
	for hour in r["hourly"]["data"] :
		levels.append(forecast[hour["icon"]])

	# update db file
	f = open(db,"a")
	levels_tostring = ",".join(levels)
	f.write('%s\n' % levels_tostring)
	f.close()
