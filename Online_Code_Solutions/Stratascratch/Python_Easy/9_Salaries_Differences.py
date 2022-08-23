#  OUTPUTs: abs difference between highest salaries
#  only in the marketing and engineering departments

# Import your libraries
import pandas as pd

# Start writing code
# Merge tables
combined = db_employee.merge(db_dept,
                        left_on='department_id',
                        right_on='id',
                        how='outer')

# Find max salary for marketing department
df_marketing = combined[combined['department'] =='marketing']
df_marketing_maxSal = df_marketing.groupby('department')['salary'].max().reset_index(name='MAx_marketing')

# Find max salary for engineering department
df_engineering = combined[combined['department'] =='engineering']
df_engineering_maxSal = df_engineering.groupby('department')['salary'].max().reset_index(name='MAx_engineering')

# Subtract:
result = abs(df_marketing_maxSal['MAx_marketing'] - df_engineering_maxSal['MAx_engineering'])
