# OpenClassrooms: Projet 2 / Exercice: Jobs to Scrape

Ce script permet de récupérer via Scrapy les informations de toutes les annonces de jobs sur https://www.python.org/jobs et https://djangojobs.net/jobs/.
Ces informations sont les suivantes:
 - Titre
 - Lien
 - Ville
 - État
 - Pays
 - Type
 - Date de publication
 - Catégorie
 - Remote
 - Relocation

Ces données sont ensuite classées par catégories et par types puis sont inscrites dans un fichier CSV correspondant.
Les données sont générées à la racine du projet suivant cette arborescence:
```
|-- data/
    |-- site1/
        |-- allposts.csv
        |-- categories_posts/
            |--categorie1.csv
            ...etc
        |-- types_posts/
            |--types1.csv
            ..etc
    |-- site2/
    ...etc
```
# Installation:
Commencez tout d'abord par installer Python.
Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/FlorianMgs/OC_P2_JobsToScrape.git
```
Placez vous dans le dossier OC_P2_JobsToScrape, puis créez un nouvel environnement virtuel:
```
python -m venv env
```
Ensuite, activez-le.
Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis:
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le script:
```
python main.py
```
