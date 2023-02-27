ci.dependency.install.sys:
	@python -m pip install --upgrade pip
	@pip install poetry
	@poetry config virtualenvs.create false

ci.dependency.check_sync:
	@poetry check

ci.migrate.check:
	@python manage.py makemigrations --check

ci.dependency.install:
	@poetry install

ci.linter:
	@black --check -l 119 .
	@flake8 . --count --exit-zero --max-line-length=119 --statistics

ci.test:
	@pytest
