# ------------------------------------------#
# Title: InputOutput.py
# Desc: assignment 06
# Change Log: (Who, When, What)
# ALarson, 2022-02-25, Created file, started assignment
# ALarson,
# ------------------------------------------#

# if __name__ == '__main__':
#    raise Exception ('This file is not meant to run by itself.')

import pyinputplus as pip
import Files
import csv
import datetime
import re

# ---DATA--- #
HP_HR = 'HP_HR_Records.csv'
header = ['employee_id', 'name', 'address', 'ssn', 'dob', 'job_title', 'start_date', 'end_date']
table = []
new_employee = 'new_employee.csv'
new_questions = []
regex = re.compile("^(?!666|000|9\\d{2})\\d{4}-(?!00)\\d{2}-(?!0{4})\\d{4}$")


# ---I/O--- #
class Menu:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print()  # spacing
        print('HUMAN RESOURCES PROGRAM'.center(38))
        print('------Menu------'.center(38))
        print('\n[1] Load HR Records From File\n[2] Save Records to File\n[3] Add A New Employee')
        print(
            '[4] Generate Current Employee Report\n[5] Generate Employee Report for Recently Unemployed\n[6] Upcoming Annual Review Reminders\n[7] Quit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (int): an integer of the users input out of the choices 1, 2, 3, 4, 5, or 6

        """
        try:
            choice = ''
            while choice not in [1, 2, 3, 4, 5, 6, 7]:
                choice = pip.inputNum(
                    'Which operation would you like to perform?\nPlease choose a number from the menu [1-7]: ', min=1,
                    max=7)
            print()  # Add extra space for layout
            return int(choice)
        except TypeError:
            print('Text characters aren\'t allowed, please choose a number from the menu choices above.')


class Reports:
    @staticmethod
    def show_current(table):
        """Displays current employee information

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        print(f'{"============ Human Resources File: Current Employees ============":^95}')
        print()
        print(
            f'{header[0].replace("_", " ").title():<15}{header[1].replace("_", " ").title():<20}{header[5].replace("_", " ").title():<30}{header[6].replace("_", " ").title():>12}')
        for row in table:
            if row['end_date'] == '':
                print(f'{row["employee_id"]:<15}{row["name"]:<20}{row["job_title"]:<30}{row["start_date"]:>12}')
        print(f'{"=" * 75:^95}')

    @staticmethod
    def show_unemployed(table):
        """Displays report for employees who recently (within 31 days) left

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """

        today = datetime.datetime.now()
        left_day = datetime.timedelta(days=31)
        time_since = today - left_day
        print(f'{"============ Human Resources File: Employees Who Have Left Recently ============":^95}')
        print()
        print(
            f'{header[0].replace("_", " ").title():<15}{header[1].replace("_", " ").title():<20}{header[5].replace("_", " ").title():<30}{header[6].replace("_", " ").title():>12}{header[7].replace("_", " ").title():>12}')
        for row in table:
            if row['end_date'] != '':
                end_date = datetime.datetime.strptime(row['end_date'], '%m/%d/%Y')
                if end_date >= time_since:
                    print(
                        f'{row["employee_id"]:<15}{row["name"]:<20}{row["job_title"]:<30}{row["start_date"]:>12}{row["end_date"]:>12}')
        print(f'{"=" * 75:^95}\n')

    @staticmethod
    def show_reviews(table):
        """Displays upcoming employee reviews. These are for employees who's work anniversary are within 90 days.

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.
        """
        today = datetime.datetime.now()
        review_time = datetime.timedelta(days=90)  # days until review
        review_date = today + review_time

        print(review_date)
        print(f'{"============ Human Resources File: Upcoming Employee Reviews ============":^95}')
        print()
        print(
            f'{header[0].replace("_", " ").title():<15}{header[1].replace("_", " ").title():<20}{header[5].replace("_", " ").title():<50}{header[6].replace("_", " ").title():>12}')
        for row in table:
            conv_date = datetime.datetime.strptime(row['start_date'], '%m/%d/%Y')
            today = datetime.datetime.now()
            mod_date = datetime.datetime(today.year, conv_date.month, conv_date.day)
            if today < mod_date < review_date:
                print(f'{row["employee_id"]:<15}{row["name"]:<20}{row["job_title"]:<50}{row["start_date"]:>12}')
        print(f'{"=" * 75:^95}')


class new_employee:
    """Class to get user input/add for new employee information to the list of employeess.

    Args: None

    Returns:
        A new questions

    """

    @staticmethod
    def employee_name():
        name = input('Enter employee\'s first and last name: ')
        return name.title()

    @staticmethod
    def employee_address():
        address = input('Enter employee\'s address: ')
        return address.title()

    @staticmethod
    def employee_ssn():
        ssn = input('Enter employee\'s ssn: ')
        while not (re.fullmatch(regex, ssn)):
            print("Invalid ssn format - please try again.")
            ssn = input('Enter employee\'s ssn: ')
        return ssn

    @staticmethod
    def employee_dob():

        while True:
            dob_input = input('Enter employee\'s dob (MM/DD/YYYY): ')
            try:
                dob = datetime.datetime.strptime(dob_input, "%m/%d/%Y")
                return dob
            except ValueError:
                print("Error: must be in MM/DD/YYYY format, please try again.")

    @staticmethod
    def employee_job():
        job_title = input('Enter employee\'s job title: ')
        return job_title

    @staticmethod
    def employee_start():
        month = None
        day = None
        year = None
        while True:
            start = input('Enter employee\'s start date (MM/DD/YYYY): ')
            try:
                start_date1 = datetime.datetime.strptime(start, "%m/%d/%Y")
                print(start_date1)
                start_date = datetime.date.strftime(start_date1, "%m/%d/%Y")
                print(start_date)
                return start_date
            except ValueError:
                print("Error: must be in MM/DD/YYYY format, please try again.")

    @staticmethod
    def employee_end():
        end_date = ''
        return end_date
