# Variables
PYTHON := python3
VENV := venv
DOCKER_COMPOSE = docker-compose
COMPOSE_FILE = docker-compose.yml
API_SERVICE := api  # Name of your API service in docker-compose.yml

.PHONY: help setup clean run test up down logs migrate

help:
	@echo "Available commands:"
	@echo "  make setup   - Create and activate the virtual environment, install dependencies"
	@echo "  make test    - Run tests using pytest"
	@echo "  make clean   - Remove the virtual environment and __pycache__ files"
	@echo "  make up      - Build and start Docker containers"
	@echo "  make down    - Stop and remove Docker containers"
	@echo "  make logs    - Tail the logs of the Docker containers"
	@echo "  make migrate - Apply database migrations in the Docker 'api' service"

$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

setup: $(VENV)/bin/activate

test:
	$(VENV)/bin/pytest

clean:
	rm -rf $(VENV) **/__pycache__ **/*.pyc

up:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) up --build -d

down:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down --volumes --remove-orphans

logs:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) logs -f

migrate:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) exec $(API_SERVICE) python src/cmd/api/manage.py migrate
