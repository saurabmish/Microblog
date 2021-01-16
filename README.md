[![Maintainability](https://api.codeclimate.com/v1/badges/7d564f3664c8293aa157/maintainability)](https://codeclimate.com/github/saurabmish/Microblog/maintainability)

# Microblog

Full stack web development using Django framework

Website is live [here][1]

## Setup

+ Navigate to an empty directory and clone this repository

  ```
  git init
  git clone https://github.com/saurabmish/Microblog.git
  ```

+ Create a Python 3 virtual environment:

  `python3 -m venv django-proj`

+ Activate newly created virtual environment:

  `source django-proj/bin/activate`

+ Update pip package manager:

  `pip install --upgrade pip`

+ Navigate to project's root directory and install all dependencies:

  ```
  cd Microblog
  pip install --requirement requirements.txt
  ```

## Local Execution

+ Start Postgres service:

  `pg_ctl -D /usr/local/var/postgres start`

+ Run django web server (all applications part of this project are executed):

  `python manage.py runserver`

+ Visit the below URL on the browser and check application functionality:

  `http://127.0.0.1:8000`

+ Once done:

    1. Stop the web server with `Ctrl+c`
    2. stop Postgres with `pg_ctl -D /usr/local/var/postgres stop`


[1]: https://djangomicroblog.herokuapp.com/
