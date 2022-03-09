# ------------------------------------------#
# Title: Files.py
# Desc: assignment 06
# Change Log: (Who, When, What)
# ALarson, 2022-02-25, Created file, started assignment
# ALarson,
# ------------------------------------------#

# if __name__ == '__main__':
#    raise Exception ('This file is not meant to run by itself.')

import csv
import os

# ---DATA--- #
HP_HR = 'HP_HR_Records.csv'
header = ['employee_id', 'name', 'address', 'ssn', 'dob', 'job_title', 'start_date', 'end_date']
table = []

# ---FILE PROCESSING--- #
# Read in Human Resources file from csv using list format
class FileProcessor:
    """Processing data to and from csv"""
    # @staticmethod
    # def verify_path(some_path_string):
    #     some_path_string = input("Prompt to get path")
    #
    #     while not os.path.exists(some_path_string):
    #         print('The HR file does not exist at the path you provided.')
    #         some_path_string = input('Prompt to get path')
    #     return some_path_string + '\\HP_HR_Records.csv'

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries.
        Reads the data from file identified by file_name into a 2D table (list of dicts) one row in the file represents one dictionary row in table.

        Args:
            file_name (string): name of csv file used from which to read the data
            table (list of dict): 2D data structure (list of dictionaries) that holds the data during runtime

        Returns:
            None
            """

        # Read in employees from csv
        table.clear()  # this clears existing data and allows to load data from file
        while True:
            some_path_string = input("Please enter the path where your HR Records are saved: \n")
            fullpath = some_path_string + '\\HP_HR_Records.csv'
            if os.path.exists(fullpath):
                print(fullpath)
                with open(fullpath, mode='r', newline='') as f:
                    csv_reader = csv.DictReader(f)
                    line_count = 0
                    for row in csv_reader:
                        table.append(row)
                    break
            else:
                print('The HR Records were not found at the provided link, please try again.')

    @staticmethod
    def write_file(file_name, table):
        """Function to manage the saving of Human Resources data to a csv file.

        Args:
            file_name (string): name of file to be saved, presumably the same as has already been loaded in.
            table (list of dictionaries): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
            """
        while True:
            some_path_string = input("Please enter the directory path where you'd like to save your HR Records: \n")
            fullpath = some_path_string + '\\HP_HR_Records.csv'
            if os.path.exists(fullpath):
                print(fullpath)
                with open(fullpath, mode='w', newline='') as f:
                    writer = csv.DictWriter(f, header)
                    writer.writeheader()
                    for row in table:
                        writer.writerow(row)
                    break
            else:
                print('That directory path was not found, please try again.')



