install:
	poetry install

run:
	poetry run linked_list

build:
	rm -rf dist/
	poetry build

lint:
	poetry run flake8 linked_list tests

test:
	poetry run pytest -vv linked_list tests -s
