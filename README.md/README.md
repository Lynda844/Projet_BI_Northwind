📌 Présentation du Projet

Ce projet vise à mettre en place un pipeline de données complet (ETL) afin d’analyser les performances commerciales de l’entreprise Northwind. Initialement basé sur Microsoft Access, le projet a été migré vers SQL Server afin de garantir une meilleure stabilité et de simuler un environnement professionnel.

🛠️ Technologies Utilisées

- Base de données : SQL Server (SSMS)
- Langage : Python (Pandas, SQLAlchemy)
- Visualisation : Plotly & Dash
- Environnement : Jupyter Notebook / VS Code

🚀 Architecture du Pipeline

- Extraction : Connexion au serveur SQL via SQLAlchemy et récupération des tables Orders, Customers et Employees.
- Transformation (ETL) :
  - Nettoyage des données (gestion des types, normalisation des textes).
  - Calcul du chiffre d’affaires (CA).
  - Jointures entre les tables pour relier ventes, employés et pays.
- Chargement : Exportation du jeu de données final au format CSV pour l’alimentation du dashboard.
- Visualisation : Création de graphiques interactifs pour le suivi des KPI.

📊 Indicateurs de Performance (KPI)

- Chiffre d’Affaires Total
- Évolution Mensuelle des Ventes
- Top 5 Employés
- Top 5 Clients

▶️ Exécution du projet

1. Cloner le dépôt
2. Créer un environnement virtuel
3. Installer les dépendances :
   pip install -r requirements.txt
4. Configurer la connexion SQL Server
5. Lancer l’application Dash :
   python python_dashboard_app.py