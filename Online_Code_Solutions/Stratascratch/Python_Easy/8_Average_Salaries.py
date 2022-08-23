# OUTPUTs: department, firstname, salary, avg salary of department
# find avg salary adn make new column, show results

# Import your libraries
import pandas as pd

# Start writing code
employee['avg_sal_byDepartment'] = employee.groupby(['department'])['salary'].transform('mean')
employee[['department', 'first_name', 'salary', 'avg_sal_byDepartment']]
