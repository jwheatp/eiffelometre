# Eiffelomètre
**Prédire le taux de fréquentation de la tour Eiffel avec le réseau social Instagram**

Les lieux touristiques de Paris sont souvent bondés et il est intéressant de modéliser cette fréquentation afin de savoir à quels moments de la journée, ou de la semaine, il est le plus conseillé de s'y rendre. Ici, on s'intéresse à la tour Eiffel dans un premier temps.

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

Le modèle est entrainé et testé sur les données du mois de juin. On utilise la méthode [*machine à vecteurs de support*](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC) implémentée dans la librairie sk-learn. Le code est disponible dans le script `train.py`.

### Précision
On test la précision pour différentes échelles de fréquentations à 3, 4 et 5 graduations. Les résultats de précisions sont disponible dans le tableau-ci-dessous.

| Echelle | Précision |
| ------------- | ------------- |
| 1 à 3  | 84.7%  |
| 1 à 4  | 79.6%  |
| 1 à 5  | 74.9%  |

## Travaux futurs
Cette expérience montre qu'il est relativement simple d'établir un modèle avec une précision correcte pour répondre à la problématique soulevée dans l'introduction. Deux pistes seraient à suivre dans le futur : 
* améliorer le modèle existant en exploitant plus de paramètres (prendre en compte le mois, les périodes de vacances, tester le degré d'influence des différents paramètres etc.)
* étendre à d'autres lieux touristiques parisiens. Il est par exemple possible de filtrer les positions géographiques des photos avec des points d'intérêt touristique enregistrés dans la base de données ouverte [OpenStreetMap](http://wiki.openstreetmap.org/wiki/Points_of_interest). Le principal écueil serait peut-être le manque de données (pas assez de photos prises) pour certains lieux dans Paris.
* utiliser les données d'autres réseaux sociaux, comme par exemple Foursquare ou Twitter.
