Premièrement on va parler de la régression linéaire et K-Nearest Neighbors (KNN)

# 1. Régression linéaire

L'apprentissage supervisé consiste à prédire une variable cible (dépendante) à partir de variables prédictrices (indépendantes). En utilisant ces variables, une fonction est générée pour associer les entrées aux sorties. La formation continue jusqu'à atteindre le niveau de précision souhaité sur les données d'entraînement.

Par conséquent, il existe de nombreux exemples d'algorithmes d'apprentissage supervisé. Dans ce cas, je voudrais me concentrer sur la régression linéaire.

Il est utilisé pour estimer les valeurs réelles (coût des maisons, nombre d'appels, ventes totales,etc.) 
sur la base de variables continues. Ici, nous établissons une relation entre les variables indépendantes et dépendantes en adaptant une meilleure ligne. Cette ligne de meilleur ajustement est appelée ligne de régression et représentée par une équation linéaire Y = a * X + b.

La meilleure façon de comprendre la régression linéaire est de revivre cette expérience de l’enfance. Disons que vous demandez à un enfant de cinquième année de classer les gens dans sa classe en augmentant son poids, sans leur demander leur poids! Que pensez-vous que l'enfant va faire? Il / elle serait probablement regarder (analyser visuellement) à la hauteur et la construction de personnes et les organiser en utilisant une combinaison de ces paramètres visibles.

C'est la régression linéaire dans la vie réelle! L'enfant a effectivement compris que la taille et la
construction seraient corrélées au poids par une relation, ce qui ressemble à l'équation ci-dessus.

Dans cette équation :

Y – Dependent Variable

a – Slope

X – Independent variable

b – Intercept

Ces coefficients a et b sont calculés en minimisant la somme de la différence au carré de la
distance entre les points de données et la ligne de régression.


# 2. K-Nearest Neighbors (KNN)

Le KNN (k-Nearest Neighbors) est un algorithme d'apprentissage supervisé qui prédit la classe d'une donnée en se basant sur les classes des données les plus proches dans l'espace des caractéristiques. Il attribue une nouvelle donnée à la classe majoritaire parmi ses k plus proches voisins. Le modèle n'a pas de phase d'entraînement explicite : il calcule les distances et fait ses prédictions en temps réel, en fonction des données disponibles.

Le KNN peut également être utilisé pour estimer des valeurs réelles, comme le coût des maisons, le nombre d'appels reçus, ou les ventes totales, en fonction de variables continues. 
Au lieu d'adapter une ligne de régression, il prédit la valeur d'une nouvelle donnée en prenant la moyenne ou la médiane des valeurs de ses k plus proches voisins. Par exemple, pour prédire le prix d'une maison, l'algorithme s'appuie sur des données telles que la superficie, le nombre de chambres ou la localisation, en utilisant les prix des maisons voisines dans des conditions similaires.


![Capture d’écran du 2024-10-24 11-06-38](https://github.com/user-attachments/assets/8351e10b-bc91-46ce-848d-0d59a50f3232)


