# Studora — Plateforme de gestion de projets étudiants

Studora est une application web permettant aux enseignants de publier des sujets de projets
et aux étudiants de postuler. Elle couvre la gestion des rôles, le CRUD des projets,
les candidatures et un tableau de bord par profil.

## Stack technique

- Backend : Django 5 + PostgreSQL
- Frontend : Django Templates + Bootstrap 5 + Bootstrap Icons
- Conteneurisation : Docker + Docker Compose
- Formulaires : django-crispy-forms + crispy-bootstrap5

## Architecture
studora/
├── config/              — Configuration Django (settings, urls, wsgi)
├── accounts/            — Authentification et gestion des utilisateurs
├── projects/            — CRUD des projets (enseignants)
├── applications/        — Candidatures (étudiants)
├── templates/           — Templates HTML par application
├── static/              — Fichiers statiques (CSS, JS)
├── seed.py              — Données de test
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── requirements.txt

## Prérequis

- Docker
- Docker Compose

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/TON_USERNAME/studora.git
cd studora
```

### 2. Configurer les variables d'environnement

```bash
cp .env.example .env
```

Éditer `.env` avec vos valeurs.

### 3. Démarrer l'application

```bash
make build
```

L'application est accessible sur `http://localhost:8000`.

### 4. Charger les données de test

```bash
make seed
```

## Variables d'environnement

| Variable       | Description                        | Exemple                        |
|----------------|------------------------------------|--------------------------------|
| `SECRET_KEY`   | Clé secrète Django                 | `django-insecure-xxxxx`        |
| `DEBUG`        | Mode debug                         | `True` / `False`               |
| `ALLOWED_HOSTS`| Hôtes autorisés                    | `localhost,127.0.0.1`          |
| `DB_NAME`      | Nom de la base de données          | `studora_db`                  |
| `DB_USER`      | Utilisateur PostgreSQL             | `studora_user`                  |
| `DB_PASSWORD`  | Mot de passe PostgreSQL            | `tonmotdepasse`                |
| `DB_HOST`      | Hôte de la base de données         | `db` (Docker) / `localhost`    |
| `DB_PORT`      | Port PostgreSQL                    | `5432`                         |

## Commandes

```bash
make build           # Construire et démarrer
make up              # Démarrer
make down            # Stopper
make restart         # Redémarrer
make logs            # Logs en temps réel
make shell           # Shell Django
make migrate         # Migrations
make seed            # Données de test
make createsuperuser # Créer un admin
make test            # Tests
make lint            # Vérification PEP 8
make clean           # Tout supprimer
```

## Comptes de test

| Rôle        | Email                | Mot de passe  |
|-------------|----------------------|---------------|
| Enseignant  | teacher@univ.fr      | password123   |
| Enseignant  | teacher2@univ.fr     | password123   |
| Étudiant    | student@univ.fr      | password123   |
| Étudiant    | student2@univ.fr     | password123   |
| Étudiant    | student3@univ.fr     | password123   |

## Fonctionnalités

**Enseignant**
- Créer, modifier, supprimer des projets
- Consulter et traiter les candidatures (accepter / refuser)
- Tableau de bord avec statistiques

**Étudiant**
- Parcourir et filtrer les projets ouverts
- Postuler avec une lettre de motivation
- Suivre le statut de ses candidatures

**Commun**
- Authentification par email
- Rôles distincts avec accès restreints
- Interface responsive

## Licence

MIT