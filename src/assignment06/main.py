# ------------------------------------------#
# Title: main.py
# Desc: assignment 06
# Change Log: (Who, When, What)
# ALarson, 2022-02-25, Created file, started assignment
# ALarson, 
# ------------------------------------------#
import InputOutput as IO
import Files



# ---DATA--- #
HP_HR = 'HP_HR_Records.csv'
table = []

# #start here
# if __name__ == '__main__':
#     some_path_string = input("Prompt to get path")
#     some_path_string = Files.FileProcessor.verify_path(some_path_string)

while True:

    IO.Menu.print_menu()
    choice = IO.Menu.menu_choice()
    if choice == 1:
        while True:
            y_n = input('Are you sure you want to import records? \nIf you have entered a new employee and haven\'t saved, '
                        'this will erase your work. \nPlease enter \'Yes\' to continue importing. Enter \'No\' to go back '
                        'to the main menu.\n')
            if y_n == 'Yes'.lower():
                Files.FileProcessor.read_file(HP_HR, table)
                print('File Found. Records loaded to file, back to main menu...\n')
                break
            elif y_n == 'No'.lower():
                print('Okay, back to the main menu...')
                break
            else:
                print('Please select \'Yes\' or \'No\'.\n')

    elif choice == 2:
        Files.FileProcessor.write_file(HP_HR, table)

    elif choice == 3:
        # Files.FileProcessor.read_file(HP_HR, table) #first read in excisting employees otherwise the  new employee id will start at 1
        employee_id = len(table)+1
        new_employee = {'employee_id': employee_id, 'name': IO.new_employee.employee_name(), 'address': IO.new_employee.employee_address(), 'ssn': IO.new_employee.employee_ssn(), 'dob': IO.new_employee.employee_dob(), 'job_title': IO.new_employee.employee_job(), 'start_date': IO.new_employee.employee_start(), 'end_date': IO.new_employee.employee_end()}
        table.append(new_employee)
        # print(table)

    elif choice == 4:
        IO.Reports.show_current(table)

    elif choice == 5:
        IO.Reports.show_unemployed(table)

    elif choice == 6:
        IO.Reports.show_reviews(table)

    else:
        print('Goodbye')
        break

