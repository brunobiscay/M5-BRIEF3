# Projet Python - Streamlit + FastAPI avec supervision/suivi performance inclus

# 🚀 Projet Python - Streamlit + FastAPI + Docker

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Tests](https://img.shields.io/badge/Tests-Pytest-yellow)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)

---

## 📌 Description

Ce projet est une application complète basée sur une architecture **frontend / backend** :

- 🎨 **Frontend** : Streamlit (interface utilisateur)
- ⚙️ **Backend** : FastAPI (API REST)
- 🐳 **Environnement** : Docker & Docker Compose
- 📜 **Logs** : Loguru (fichiers séparés)
- ✅ **Tests** : pytest
- 🔁 **CI/CD** : GitHub Actions
- 📊 **Monitoring** : Prometheus en collecte + Grafana (display)
- 🔔 **Alerting** : superivsion de l'API via Kuma et alerting Discord

👉 L’application permet à l’utilisateur de saisir un entier et d’obtenir son **carré** via une API REST.

De plus ce code permet de  déployer les images automatiquement sur Docker Hub dès qu’un commit est effectué sur la branche main.

Et les docker inclus la supervison/alerting
---

## 🏗️ Architecture du projet


```bash
├── frontend/
│   ├── app.py
│   ├── app.log
│   └── Dockerfile
│
├── backend/
│   ├── main.py
│   ├── main.log
│   ├── Dockerfile
│   ├── modules/
│   │   ├── calcul.py
│   │   └── calcul.log
│   └── tests/
│       └── test_calcul.py
├── monitoring/
│   ├── prometheus.yml
│   └── grafana/
│       ├── provisioning/
│       │   ├── datasources/
│       │   │   └── datasource.yml
│       │   └── dashboards/
│       │       └── dashboard.yml
│
├── docker-compose.yml
├── .env
└── .github/
    └── workflows/
        └── test.yml
```

## ⚙️ Fonctionnalités

✅ API REST avec 3 routes différentes :
- `/` → message de bienvenue  
- `/health` → vérification état API  
- `/calcul` → retourne le carré d’un entier  

✅ Interface simple avec Streamlit  
✅ Validation des données avec Pydantic  
✅ Logs séparés par composant  
✅ Tests unitaires avec pytest  
✅ Conteneurisation complète Docker  

---

## 🐳 Lancer le docker

docker-compose up --build

## 🌐 Accès aux services

| Service | URL | 
|:-------- |:--------:|
| Frontend    | http://localhost:8501|
| Backend    | http://localhost:8000|
| Docs    | http://localhost:8000/docs|
| Prometheus    | http://localhost:9090 |
| Grafana     | http://localhost:3000 |
| Uptime Kuma    | http://localhost:3001 |


## 🧪 Lancer les tests
cd backend
pytest

## 📜 Logs
| Fichier | Description | 
|:-------- |:--------:|
| main.log    | Logs API FastAPI |
| calcul.log   | Logs du module de calcul |
| app.log    | Logs du frontend |

## 🔁 Intégration Continue (CI)
À chaque :

✅ push
✅ pull request

GitHub Actions lance automatiquement : pytest


## Deploiement sur GitHub
### Declencheur
on:
  push:
    branches:
      - main

### Double tag
//version courante et traçabilité

```
latest                      
${{ github.sha }}
```
### Cache Docker
```
cache-from: type=gha
cache-to: type=gha,mode=ma
```

### Lancement du test CI+CD
.github/workflows/test.yml

```
needs: test
```

##  Technologies utilisées

Python 3.10
FastAPI
Streamlit
Pydantic
Loguru
Docker
pytest
GitHub Actions
Docker Hub
Grana
Prometheus
Uptime Kuma