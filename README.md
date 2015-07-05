# Eiffelomètre
**Prédire le taux de fréquentation de la tour Eiffel avec le réseau social Instagram**

## Objectif
L'objectif de ce modèle est de prédire le taux de fréquentation de la tour Eiffel sur une échelle discrète (par exemple de 1 à 5), en se basant sur le nombre de photos prises et postées sur Instagram à cet endroit. On suppose que la proportion de touristes postant des photos sur Instagram est toujours la même et évolue de la même manière que le nombre total de touristes à la tour Eiffel.

## Données
### Instagram
Le premier jeu de données est obtenu via le réseau social de photos Instagram. Beaucoup de photos sont associées à un lieu par l'utilisateur. On décide de récupérer toutes les photos prises à la tour Eiffel entre le 1er et le 30 juin. Les données sont obtenues via le script `fetch.py` et sont disponibles dans le fichier `db_june`.
On récupère pour chaque photo :
* l'ID
* la date et l'heure où elle a été postée
* le lien de l'image

Au final, seul la date et l'heure seront utilisées. Etant donné le fonctionnement d'Instagram, on suppose que toutes les photos sont postées immédiatement après avoir été prises.

### Forecast.io
On utilise aussi des données météorologiques depuis l'API http://forecast.io. Dans un souci de simplificté, on se limite à la description du temps (nuages, pluie, soleil etc.) pour chaque heure de chaque jour. Ces données sont obtenues via le script `fetch_weather.py` et sont disponibles dans le fichier `db_weather`.

## Modèle
On décide de réaliser un modèle simple en prenant en compte trois paramètres :
* le jour de la semaine (par exemple "Lundi")
* l'heure du jour (par exemple "22h")
* la description météorologique (par exemple "ensoleillé")

Le modèle est entrainé et testé sur les données du mois de juin. On utilise la méthode [*machine à vecteurs de support*](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC) implémentée dans la librairie sk-learn.
