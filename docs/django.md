# Command-Line Arguments

This document contains some of the most commonly used Django command-line arguments.

+ Create a project:

  `django-admin startproject PROJECT_NAME`

+ Create an application:

  **NOTE:** There can be multiple applications associated with a project. To create an application, navigate to the project's root directory - `PROJECT_NAME`

  `python manage.py startapp APPLICATION_NAME`

+ Run django web server:

  **NOTE:**: All applications part of the project are executed

  `python manage.py runserver`

+ Do a *dry run* to see if there's any existing tables in the database:

  **NOTE:** This will add default tables using the specifications in the `DATABASE` section of `settings.py`. Additionally, specifications from the application's `models.py` will also be applied

  `python manage.py makemigrations`

+ Stage changes:

  `python manage.py sqlmigrate APPLICATION_NAME MIGRATION_NUMBER`

+ Create project tables (based on staged changes):

  `python manage.py migrate`

+ Create project's admin user (verify this by logging into Django's admin console on http://localhost:8000/admin):

  `python manage.py createsuperuser`

+ Run python interactive shell:

  `python manage.py shell`
