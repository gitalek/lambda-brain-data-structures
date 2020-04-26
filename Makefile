install:
	poetry install

run:
	poetry run linked_list

build:
	rm -rf dist/
	poetry build

lint:
	poetry run flake8 data_structures tests

test_all:
	poetry run pytest -vv

test_linked_list:
	poetry run pytest -vv linked_list tests -s

test_doubly_linked_list:
	poetry run pytest -vv doubly_linked_list tests -s
