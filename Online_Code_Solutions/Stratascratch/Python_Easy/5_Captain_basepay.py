# find the base pay of Police Captains

# Import your libraries
import pandas as pd

# Start writing code
# find out all job titles
# sf_public_salaries['jobtitle'].value_counts().reset_index()

# captains job title = CAPTAIN III (POLICE DEPARTMENT)
sf_public_salaries = sf_public_salaries[sf_public_salaries['jobtitle'] == 'CAPTAIN III (POLICE DEPARTMENT)']

# outputs the employee name, and pay:
sf_public_salaries[['employeename', 'basepay']]
sf_public_salaries


# one liner:
result =sf_public_salaries[(sf_public_salaries['jobtitle'].str.contains('CAPTAIN', case = False))&(sf_public_salaries['jobtitle'].str.contains('POLICE', case = False))][['employeename','basepay']]
