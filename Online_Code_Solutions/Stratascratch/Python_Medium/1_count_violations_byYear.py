# OUTPUTs: number of violations by year
# Count number of violation for Roxanne Cafe for each year
#  Sort values by year in ascending order

# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations.copy()

R_cafe = df[df['business_name'] == 'Roxanne Cafe']
R_cafe['inspection_date'] = R_cafe['inspection_date'].dt.year
R_cafe.groupby(['inspection_date'])['business_id'].count().reset_index()
