# Setup and Configuration

+ Install PostgreSQL:

  `brew install postgresql`

+ View installed location:

  `which postgres`

+ Check if postgres service is running:

  `pg_ctl -D /usr/local/var/postgres status`

+ Manually start (or stop) services:

  `pg_ctl -D /usr/local/var/postgres start (or stop)`

  **NOTE:** Postgres can also be started automatically:

  `brew services start postgresql`

+ Create role postgres (service needs to be running):

  `/usr/local/opt/postgres/bin/createuser -s postgres`

+ Login to psql as root user (postgres):

  `psql -U postgres`

  OR

  `psql -U postgres -h localhost`

+ Create new user:

  `CREATE USER microblog_admin WITH PASSWORD 'admin123';`

+ Create database:

  `CREATE DATABASE microblogdb;`

+ Grant access on database to user:

  `GRANT ALL PRIVILEGES ON DATABASE microblogdb TO microblog_admin;`

+ Verify new user (this will list all roles of existing postgres users):

  `\du`

+ Verify database (this will give details like owner, privileges, etc.):

  `\l`

+ Connect to *new* database with *new* user:

  `\c microblogdb microblog_admin`

+ Exit psql:

  `\q`

+ Check the listen addresses and port in postgresql.conf:

  `egrep 'listen|port' /usr/local/var/postgres/postgresql.conf`

----

# Project Integration

+ Install PostgreSQL database adapter `psycopg2` inside the project's virtual environment:

  `pip install psycopg2`

+ Modify `DATABASES` section of the project's `settings.py` to:

  ```
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': 'microblogdb',
      'USER': 'microblog_admin',
      'PASSWORD': 'admin123',
      'HOST': 'localhost',
      'PORT': '5432',
  }
  ```

+ To be able to run test cases, the user must have permission to create a database

  `$ psql -U postgres -h localhost`

  `postgres=# ALTER USER microblog_admin CREATEDB;`

+ View (dry run) if there are any existing tables in the database:

  `python manage.py makemigrations`

+ Create project's tables:

  `python manage.py migrate`

+ Create project's admin user:

  `python manage.py createsuperuser`

+ Enter the details (username, email, and password) and then run the project:

  `python manage.py runserver`

+ Navigate to the Django's admin panel on the browser:

  `http://127.0.0.1:8000/admin/auth/user/`

+ Create a new user for this application (by specifying details like above)

----

# Verification

+ Execute a Python shell using Django:

  `python manage.py shell`

+ Commands

  ```
  >>> # import users associated with the project
  >>> from django.contrib.auth.models import User
  >>>
  >>> # return all users (objects are of type "QuerySet")
  >>> User.objects.all()
  >>>
  >>> # get the first (or last) user
  >>> User.objects.first()
  >>>
  >>> # filter users by field
  >>> User.objects.filter(username='saurabh')
  >>>
  >>> # return filtered user of type User (not QuerySet)
  >>> User.objects.filter(username='saurabh').first()
  >>>
  >>> # get a user's primary key (pk) (or identification (id))
  >>> User.objects.filter(username='saurabh').first().pk
  >>>
  >>> # get a user having specific primary key (pk) (or identification (id))
  >>> User.objects.get(id=1)
  ```
