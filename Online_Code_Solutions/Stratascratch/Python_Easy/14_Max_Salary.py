# OUTPUTs: id, first name, last name, department id, and current salary
# Data in system is old and we need to find most current salary
# there are duplicates

# Import your libraries
import pandas as pd

# Start writing code
ms_employee_salary.groupby(['id','first_name', 'last_name', 'department_id'])['salary'].max().reset_index().sort_values(by='id')
