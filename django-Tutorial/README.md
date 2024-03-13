# Django Begginer Course
I've introduced a Django module to explore the fundamentals of Django development. This module will cover essential aspects that are listed below:
  - Introduction to Django: Overview and benefits of Django framework.
  - Setting Up: Installing Python and Django. Creating a virtual environment.
  - Project and Apps: Creating a Django project. Understanding apps and creating them.
  - Configuration: Configuring settings.py. Database settings and middleware.
  - Models and Migrations: Defining models. Generating and applying migrations.
  - Admin Interface: Enabling and customizing admin. Creating superusers.
  - Views and URLs: Creating views and mapping URLs.
  - Templates: Using Django templates.
  - Static Files and Media: Managing static files and user-uploaded media.
  - Forms and Form Handling: Creating and handling HTML forms.
  - Authentication and Authorization: Implementing user authentication and permissions.
  - Error Handling and Debugging: Handling errors and debugging techniques.
  - Deployment: Deploying Django applications.
  - Advanced Topics (Optional): Additional features and integrations. Exploring Django REST Framework.

## Development tools
- IDE - We are using Visual Studio Code but you are more than welcome to use any IDE that support python/django (Notepad++, Atom, PyCharm, etc..). If you are using VSC, go to the marketplace and install the extension prettier. It will maintain our code format throught the django development.

## Install

To get started with Django, ensure you have the following installed:

- Python 3.11.5: Check your Python version with python --version.
- Django 5.0.3: Install Django using python -m pip install Django and verify the version with django-admin --version.
- Optionally, install virtualenv with pip install virtualenv to create a virtual environment.
  - Create a virtual environment named django-env: virtualenv django-env.
  - Activate the virtual environment: django-env\scripts\activate.
Once you created that env you may install Django is.

- Use django-admin startproject devsearch to create a new project named "devsearch".
- Run the server with python manage.py runserver and navigate to the provided URL to view your application.

To learn more about django project structure visit https://django-project-skeleton.readthedocs.io/en/latest/structure.html.

- To create your first app use the command 'python manage.py startapp --nameOfTheApp'



