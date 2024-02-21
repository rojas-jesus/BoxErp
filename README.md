# Overview

BoxErp is a simple ERP web application. Developed in 2022, it offers a range of functionalities to manage various aspects of a company, all in a simple and easy-to-use interface. Its adaptable design ensures smooth operation on a variety of devices, from desktops to smartphones.

# Features

• Category Management

• Product Management

• Client Management

• Sales Management

• Authentication System

• Authorization System

• Handling of Deleted Records

• Audit Section

Note: While the BoxErp web application includes comprehensive features for managing various aspects of a business, does not include a purchasing management module. 

# Preview 

![products](https://github.com/rojas-jesus/BoxErp/assets/148916557/c1066088-b040-4189-938e-3e527c444f36)

![categories](https://github.com/rojas-jesus/BoxErp/assets/148916557/7600697f-f74b-42a9-8721-49ec3f2e435b)

![BoxErp1](https://github.com/rojas-jesus/BoxErp/assets/148916557/99e201dc-e82c-4527-9af0-1c39d86cc176)

![BoxErp2](https://github.com/rojas-jesus/BoxErp/assets/148916557/d3a7876f-4878-4a33-8fb5-39d9da3063a9)


• High-quality preview

https://github.com/rojas-jesus/BoxErp/assets/148916557/612b0aa4-0238-412b-b970-d30dc5ff8fb6




# Main Technologies Used

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
