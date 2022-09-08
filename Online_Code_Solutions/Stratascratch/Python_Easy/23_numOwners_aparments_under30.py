# OUTPUTs: nationality, num of apartments
# owned by people under 30
# Sort values by apartment counts DESC

# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_hosts.copy()

combine = df.merge(airbnb_units,
                        left_on='host_id',
                        right_on='host_id',
                        how='left')
                        
conditions = combine[(combine['unit_type'] == 'Apartment') & (combine['age'] < 30)]

results = conditions.groupby(['nationality'])['unit_id'].nunique().to_frame('Apartment_counts').reset_index().sort_values(by='Apartment_counts', ascending=False)
