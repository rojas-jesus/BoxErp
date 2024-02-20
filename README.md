# Overview:

The BoxErp web application is a simple but powerful business management solution. Developed in 2022, it offers a range of functionalities to manage various aspects of a company, all in a simple and easy-to-use interface. Its adaptable design ensures smooth operation on a variety of devices, from desktops to smartphones.

# Features:

• Category Management
• Product Management
• Client Management
• Sales Management
• Authentication System
• Authorization System
• Handling of Deleted Records
• Audit Section

# Main Technologies Used:

• Django
• Bootstrap
• JavaScript

# Getting Started
First, clone the repository from Github. Then, navigate to the project directory and activate the virtual environment.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Apply the migrations:

    $ python manage.py migrate

Create a superuser:

    $ python manage.py createsuperuser

Run the development server:

    $ python manage.py runserver

# Maintenance Status
This repository is no longer actively maintained. The project is in a stable state.

# Testing
Functional and non-functional tests have been conducted to ensure the quality and reliability of the application.

Note: The unit test suite is limited and only covers a small portion of the core app models and views. Despite this limitation, the application is functioning correctly.

All the tests that are in the tests folder and you can run them locally with:

    $ python manage.py test tests
