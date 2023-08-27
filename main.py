from handle_data_script import *
from write_data_to_file import *

# use an array of strings to store the  name(s) of the txt file(s) with the table data
file_names = ["department_table.txt", "employee_table1.txt", "employee_table2.txt", "project_table.txt", "employee_account_table.txt"]

inserts = read_data_from_file(file_names)

send_to_file(inserts, 'insert_result.txt')