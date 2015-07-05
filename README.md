# Eiffelomètre
**Prédire le taux de fréquentation de la tour Eiffel avec le réseau social Instagram**

## Objectif
L'objectif de ce modèle est de prédire le taux de fréquentation de la tour Eiffel sur une échelle discrète (par exemple de 1 à 5), en se basant sur le nombre de photos prises et postées sur Instagram à cet endroit. On suppose que la proportion de touristes postant des photos sur Instagram est toujours la même et évolue de la même manière que le nombre total de touristes à la tour Eiffel.

## Modèle
On décide de réaliser un modèle simple en prenant en compte trois paramètres :
* le jour de la semaine (par exemple "Lundi")
* l'heure du jour (par exemple "22h")
* la description météorologique (par exemple "ensoleillé")

## Données
### Instagram
Le premier jeu de données est obtenu via le réseau social de photos Instagram. Beaucoup de photos sont associées à un lieu par l'utilisateur. On décide de récupérer toutes les photos prises à la tour Eiffel entre le 1er juin et le 3 juillet. Les données sont disponibles dans les fichiers `db_june` et `db_july`.
On récupère pour chaque photo :
* l'ID
* la date et l'heure où elle a été postée
* le lien de l'image

Au final, seul la date et l'heure seront utilisées. Etant donné le fonctionnement d'Instagram, on suppose que toutes les photos sont postées immédiatement après avoir été prises.
