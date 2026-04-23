.PHONY: help build up down restart logs shell migrate seed createsuperuser test lint clean

help:
	@echo "Commandes disponibles :"
	@echo "  make build          — Construire les images Docker"
	@echo "  make up             — Démarrer les conteneurs"
	@echo "  make down           — Stopper les conteneurs"
	@echo "  make restart        — Redémarrer les conteneurs"
	@echo "  make logs           — Afficher les logs"
	@echo "  make shell          — Ouvrir un shell Django"
	@echo "  make migrate        — Appliquer les migrations"
	@echo "  make seed           — Charger les données de test"
	@echo "  make createsuperuser— Créer un superutilisateur"
	@echo "  make test           — Lancer les tests"
	@echo "  make lint           — Vérifier le code (flake8)"
	@echo "  make clean          — Supprimer les conteneurs et volumes"

build:
	docker compose up --build -d

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down && docker compose up -d

logs:
	docker compose logs -f web

shell:
	docker compose exec web python manage.py shell

migrate:
	docker compose exec web python manage.py migrate

seed:
	docker compose exec web python seed.py

createsuperuser:
	docker compose exec web python manage.py createsuperuser

test:
	docker compose exec web python manage.py test

lint:
	docker compose exec web flake8 . --exclude=venv,migrations

clean:
	docker compose down -v --remove-orphans