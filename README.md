# Welcome to Shift Tally
> A Python Django web app that allows users to track their employees, employee's personal info, and allows employees to record their working hours. 

## Background
I spent most of my twenties working for coffee shops and a few other small businesses.  I noticed that in most of these positions the owner didn't have a good resource for a time clock.  Most of the small businesses I worked at had employees write down their hours in an excel sheet or on a piece of paper and turn it in. I wanted to create an option for small business owners to keep track of hours.

## General App Functionality
The following functionalities are part of Bike Dash:

1. User registration (forked from Steve and Joe - thanks! ;) )
1. User login (forked from Steve and Joe)
1. User logout (forked from Steve and Joe)
1. Employee: add, edit, detail, list
1. Shifts: add, edit, delete, list

## App Flow
This app has 4 goals:
1. Track employee personal data
1. Track employee worked shifts
1. Track employee employment status (active or inactive)
1. Allow employees to clock in and out without needing to register

Typical flow:

1. Create new employees
1. An employee can enter their given pin code into the affordance to clock in or out
1. Check your dashboard to see which active employees are currently clocked in or not
1. Edit employee details
1. Edit/delete employee shifts
1. Mark an employee inactive 

## ERD

![shift tally erd](website/static/ERD-shift-tally.png)

## To Clone
1. Create a directory
1. cd into that directory
1. Clone the repository
1. Start a virtual environment
1. Run pip install django
1. Create migrations python manage.py makemigrations bikes
1. Apply migrations to db python manage.py migrate
1. run python manage.py runserver
1. Open up your browser and navigate to the running server
1. Register, add employee, and now that employee can clock in & out with the pin code you provided

## Created by Samuel Webber
I'm a graduate of [Nashville Software School](http://nashvillesoftwareschool.com/) 
Learn more about me at [samuelwebber.com](http://www.samuelwebber.com/)

