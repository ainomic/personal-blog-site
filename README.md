# Personal Blog site

Personal blog site using Python + Django framework

## Setup dev environment

1. To get started with the project run command: `django-admin startproject "personal_blog"`
1. Then change directory to the "personal_blog" folder
1. Run command to create an app: `python manage.py startapp "ainomic_blog"`

## User Authentication

1. Make migrations: `python manage.py makemigrations`
1. Apply migrations: `python manage.py migrate`
2. Run the development server: `python manage.py runserver`
3. Access the website at `http://localhost:8000` in your web browser.

## Usage

1. Sign up for an account if you're a new user, or log in with your existing credentials.
2. Navigate to the homepage to view a list of blog post titles.
3. Click on a title to read the full blog post.
