# Assignment 6

## Time to complete this assignment:

You have two weeks for this assignment.

## Motivation:

With your newly acquired Python skills you have been asked by a friend who 
runs a small business to develop an application to keep track of her employees.

There will be an estimate 40-50 employees at any one time; your friend, as business
owner, will be the sole user of the system. It is fine that it will run as an app
that is launched from the terminal and will use text based input and output.

You are going to develop that system. It will be able to record basic employee 
details, like name, address, Social Security number (SSN), date of birth, job title,
start date and end date. It will store these details in a csv (Comma-separated files,
which you may have used on spreadsheet software) file on disk, from where
it can also load them, so the employee details can be amended. The system must make 
appropriate use of validation for the data entered (check for missing fields, invalid
values, etc.), and must also be able to trap major errors (things that will make your
program crash), at least by reporting a meaningful message.

The system must be able to produce a list of all employees who are currently 
employed, and a list of all employess who have left on the last month. Both 
lists must be sorted by employee id number.

The system needs to be able to display reminders to schedule an annual review 
with an employee 3 months prior to their individual review date. This can just 
be shown on the screen for the purpose of this assignment.

Because this system is used to store data about people it is very important 
that it is tested well, using automated testing techniques.

## Here is what you need to do:

1. Create a menu that gives the user the options to load employees in from a csv, save them into a csv, add a new employee, generate a report of current employees, generate a report of employees who have recently left, and generate a report of annual review reminders.
1. For the first option, loading in employees from a csv, you must ask the user for the location of the csv and load that in. The format of csv will be as follows:
```csv
employee_id,name,address,ssn,date_of_birth,job_title,start_date,end_date
Anubhaw Arya,Seattle,1234567890,1/1/1970,lecturer,1/1/2021,
```
Notice that `end_date` is empty, signifying that the employee still works there. Feel free to add more fields
1. For the second option, saving the employees to a csv, you must ask the user where to save the csv file and save it there. Follow the above format for the file.
1. For the third option, adding a new employee, collect all the data from the user and apply input validation to those fields. If any of those checks fail, reprompt the user for that data. `employee_id` should be generated and be unique across all employees.
1. For the fourth option, generate a report of currently employees currently working for the company. Print it out cleanly via string formatting!
1. For the fifth option, generate a report of employees who have left within the past 31 days. Print it out cleanly via string formatting!
1. For the sixth option, generate a report of annual review reminders. These are for employees who's work anniversary are within 90 days.
1. Including unit testing where this makes the most sense. We want to make sure our program is correct as we incrementally build it out!

## Submission:

Your submission should include the following:

1. All Python (.py) files, including tests, that you developed.
1. A sample csv file with some employee data in it.
1. Any other files required to successfully run your code.
1. You also need to upload your code to Canvas, uploading it as a pull request.
1. In Canvas, add a comment to your submission with a link to your pull request.

Your submission **should not** include your virtual environment.

## Tips

1. Be creative! Use this as an opportunity to reflect on everything you have 
learned so far and apply it to application development.
1. Use your time well, two weeks might seem like a lot, but you will run out of time if you
wait too much to get started. At the end of the first week, you should have the first
*draft* of your project, so that you can devote the second week fixing potential crashes
and adding any missing features.
