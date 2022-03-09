from src.assignment06.files import FileProcessor
from src.assignment06.input_output import Menu


# from InputOutput import Reports
# from InputOutput import NewEmployee


def test_print_menu():
    assert Menu.print_menu() is None


def test_read_file():
    assert FileProcessor.read_file()

def test_menu_choice():
    choice = ''
    Menu.menu_choice()
    assert choice in [1, 2, 3, 4, 5, 6, 7]


# class Reports:
#
#     @staticmethod
#     def test_show_current():
#         assert False
#
#     @staticmethod
#     def test_show_unemployed():
#         assert False
#
#     @staticmethod
#     def test_show_reviews():
#         assert False
#
#
# class NewEmployee:
#
#     @staticmethod
#     def test_employee_name():
#         assert False
#
#     @staticmethod
#     def test_employee_address():
#         assert False
#
#     @staticmethod
#     def test_employee_ssn():
#         assert False
#
#     @staticmethod
#     def test_employee_dob():
#         assert False
#
#     @staticmethod
#     def test_employee_job():
#         assert False
#
#     @staticmethod
#     def test_employee_start():
#         assert False
#
#     @staticmethod
#     def test_employee_end():
#         assert False
