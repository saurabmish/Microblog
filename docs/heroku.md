# Setup

+ Create a Heroku account [here][1]:

+ Install CLI

  `brew tap heroku/brew && brew install heroku`

  OR

  `sudo snap install --classic heroku`

+ Install Heroku CLI's autocomplete

  `heroku autocomplete`

+ Enable autocomplete

  (press `y` for the option "Ignore insecure directories and continue")

  `printf "$(heroku autocomplete:script zsh)" >> ~/.config/zsh/.zshrc; source ~/.config/zsh/.zshrc`

+ Login to account with CLI

  (A link will open a browser asking for credentials. After credentials are validated, a "Logged In" message will appear)

  `heroku login`

# Project Configuration

+ At the project root (`.git/` is located here), create a heroku app

  `heroku create djangomicroblog`

+ Publish code to the Heroku platform

  `git push heroku master`

+ View existing resources associated with the application on Heroku

  `heroku addons`

+ View database details

  `heroku pg`

+ Migrate applications tables to database

  `heroku run python manage.py migrate`

+ Access remote Heroku server (*Dynos*)

  `heroku run bash`

+ Create super user for Django's console

  `python manage.py createsuperuser`

+ Run application

  (**NOTE:** Ensure the below configurations are set and committed to GitHub **and** heroku:
    1. `STATIC_ROOT` is set in the project's `settings.py`
    2. `django_heroku` is set for auto configuration in the project's `settings.py`
    3. `Procfile` is present in the project's root
    4. Super user is created on Heroku
  )

  `heroku open`

[1]: https://signup.heroku.com/login
