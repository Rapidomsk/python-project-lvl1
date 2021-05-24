install:
	poetry install
brain-games:
	poetry run brain-games
	poetry run brain-even
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
make lint:
	poetry run wemake-python-styleguide brain_games
brain_even:
	poetry run brain-even
brain_calc:
	poetry run brain-calc
