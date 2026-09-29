set dotenv-load
set shell := ["bash", "-uc"]

## Variables initialized from env
host_url := env("HOST_URL", "django.localhost")
host_port := env("HOST_PORT", "8000")

## Recipes

# List the available recipes
default:
    @just --list

# Pass a django command
[group('Django')]
django +command:
    uv run python manage.py {{command}}

# Collect static files
[group('Django')]
collectstatic:
    just django collectstatic --noinput

# Create a superuser
[group('Django')]
createsuperuser:
    just django createsuperuser

alias mm:= makemigrations
# Create missing migrations
[group('Django')]
makemigrations app="":
    just django makemigrations {{app}}

alias mi := migrate
# Run existing migrations
[group('Django')]
migrate app="" version="":
    just django migrate {{app}} {{version}}

# Create and run migrations
[group('Django')]
mmi:
    just makemigrations
    just migrate

alias run := runserver
# Run the development server
[group('Django')]
runserver host_url=host_url host_port=host_port:
    just django runserver {{host_url}}:{{host_port}}

# Open a Django shell
[group('Django')]
shell:
    just django shell

# Check test coverage
[group('Tests')]
coverage app="":
    uv run coverage run --source='.' manage.py test {{app}}
    uv run coverage html
    firefox htmlcov/index.html

# Run the unit tests
[group('Tests')]
test app="":
    just django test {{app}}

# Run the Django system check framework
[group('Code audit')]
check +apps="":
    just django check {{apps}}

# Run a global pre-commit check
[group('Code audit')]
quality:
    uv run pre-commit run --all-files

# Check that all imported packages are declared as dependencies (and vice versa)
[group('Code audit')]
deps-check:
    uv run deptry .

# Check dependency licenses for disallowed (e.g. GPL) licenses
[group('Code audit')]
licenses-check:
    uv run pip-licenses

# Generate a secret key
[group('Utils')]
generate_secret_key:
    uv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

# Upgrade versions of dependencies
[group('Utils')]
upgrade:
    uv lock --upgrade
    uv run pre-commit autoupdate
