# :globe_with_meridians: Projet Noise2Noise DeepLearning
Projet pour le cours de DeepLearning à CentraleSupélec.

## :page_facing_up: Description

## ❓ Problématiques

## 🎯 Objectifs

## 🤔 Choix techniques

## :card_index_dividers: Segmentation
Notre répertoire est segmenté en X fichiers python, X fichiers jupyter notebooks, deux fichiers markdown, un fichier .gitinore et un fichier texte pour les requirements :

```bash 
.
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt 
├── 
├── 
├── 
└── 
```

- ``README.md`` contient l'ensemble des informations sur le projet pour pouvoir l'installer.
- ``CONTRIBUTING.md`` contient l'ensemble des informations sur les normes et les pratiques de collaboration et de gestion du projet.
- ``.gitignore`` contient les fichiers qui doivent être ignorés lors de l'ajout de fichiers au dépôt Git.
- ``requirements.txt`` contient la liste des modules et des bibliothèques Python qui doivent être installés, ainsi que leur version spécifique.


## :wrench: Installation
Pour lancer, nous vous recommandons sur un terminal uniquement :

1. Tout d'abord, assurez-vous que vous avez installé une version `python` supérieure à 3.9. Nous vous conseillons un environnement conda avec la commande suivante : 
```bash
conda create --name noise2noise python=3.9
```
- Pour activer l'environnement :
```bash
conda activate noise2noise
```
- Pour accéder au répertoire : 
```bash
cd DeepLearning_Project
```

2. Vous devez ensuite installer tous les `requirements` en utilisant la commande suivante :
```bash
pip install -r requirements.txt
```

3. Exécuter X en utilisant la commande suivante :
```bash
python3 X
```

Exécuter ensuite les notebooks python dans l'ordre suivant : 

1. 

## :thinking_face: Choix
Nous avons sélectionné quatre cas de pays qui posent problème s'ils sont tirés comme pays initial en début de partie ou comme pays voisin lors des manches suivantes :
1. Les pays ayant aucun pays limitrophe. 
2. Les anciens pays.
3. Les anciennes civilisations comme l'Égypte antique.
4. Les îles. Wikidata considèrent sur certaines îles, des pays limitrophes. 
Pour l'ensemble de ces quatre cas, nous avons fait le choix de ne pas les prendre en compte. Nous nous restreignons pour le jeu à l'ensemble des pays qui ne sont pas dans l'un de ces quatre cas.
 
Un bon joueur doit bien réfléchir aux pays limitrophes qu'il choisit pour ne pas perdre de points. En effet, si un joueur se retrouve bloqué dans un pays lors des manches qui suivent la première manche, (ex: il désigne Portugal comme pays limitrophe de l'Espagne lors de la première manche, il n'a malheureusement plus de possibilités de pays voisins pour le Portugal lors de la seconde manche), le joueur est téléporté dans un autre pays, et devra attendre la manche suivante pour pouvoir jouer.

## :pencil2: Auteur
- MICHOT Albane



