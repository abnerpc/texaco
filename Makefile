clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

.env:
	@cp contrib/dotenv .env

run: .env clean
	@python run.py

test: clean
	@py.test --pdb

requirements:
	@pip install -r requirements.pip

requirements-dev:
	@pip install -r requirements/dev.pip

.PHONY: requirements test