import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# import data
# it's a small dataset so we can load it completely
df = pd.read_csv('db_june', sep=",")

# we keep only the timestamp
df = df.ix[:,"timestamp"]

# convert dates to pandas dates
dates = pd.DatetimeIndex(pd.to_datetime(df, unit='s', utc=True)).tz_localize('UTC').tz_convert('Europe/Paris')

#sort
dates = dates.order()

# create count dataframe and sample by hour
dates = pd.DataFrame([1]*len(dates), index=dates)
dates = dates.resample('1h', how='sum')

out_db = "db_june_dayhourcount"
f = open(out_db,"w")
for d in dates.iterrows() :
	f.write("%s,%s,%s\n" % (d[0].weekday(),d[0].hour,d[1][0]))

f.close()

#######
# Plot
#################

daylists = []
for group in dates.groupby(dates.index.day):
	group[1].index = group[1].index.hour
	daylists.append(group[1])

daylists = pd.concat(daylists, axis=1)

plt.figure()

daylists.plot(legend=None)

plt.title('Number of photos per hour taken at\n the Eiffel tower, for different days')
plt.xlabel("hours of the day")
plt.ylabel("number of photos")

plt.savefig("plot.png")
