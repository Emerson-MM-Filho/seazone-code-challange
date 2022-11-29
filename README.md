# Seazone Code Challange
[See challenge description](challenge_description.pdf)

---

## Pre-requisitos
* Python 3.8.9 installed.
* [PostgreSQL server running](https://www.postgresql.org/download/) (or Docker).
* Create ```.env``` file following ```.env.example``` file.

---

## Setup:
1 - Create and activate virtual env:
```shell
# create venv
python venv .venv

# activate venv
.venv/Scripts/activate.ps1
```

2 - Install dependencies:
```shell
pip install -r requirements.txt
```

3 - Update database with default data:
```shell
python .\manage.py load_default_data
```

---

## Run:
```shell
python .\manage.py runserver
```

## Tests:
```shell
python .\manage.py test
```
