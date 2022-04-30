.PHONY:  help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-30s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help: ## help
	@poetry run python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

pre-requirements: ## install poetry
	pip install --user poetry

install: ## install packages
	poetry install

flake8: ## lint
	poetry run flake8 user_service

mypy: ## code checker
	poetry run mypy user_service

test: ## test
	docker-compose run --rm user-box-test bash -c "python -m pytest tests"

test.verbose: ## test.verbose
	docker-compose run --rm user-box-test bash -c "python -m pytest tests -v --pdb --pdbcls=IPython.terminal.debugger:Pdb"

db.init:
	docker-compose run --rm user-box bash -c "user-cli db init"

db.makemigrations:
	docker-compose run --rm user-box bash -c "user-cli db makemigrations"

db.migrate:
	docker-compose run --rm user-box bash -c "user-cli db migrate"

optimise-imports: ## optimise imports
	poetry run autoimport user_service
	poetry run isort user_service
	poetry run autoimport tests
	poetry run isort tests

format: optimise-imports ## format
	poetry run black user_service
	poetry run black tests

start: ## start
	docker-compose run --rm --service-ports user-service

docker.build: ## > user
	docker build -t 'user-service:latest' -f 'Dockerfile' .

docker.build-no-cache: ## > user
	docker build -t 'user-service:latest' -f 'Dockerfile' --no-cache .

docker.publish: ## > build and publish user image
	docker pull user-service:latest || true
	docker build -t 'user-service:latest' -f 'Dockerfile' . --cache-from=user-service:latest
	docker push user-service:latest || true
