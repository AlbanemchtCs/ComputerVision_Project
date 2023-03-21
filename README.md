# :globe_with_meridians: Projet Noise2Noise DeepLearning et ComputerVision
Projet pour les cours de DeepLearning et ComputerVision à CentraleSupélec.

Le dataset du projet se trouve sur [GoogleDrive](https://drive.google.com/drive/folders/1ibHySGXsBqP30s7mwOPyFWa1eA8NYo2J?usp=sharing).

## 🎯 Objectifs
Le but de ce projet des cours Deep Learning et ComputerVision est d’implémenter un modèle similaire au [Noise2Noise](https://arxiv.org/pdf/1803.04189.pdf), un réseau de débruitage d’images entraîné sans image de référence propre. 

[Kaggle](https://www.kaggle.com/datasets/mehrdadkianiosh/noisy-images?resource=download) mettant à disposition un dataset basé sur le papier original, l’objectif est d’étudier et d’implémenter différentes architectures de réseaux de neurones afin de vérifier les affirmations et résultats du papier original. Le code des auteurs se basant sur TensorFlow, le framework PyTorch est ici utilisé comme alternative.

## :page_facing_up: Description
Avec Noise2Noise, les auteurs souhaitent tirer parti des DNN (deep neural networks) pour éviter la modélisation de vraisemblance statistique explicite préalable des images bruitées et à la place apprendre à mettre en correspondance les images bruitées avec les images propres non observées. 

En particulier, le débruitage peut être réalisé en utilisant uniquement des images bruitées, si le bruit est additif et non biaisé. En d’autres termes, il est possible, à partir des données d’apprentissage sur deux images bruitées de manière indépendante, d’apprendre indirectement le modèle de vraisemblance statistique explicite de la corruption sans se baser sur un modèle de débruitage qui utilise des images propres.

## 🤔 Choix techniques
Deux modèles ont été implémentés : un Resnet et un U-Net. Ces deux derniers découlent de l’architecture Noise2Noise du papier original. 

Un réseau discriminant a également été implémenté pour pouvoir comparer la performance entre un débruiteur avec un training discriminant (avec une image propre) et les deux réseaux Noise2Noise déployés, pour valider l'hypothèse du papier original qui montre qu’en restaurant des images en ne regardant que des exemples corrompus produit des performances égales, voire supérieures, à celles obtenues en utilisant des données propres. 

Une augmentation des données a été réalisé sur l'ensemble des trois modèles pour améliorer notre performance globale des modèles, basée sur la métrique PSNR (Peak Signal Noise Ratio), exprimée en décibel (dB). Le PSNR permet de quantifier la performance des modèles en mesurant la qualité de reconstruction de l’image compressée par rapport à l’image propre.

## :card_index_dividers: Segmentation
Notre répertoire est segmenté en 4 fichiers jupyter notebooks, 3 fichiers .pth, deux fichiers markdown, un fichier .gitinore et un fichier texte pour les requirements :

```bash 
.
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt 
├── Networks
│     ├── Noise2Noise_ResNet.ipynb
│     ├── parameters_models_Resnet.pth
│     ├── Noise2Noise_UNet.ipynb
│     ├── parameters_models_UNet.pth
│     ├── Inverse_Noise2Noise_Discriminative.ipynb
│     └── parameters_models_Discriminative.pth
└── Preprocessing
      └──  Data_augmentation.ipynb

```

- ``README.md`` contient l'ensemble des informations sur le projet pour pouvoir l'installer.
- ``CONTRIBUTING.md`` contient l'ensemble des informations sur les normes et les pratiques de collaboration et de gestion du projet.
- ``.gitignore`` contient les fichiers qui doivent être ignorés lors de l'ajout de fichiers au dépôt Git.
- ``requirements.txt`` contient la liste des modules et des bibliothèques Python qui doivent être installés, ainsi que leur version spécifique.
- ``Networks`` contient l'ensemble des jupyter notebooks de nos réseaux implémentés ``Noise2Noise_ResNet.ipynb``, ``Noise2Noise_UNet.ipynb`` et ``Inverse_Noise2Noise_Discriminative.ipynb``, ainsi que les fichiers de sauvegarde des paramètres du dernier training de chaque modèle ``parameters_models_Resnet.pth``, ``parameters_models_UNet.pth`` et ``parameters_models_Discriminative.pth``.
- ``Preprocessing`` contient le jupyter notebook ``Data_augmentation.ipynb`` qui permet de générer les fichiers augmentés pour le training set et validation set (utilisé comme training set dans le réseau discriminatif).

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

Exécuter ensuite les notebooks jupyter dans l'ordre suivant : 

1. Data_augmentation.ipynb 
2. Noise2Noise_ResNet.ipynb
3. Noise2Noise_UNet.ipynb
4. Inverse_Noise2Noise_Discriminative.ipynb

## :pencil2: Auteurs
- MICHOT Albane
- NONCLERCQ Rodolphe



