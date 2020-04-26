install:
	poetry install

run:
	poetry run linked_list

build:
	rm -rf dist/
	poetry build

lint:
	poetry run flake8 data_structures tests

test:
	poetry run pytest -vv

test_linked_list:
	poetry run pytest -vv tests/test_linked_list.py -s

test_doubly_linked_list:
	poetry run pytest -vv tests/test_doubly_linked_list.py -s
