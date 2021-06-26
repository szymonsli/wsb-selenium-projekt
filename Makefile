.PHONY: test

deps:
	pip install -r requirements.txt

lint:
	flake8 tests pages

test:
	pytest ./tests -v