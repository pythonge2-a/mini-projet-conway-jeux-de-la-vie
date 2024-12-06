[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oOQR1xPR)
# Nom du projet

## Membres

- Rémi Richard
- Romain Schorro
- Jonas Perez

## Description

Le jeu de la vie de Conway est un automate cellulaire inventé par le mathématicien britannique John Horton Conway en 1970. Il s'agit d'un jeu à zéro joueurs sans objectif, et où la seule interaction possible est de créer un état initial (seed). Le jeu consiste en une grille infinie en deux dimensions de l'espace et une dimension de temps, où chaque cellule peut être à l'état "mort" ou "vivant". Quand la cellule est "morte", elle est blanche. Quand la cellule est "vivante", elle est noire. Ces cellules peuvent naître ou mourir selon quatre règles simples :

1. Toute cellule vivante avec moins de deux cellules vivantes avoisinantes meurt (sous-population)

2. Toute cellule avec deux ou trois cellules vivantes avoisinantes reste vivante jusqu'à la prochaine unité de temps.

3. Toute cellule avec plus de trois cellules vivantes avoisinantes meurt (surpopulation).

4. Toute cellule morte avec exactement trois cellules vivantes avoisinantes devient une cellule vivante (reproduction).

Voici un exemple de cellules créant d'autres cellules :

![Alt Text](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

Ces règles en apparence simples permettent en réalité de recréer des pattern et des systèmes multicellulaires bien plus complexes, certaines pouvant même se reproduire, créer des patterns aléatoires et/ou d'avoir des durées de vie infinies. 

L'idée est de recréer un jeu de la vie sur Python à partir de rien, avec une interface simple pour le joueur. Pour rajouter de l'interactivité, nous donnerons la possibilité aux joueurs de rajouter des cellules pendant la simulation. L'option de ralentir ou accélerer l'écoulement du temps sur le tas sera également possible.

## Cahier des charges

- Un jeux de la vie fonctionnel avec la règle B3S23 
- Possibilité d'ajouter des cellules vivantes durant le jeu
- Ajout de tests pour notre code
- Possibilité d'accélérer, décélerer et arrêter le temps
- **Si possible** changer les règles avant le lancement du jeu

## Installation

```bash
poetry install
...
```
