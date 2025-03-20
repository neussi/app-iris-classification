# Application Web de Classification Iris

[![GitHub issues](https://img.shields.io/github/issues/neussi/app-iris-classification)](https://github.com/neussi/app-iris-classification/issues)
[![GitHub stars](https://img.shields.io/github/stars/neussi/app-iris-classification)](https://github.com/neussi/app-iris-classification/stargazers)
[![GitHub license](https://img.shields.io/github/license/neussi/app-iris-classification)](https://github.com/neussi/app-iris-classification/blob/main/LICENSE)

## Description
Cette application web interactive permet de classifier les espèces d'iris en se basant sur les caractéristiques de leurs fleurs. Elle utilise un modèle de machine learning entraîné sur le célèbre jeu de données Iris de Fisher pour prédire l'espèce d'iris (setosa, versicolor ou virginica) à partir des mesures des pétales et des sépales.

## Fonctionnalités
- Interface utilisateur moderne et responsive avec Bootstrap
- Formulaire interactif pour entrer les mesures d'un iris
- Prédiction en temps réel de l'espèce d'iris avec AJAX
- Visualisation des données avec Chart.js
- Exploration interactive des caractéristiques de chaque espèce
- Génération d'exemples aléatoires pour tester le modèle
- Graphique de dispersion configurable pour comparer les caractéristiques

## Technologie utilisée
- **Framework**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Visualisation**: Chart.js
- **Machine Learning**: Scikit-learn
- **Base de données**: SQLite3

## Installation

### Prérequis
- Python 3.8 ou plus récent
- pip (gestionnaire de paquets Python)
- Git

### Étapes d'installation
1. Clonez le dépôt:
```bash
git clone https://github.com/neussi/app-iris-classification.git
cd app-iris-classification
```

2. Créez un environnement virtuel:
```bash
python -m venv venv
```

3. Activez l'environnement virtuel:
   - Sous Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Sous macOS et Linux:
   ```bash
   source venv/bin/activate
   ```

4. Installez les dépendances:
```bash
pip install -r requirements.txt
```

5. Appliquez les migrations pour configurer la base de données:
```bash
python manage.py migrate
```

## Utilisation

1. Démarrez le serveur de développement Django:
```bash
python manage.py runserver
```

2. Ouvrez votre navigateur et accédez à:
```
http://localhost:8000
```

3. Utilisation de l'application:
   - **Prédiction d'espèce**: Entrez les mesures de l'iris dans le formulaire (longueur/largeur du sépale et du pétale) et cliquez sur "Classifier"
   - **Exemple aléatoire**: Cliquez sur le bouton "Exemple aléatoire" pour générer des valeurs de test
   - **Explorer les espèces**: Sélectionnez une espèce dans le menu déroulant pour voir ses caractéristiques moyennes
   - **Visualisation**: Utilisez le graphique de dispersion pour comparer les différentes caractéristiques en sélectionnant les axes X et Y

## Structure du projet
```
app-iris-classification/
├── .ipynb_checkpoints/      # Checkpoints pour les notebooks Jupyter
├── app/                     # Application Django principale
│   ├── __pycache__/         # Fichiers cache Python
│   ├── migrations/          # Migrations de base de données Django
│   ├── templates/           # Templates HTML
│   │   ├── base.html        # Template de base avec structure commune
│   │   └── home.html        # Page d'accueil avec formulaire de prédiction
│   ├── __init__.py          # Initialise le package Python
│   ├── admin.py             # Configuration de l'interface d'administration
│   ├── apps.py              # Configuration de l'application Django
│   ├── forms.py             # Formulaires pour la saisie des données
│   ├── iris_model.pkl       # Modèle entraîné sauvegardé
│   ├── ml_model.py          # Définition et utilisation du modèle
│   ├── models.py            # Modèles de données Django
│   ├── tests.py             # Tests unitaires
│   ├── urls.py              # Configuration des URLs
│   └── views.py             # Vues et logique métier
├── data/                    # Données utilisées par l'application
│   └── irisapp/             # Dossier contenant le dataset Iris
├── static/                  # Fichiers statiques
│   ├── css/                 # Feuilles de style
│   │   └── style.css        # Styles personnalisés
│   ├── images/              # Images et ressources graphiques
│   │   └── iris-logo.svg    # Logo de l'application
│   └── js/                  # Scripts JavaScript
├── db.sqlite3               # Base de données SQLite
├── manage.py                # Script de gestion Django
├── Perceptron_Simple.ipynb  # Notebook Jupyter pour l'exploration/l'entraînement
├── requirements.txt         # Dépendances du projet
└── README.md                # Documentation du projet (ce fichier)
```

## Points forts de l'application

### Interface utilisateur
- **Design moderne**: Interface utilisateur élégante et responsive utilisant Bootstrap 5
- **Animations**: Transitions fluides et animations pour améliorer l'expérience utilisateur
- **Cartes interactives**: Présentation des données dans des cartes visuellement attrayantes
- **Icônes FontAwesome**: Utilisation d'icônes pour améliorer la compréhension et l'esthétique

### Fonctionnalités interactives
- **AJAX**: Interactions sans rechargement de page pour une expérience fluide
- **Formulaires dynamiques**: Validation côté client et exemples aléatoires
- **Visualisations configurables**: Possibilité de choisir les axes du graphique de dispersion
- **Informations détaillées**: Affichage des caractéristiques moyennes pour chaque espèce

### Endpoints AJAX
L'application utilise des requêtes AJAX pour communiquer avec le serveur:

#### Prédiction d'espèce
```
POST /predict/
```

Exemple de requête:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Exemple de réponse:
```json
{
  "success": true,
  "species": "setosa",
  "species_info": {
    "name": "setosa",
    "avg_characteristics": {
      "sepal_length": 5.01,
      "sepal_width": 3.42,
      "petal_length": 1.46,
      "petal_width": 0.24
    }
  }
}
```

## Modèle de Machine Learning
Le modèle utilise un algorithme de classification entraîné sur le dataset Iris de Fisher pour identifier les trois espèces d'iris.

### Caractéristiques du modèle
- **Algorithme**: RandomForestClassifier de scikit-learn
- **Données d'entrée**: 4 caractéristiques (longueur et largeur des sépales et pétales)
- **Classes de sortie**: 3 espèces (setosa, versicolor, virginica)
- **Prétraitement**: Normalisation des données pour une meilleure performance

### Performance
- **Précision globale**: >95% sur l'ensemble de test
- **Séparabilité**: Excellente séparation pour l'espèce setosa, légère confusion possible entre versicolor et virginica

### Notebook Jupyter
Le projet inclut un notebook Jupyter (`Perceptron_Simple.ipynb`) qui permet d'explorer le dataset Iris et d'expérimenter avec différents algorithmes de classification, notamment le Perceptron.

## Structure du projet visuelle

```
app-iris-classification/
│
├── .ipynb_checkpoints
├── app/
│   ├── __pycache__
│   ├── migrations
│   ├── templates
│   │   ├── base.html
│   │   └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── iris_model.pkl
│   ├── ml_model.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── data/
│   └── irisapp/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   └── iris-logo.svg
│   └── js/
├── db.sqlite3
├── manage.py
└── Perceptron_Simple.ipynb
```

La structure ci-dessus montre l'organisation des fichiers du projet, avec une application Django principale (`app/`), des assets statiques et un notebook Jupyter pour l'exploration des données et l'entraînement du modèle.

## Fonctionnalités à venir
- Ajout d'une API REST complète
- Support pour le téléchargement de données personnalisées
- Interface d'administration pour visualiser les prédictions historiques
- Mode sombre

## Développement
Pour contribuer au développement:

1. Créez une branche pour votre fonctionnalité:
```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

2. Apportez vos modifications et committez:
```bash
git commit -am 'Ajout d'une nouvelle fonctionnalité'
```

3. Poussez vers la branche:
```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

4. Créez une Pull Request

## Tests
Pour exécuter les tests Django:
```bash
python manage.py test
```

## Déploiement
L'application peut être facilement déployée sur des plateformes comme Heroku, PythonAnywhere ou tout serveur supportant Django.

### Exemple de déploiement sur Heroku
1. Assurez-vous d'avoir le fichier `Procfile` avec le contenu suivant:
```
web: gunicorn yourproject.wsgi
```

2. Installez les dépendances supplémentaires:
```bash
pip install gunicorn dj-database-url whitenoise
```

3. Suivez les instructions de déploiement Heroku standard

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Contact
Pour toute question ou suggestion, veuillez contacter:
- GitHub: [neussi](https://github.com/neussi)

## Remerciements
- R.A. Fisher pour le jeu de données Iris original
- La communauté Django pour le framework et la documentation
- Les contributeurs de scikit-learn pour les outils de machine learning