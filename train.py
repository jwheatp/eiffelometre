# imports
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import KFold

# import data
# it's a small dataset so we can load it completely
df = pd.read_csv('db_june_dayhourcount', sep=",")

# weather data
df_weather = pd.read_csv('db_june_weather', sep=",")

weather = []
for row in df_weather.iterrows() :
	index, data = row
	weather.extend(data.tolist())

df["weather"] = weather

y = df[["count"]].as_matrix()
y = np.ravel(y)
y = y.astype(float)

y = (y-min(y))/(max(y)+1-min(y))

bins_5 = np.array([0,0.2,0.4,0.6,0.8,1])
bins_4 = np.array([0,0.25,0.5,0.75,1])
bins_3 = np.array([0,0.33,0.66,1])

y = np.digitize(y, bins_3)

X = df[["weekday","hour","weather"]].as_matrix()


n = len(y)

clf = SVC()

kf = KFold(n, n_folds=5, shuffle=True)
scores = []
for train, test in kf:
	X_train = [X[i] for i in train]
	y_train = [y[i] for i in train]

	clf.fit(X_train,y_train)

	X_test = [X[i] for i in test]
	y_test = [y[i] for i in test]

	scores.append(clf.score(X_test,y_test))

print(np.mean(scores))
