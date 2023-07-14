# TikDL

![ezgif-5-2171224327](https://github.com/th3k3y/TikDL/assets/49789253/091bf92e-edac-4262-b89e-1cb6704d7a8d)

Téléchargeur de Vidéos TikTok

## Description

Ceci est un projet de démonstration qui illustre comment créer un téléchargeur de vidéos TikTok en utilisant l'API RapidAPI. Vous pouvez télécharger plusieurs vidéos à la fois en entrant leurs URL, et toutes les vidéos seront regroupées dans un fichier zip une fois téléchargées.

## Installation

1. Assurez-vous d'avoir Python 3.7+ installé sur votre système. Vous pouvez télécharger Python à partir de [ici](https://www.python.org/downloads/).

2. Clonez cette repo' :
    ```
    git clone https://github.com/th3k3y/TikDL/
    ```
3. Naviguez vers le répertoire du projet :
    ```
    cd TikDL
    ```
4. Installez les dépendances :
    ```
    pip install -r requirements.txt
    ```
5. Lancez l'application :
    ```
    python tiktok.py
    ```

## Utilisation

1. Ouvrez votre navigateur et allez sur `http://localhost:5000`.

2. Vous verrez une interface utilisateur simple avec une zone de texte. Entrez les URL des vidéos TikTok que vous souhaitez télécharger (une URL par ligne) dans la zone de texte.

3. Cliquez sur le bouton `Télécharger`. Les vidéos seront téléchargées et regroupées dans un fichier zip qui se téléchargera ensuite automatiquement.

## Note importante

Ce projet est à but démonstratif et nécessite des modifications avant de pouvoir être utilisé dans un environnement de production. En particulier, vous devrez remplacer la clé API de RapidAPI par votre propre clé API dans le fichier `tiktok.py` :

```python
headers = {
    "X-RapidAPI-Key": "<votre clé API>",
    "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
}
```
