# OUTPUTs: location and avg popularity
#  find avg popularity of hacker per office location

# Import your libraries
import pandas as pd

# Start writing code
combined = facebook_employees.merge(facebook_hack_survey,
                                    left_on='id',
                                    right_on='employee_id',how='outer')

results = combined.groupby(['location'])['popularity'].mean().reset_index()
