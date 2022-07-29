./manage.py truncate_django_migrations_table

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

./manage.py makemigrations
./manage.py migrate --fake
