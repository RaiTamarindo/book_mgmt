# Variables
PYTHON := python3
VENV := venv
DOCKER_COMPOSE = docker-compose
COMPOSE_FILE = docker-compose.yml
API_SERVICE := api  # Name of your API service in docker-compose.yml

.PHONY: help setup clean run test up down logs migrate

help:
	@echo "Available commands:"
	@echo "  make setup      - Create and activate the virtual environment, install dependencies"
	@echo "  make test       - Run tests using pytest"
	@echo "  make clean      - Remove the virtual environment and __pycache__ files"
	@echo "  make run        - Build and start Docker containers"
	@echo "  make stop       - Stop and remove Docker containers"
	@echo "  make logs       - Tail the logs of the Docker containers"
	@echo "  make migrations - Generate database migrations from the models

$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

setup: $(VENV)/bin/activate

test:
	$(VENV)/bin/pytest

clean:
	rm -rf $(VENV) **/__pycache__ **/*.pyc

run:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) up --build -d

stop:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) down --volumes --remove-orphans

test:
	$(DOCKER_COMPOSE) -f docker-compose.test.yml up --build

logs:
	$(DOCKER_COMPOSE) -f $(COMPOSE_FILE) logs -f

migrations:
	$(VENV)/bin/python manage.py makemigrations
