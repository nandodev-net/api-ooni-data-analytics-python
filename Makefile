PACKAGE=api_ooni_data_analytics
PROJECT=api-ooni-data-analytics
SOURCES=./$(PACKAGE)
BLACK_OPTS=--exclude templates ${SOURCES}
REPO_NAME=api-ooni-data-analytics-python
PACKAGE_NAME=api_ooni_data_analytics

.PHONY: requirements clean test-app test-quality format

requirements: ## install development environment requirements
	pip install -r requirements.txt

clean: ## delete most git-ignored files
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -fr build/
	rm -fr dist/

test-app: ## run the app test suite
	pytest $(SOURCES)

test-quality: ## runs the code style tools diagnostic
	pylint ${SOURCES}
	black --check --diff $(BLACK_OPTS)
	isort --check-only --diff $(SOURCES)
	pydocstyle ${SOURCES}

format: ## format the project style
	black $(BLACK_OPTS)
	isort $(SOURCES)
