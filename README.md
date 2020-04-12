# Microsoft Student Partners

This is the unofficial website for the Microsoft Student Partners

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)
![image](https://img.shields.io/badge/code%20style-black-000000.svg)
[![GitHub license](https://img.shields.io/github/license/ramanaditya/Microsoft-Student-Partners.svg?logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ramanaditya/Microsoft-Student-Partners.svg?logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/ramanaditya/Microsoft-Student-Partners.svg?logo=github&color=teal)](https://github.com/ramanaditya/Microsoft-Student-Partners/network/members) 
[![GitHub top language](https://img.shields.io/github/languages/top/ramanaditya/Microsoft-Student-Partners?color=blue&logo=python)](https://github.com/ramanaditya/Microsoft-Student-Partners)

:License: MIT

## Setup

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ramanaditya/Microsoft-Student-Partners?logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/) 
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ramanaditya/Microsoft-Student-Partners?color=bluevoilet&logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/commits/) 
[![GitHub repo size](https://img.shields.io/github/repo-size/ramanaditya/Microsoft-Student-Partners?logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/)

1.  Clone the repository
    ```console
    $ git clone https://github.com/ramanaditya/Microsoft-Student-Partners
    ```

2.  Create a virtual environment using virtualenv or venv.
     ```console
     $ virtualenv -p python3 venv/ 
     $ source venv/bin/activate
     ```

3.  Install python packages
     ```console
     $ pip3 install -r requirements/local.txt
     ```

4.  Install OS dependencies (For linux systems only, others have to install it manually)
    ```console
    $ sudo ./utility/install\_os\_dependencies.sh install
    ```

5.  Makemigrations and migrate
    ```console
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```
    
6.  Run project locally
    ```console
    $ python manage.py runserver --settings=config.settings.local
    ```

## Settings

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

## Basic Commands

### Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

  $ mypy microsoft_student_partners

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with py.test

    ```console
      $ pytest
    ```

### Live reloading and Sass CSS compilation

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

## Celery

This app comes with Celery.

To run a celery worker:

    cd microsoft_student_partners
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

## Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


## Issues

[![GitHub issues](https://img.shields.io/github/issues/ramanaditya/Microsoft-Student-Partners?logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white)](https://github.com/ramanaditya/Microsoft-Student-Partners/pulls) 
[![GitHub last commit](https://img.shields.io/github/last-commit/ramanaditya/Microsoft-Student-Partners?logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/)

> // No Issues now.

**NOTE**: **Feel free to [open issues](https://github.com/ramanaditya/Microsoft-Student-Partners/issues/new/choose)**. Make sure you follow the Issue Template provided.


## Contribution Guidelines

[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/ramanaditya/Microsoft-Student-Partners?logo=git&logoColor=white)](https://github.com/ramanaditya/Microsoft-Student-Partners/compare) 
[![GitHub contributors](https://img.shields.io/github/contributors/ramanaditya/Microsoft-Student-Partners?logo=github)](https://github.com/ramanaditya/Microsoft-Student-Partners/graphs/contributors) 

- Write clear meaningful git commit messages (Do read [this](http://chris.beams.io/posts/git-commit/)).

- Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check [this](https://github.com/blog/1506-closing-issues-via-pull-requests) for more info)

- When you make very very minor changes to a PR of yours (like for example fixing a text in button, minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at [here](https://davidwalsh.name/squash-commits-git))

- When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.

- Please follow the [PR Template](https://github.com/ramanaditya/Microsoft-Student-Partners/blob/master/.github/PULL_REQUEST_TEMPLATE.md) to create the PR.

- Always open PR to `develop` branch.

- Please read our [Code of Conduct](./CODE_OF_CONDUCT.md).

- Refer [this](https://github.com/ramanaditya/Microsoft-Student-Partners/blob/master/CONTRIBUTING.md) for more.


[![with love](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/ramanaditya/Microsoft-Student-Partners/) [![forthebadge](https://forthebadge.com/images/badges/for-you.svg)](https://github.com/ramanaditya/Microsoft-Student-Partners/) [![smile please](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/ramanaditya/Microsoft-Student-Partners/)
