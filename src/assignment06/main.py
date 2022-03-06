# ------------------------------------------#
# Title: main.py
# Desc: assignment 06
# Change Log: (Who, When, What)
# ALarson, 2022-02-25, Created file, started assignment
# ALarson, 
# ------------------------7------------------#
import input_output as IO
import files



# ---DATA--- #
HP_HR = 'HP_HR_Records.csv'
table = []

# #start here
# if __name__ == '__main__':
#     some_path_string = input("Prompt to get path")
#     some_path_string = files.FileProcessor.verify_path(some_path_string)

while True:

    IO.Menu.print_menu()
    choice = IO.Menu.menu_choice()
    if choice == 1:
        while True:
            y_n = input('Are you sure you want to import records? \nIf you have entered a new employee and haven\'t saved, '
                        'this will erase your work. \nPlease enter \'Yes\' to continue importing. Enter \'No\' to go back '
                        'to the main menu.\n')
            if y_n == 'Yes'.lower():
                files.FileProcessor.read_file(HP_HR, table)
                print('File Found. Records loaded to file, back to main menu...\n')
                break
            elif y_n == 'No'.lower():
                print('Okay, back to the main menu...')
                break
            else:
                print('Please select \'Yes\' or \'No\'.\n')

    elif choice == 2:
        files.FileProcessor.write_file(HP_HR, table)

    elif choice == 3:
        # files.FileProcessor.read_file(HP_HR, table) #first read in excisting employees otherwise the  new employee id will start at 1
        employee_id = len(table)+1
        new_employee = {'employee_id': employee_id, 'name': IO.NewEmployee.employee_name(), 'address': IO.NewEmployee.employee_address(), 'ssn': IO.NewEmployee.employee_ssn(), 'dob': IO.NewEmployee.employee_dob(), 'job_title': IO.NewEmployee.employee_job(), 'start_date': IO.NewEmployee.employee_start(), 'end_date': IO.NewEmployee.employee_end()}
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

