.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

migrations: ## Make Django migrations
	python manage.py makemigrations
	python manage.py migrate

server: ## Start Django server
	python manage.py runserver

superuser: ## Create superuser
	python manage.py createsuperuser

.DEFAULT_GOAL := help
