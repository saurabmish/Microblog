[![Maintainability](https://api.codeclimate.com/v1/badges/7d564f3664c8293aa157/maintainability)](https://codeclimate.com/github/saurabmish/Microblog/maintainability)

# Microblog

Full stack web development using Django framework

## Setup

### Project

+ Navigate to an empty directory

+ Create a Python 3 virtual environment:

  `python3 -m venv django-proj`

+ Activate newly created virtual environment:

  `source django-proj/bin/activate`

+ Update pip package manager:

  `pip install --upgrade pip`

+ Install `django`:

  `pip install django`

+ Check `django` version:

  `python -m django --version`

+ Create a new Django project:

  `django-admin startproject microblog`

+ Navigate to project's root:

  `cd microblog`

+ Run django web server:

  `python manage.py runserver`

+ Go to the below URL on the browser to verify Django server:

  `http://127.0.0.1:8000`

+ Stop the web server `Ctrl+c`

### Application

+ Create application directory:

  `python manage.py startapp app`

+ Define `views` and `urls` and create a directory `templates` for static content

+ Update the `INSTALLED_APPS` of project settings

+ Run project (and all apps inside):

  `python manage.py runserver`
