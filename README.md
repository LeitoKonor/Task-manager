### Hexlet tests and linter status:
[![Actions Status](https://github.com/LeitoKonor/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/LeitoKonor/python-project-52/actions)
[![Python CI](https://github.com/LeitoKonor/python-project-52/actions/workflows/python.yml/badge.svg)](https://github.com/LeitoKonor/python-project-52/actions/workflows/python.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/d9b18c1b183a10e407b5/maintainability)](https://codeclimate.com/github/LeitoKonor/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d9b18c1b183a10e407b5/test_coverage)](https://codeclimate.com/github/LeitoKonor/python-project-52/test_coverage)

### About The Project

Register, create, delete and edit tasks, labels and statuses, assign executors to tasks. Filter tasks by tags, statuses, and executors, or filter only your created tasks.

### Demonstration:

https://task-manager-6y9z.onrender.com

### Requerements:

- Python >= 3.10.12
- Poetry >= version 1.4.2
- django >= 4.2.4
- python-dotenv >= 1.0.0
- dj-database-url >= 2.1.0
- gunicorn >= 21.2.0
- django-bootstrap4 >= 23.2
- whitenoise >= 6.5.0
- django-extensions >= 3.2.3
- django-filter >= 23.2
- rollbar >= 0.16.3
- psycopg2-binary >= 2.9.7

### Install:

git clone git@github.com:LeitoKonor/python-project-52.git

cd python-project-52

make install

make migrate

make dev