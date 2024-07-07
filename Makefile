.DEFAULT_GOAL := help

ifdef TOXENV
TOX := poetry run tox -e $(TOXENV) -- ## isolate each tox environment if TOXENV is defined
else
TOX := poetry run tox -- ## use default tox environment if TOXENV is not defined
endif

.PHONY: requirements clean test-app test-quality format

PACKAGE=apps
PROJECT=api-ooni-data-analytics
SOURCES=./$(PACKAGE)
BLACK_OPTS=--exclude templates ${SOURCES}
REPO_NAME=api-ooni-data-analytics-python
PACKAGE_NAME=api_ooni_data_analytics

help:
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

requirements: ## install development environment requirements
	pip install -r requirements.txt
	poetry install -v

format: ## format the project style.
	poetry run black $(BLACK_OPTS)
	poetry run isort $(SOURCES)

clean: ## delete most git-ignored files
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -fr build/
	rm -fr dist/

test-actions-app: ## run the app tests with tox (reserved for GHactions or to run with act running 'act pull_request -j run_tests').
	$(TOX) -- $(SOURCES)

test-local-app: ## run the app test suite without tox.
	poetry run pytest $(SOURCES)

test-quality: ## runs the code style tools diagnostic.
	poetry run pylint --rcfile=setup.cfg $(SOURCES)
	poetry run black --check --diff $(BLACK_OPTS)
	poetry run isort --settings-path=setup.cfg --check-only --diff $(SOURCES)
	poetry run pydocstyle --config=setup.cfg $(SOURCES)

test-repo: clean test-quality test-actions-app ## run test for GHactions environment.

test-dev: test-quality test-local-app ## run test for local environment.

run: ## run the Django development server
	poetry run python manage.py runserver
