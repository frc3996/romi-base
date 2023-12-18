# FIRST Team 3996 - 2023

## Installation
Télécharger et extraire ce projet (ou encore mieu le cloner avec git)
Utilisez VSCODE pour programmer
Dans les modules de VSCODE, ajoutez pylint

### Sur Windows
installer [python 3.10](https://www.python.org/downloads/)
Ouvrez un terminal powershell exécutez
`python -V` pour valider que votre version de python est bonne
`python -m pip install --upgrade pip` pour mettre à jours le gestionnaire des dépendances
`python -m pip install -U poetry` pour installer un outil de gestion des dépendances

Ouvrez un terminal et naviguez jusqu'au dossier du projet. Exécutez
`poetry install`

### Sur Linux (Ubuntu 2022.04 ou plus)
python 3.10 est installé par défaut
Ouvrez un terminal et exécutez
`python3 -V` pour valider que votre version de python est bonne
`sudo apt update && sudo apt install -y python3-pip` pour installer le gestionnaire des dépendances
`python3 -m pip install --upgrade pip` pour mettre à jours le gestionnaire des dépendances
`python3 -m pip install -U poetry` pour installer un outil de gestion des dépendances

Ouvrez un terminal et naviguez jusqu'au dossier du projet. Exécutez
`poetry install`


## Utilisation
NOTE: Remplacez `python3` par `python` selon votre plateforme

Ouvrir un terminal et naviguez jusqu'au dossier du projet. Depuis cet emplacement, vous pouvez exécuter les commandes suivantes

`poetry run python ./robot-code/robot.py sim --ws-client` pour déployer le code sur Romi


## Ajouter une nouvelle dépendance
Exécuter le fichier poetry_shell.ps1 (Windows) ou poetry_shell.sh (Linux)
`poetry add <nom_de_la_dependance>` pour ajouter une nouvelle dépendance (Ex.: robotpy-navx ou robotpy-ctre)

`poetry update <nom_de_la_dependance>` pour mettre à jours une dépendance
`poetry update` pour mettre à jours toute les dépendances