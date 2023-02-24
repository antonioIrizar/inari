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
	@flake8

ci.test:
	@pytest
