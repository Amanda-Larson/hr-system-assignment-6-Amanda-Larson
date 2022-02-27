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

# ---DATA--- #
HP_HR = 'HP_HR_Records.csv'
header = ['employee_id', 'name', 'address', 'ssn', 'dob', 'job_title', 'start_date', 'end_date']
table = []
new_employee = 'new_employee.csv'
new_questions = []


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
        print(f'{"============ Human Resources File: Current Employees: ============":^95}')
        print()
        print(f'{header[0]:<15}{header[1]:<20}{header[5]:<50}{header[6]:>12}')
        for row in table:
            if row['end_date'] == '':
                print(f'{row["employee_id"]:<15}{row["name"]:<20}{row["job_title"]:<50}{row["start_date"]:>12}')
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

        for row in table:
            end_date = datetime.datetime.strptime(row['end_date'], '%m/%d/%Y')
            if end_date >= time_since:
                print(f'{"============ Human Resources File: Employees Who Have Left Recently: ============":^95}')
                print()
                print(f'{header[0]:<15}{header[1]:<20}{header[5]:<50}{header[6]:>12}')
                print(f'{row["employee_id"]:<15}{row["name"]:<20}{row["job_title"]:<40}{row["start_date"]:>12}{row["end_date"]:>12}')
        print(f'{"=" * 75:^95}\n')


class new_employee:
    """Class to get user input/add for new employee information to the list of employeess.

    Args: None

    Returns:
        A new questions

    """

    def employee_name():
        name = input('Enter employee\'s first and last name: ')
        return name

    def employee_address():
        address = input('Enter employee\'s address: ')
        return address

    def employee_ssn():
        ssn = input('Enter employee\'s ssn: ')
        return ssn

    def employee_dob():
        dob = input('Enter employee\'s dob: ')
        return dob

    def employee_job():
        job_title = input('Enter employee\'s job title: ')
        return job_title

    def employee_start():
        start_date = input('Enter employee\'s start date: ')
        return start_date


