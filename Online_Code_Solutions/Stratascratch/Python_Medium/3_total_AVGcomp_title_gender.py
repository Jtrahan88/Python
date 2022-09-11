# OUTPUTs: employee title, gender, avg total compensation
# total comp = salary and bonus
# based on titles and gender
# skip employees without bonuses


# Import your libraries
import pandas as pd

# Start writing code
salary = sf_employee.copy()
bonus = sf_bonus.copy()

bonus_sum = bonus.groupby(['worker_ref_id'])['bonus'].sum().to_frame('bonus').reset_index()

combined = pd.merge(salary,
                    bonus_sum,
                    left_on='id',
                    right_on='worker_ref_id')
                    
# combined = combined[~(combined['bonus'].isna())].drop_duplicates()
combined['Total Comp'] = combined['bonus'] + combined['salary']
combined.groupby(['sex', 'employee_title'])['Total Comp'].mean().reset_index()
