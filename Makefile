.PHONY: test

deps:
	pip install -r requirements.txt

lint:
	flake8 tests

test:
	pytest ./tests -v