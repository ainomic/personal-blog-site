# Personal Blog site

Personal blog site using Python + Django framework

## Setup dev environment

1. Create virtual environment: `conda create -n personal-blog -y python=3.10`
1. Activate virtual environment: `conda activate personal-blog`
1. Install dependencies: `pip install -r requirements.txt`
1. To get started with the project run command: `django-admin startproject "personal_blog"`
1. Then change directory to the "personal_blog" folder
1. Run command to create an app: `python manage.py startapp "ainomic_blog"`

## Run website application

1. Make migrations: `python manage.py makemigrations`
1. Apply migrations: `python manage.py migrate`
2. Run the development server: `python manage.py runserver`
3. Access the website at `http://localhost:8000` in your web browser.

## Usage

1. Sign up for an account if you're a new user, or log in with your existing credentials.
2. Navigate to the homepage to view a list of blog post titles.
3. Click on a title to read the full blog post.

## Create New Blog

1. To create a new blog post, click on the "Create" button.
2. Fill out the form with the necessary details, such as title, and content.
3. Click the "Submit" button to add the new blog post.

## Update Blog

1. Upon accessing the homepage, you'll see a list of existing blog posts.
2. Click on the "Edit" button of the blog post you wish to update.
3. You'll be directed to a page where you can view the blog post content and update it.
4. Edit the content of the blog post as desired.
5. Click the "Submit" button to update the blog post.
6. The changes will be reflected on the website, and users will see the updated content when they view the blog post.

## Delete Blog

1. Click the "Delete" button.
2. Confirm the deletion when prompted.
3. The blog post will be removed from the website, and users will no longer see it listed on the homepage.
