# Command-Line Arguments

This section contains some of the most commonly used Django command-line arguments.

+ Create a project:

  `django-admin startproject PROJECT_NAME`

+ Create an application:

  **NOTE:** There can be multiple applications associated with a project. To create an application, navigate to the project's root directory - `PROJECT_NAME`

  `python manage.py startapp app`

+ Run django web server:

  **NOTE:**: All applications part of the project are executed

  `python manage.py runserver`
