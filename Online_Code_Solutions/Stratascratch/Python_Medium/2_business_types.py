# OUTPUTs: business na,e and calculated classification
# classify business based on types
#  types to use: restaurant,  'cafe',| 'café', | 'coffee', school, or other

# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations.copy()
df['business_name'] = df['business_name'].str.lower()
df['business_type'] = df['business_name'].apply(lambda x: 'school' if 'school' in x\
                        else 'restaurant' if 'restaurant' in x\
                        else 'cafe' if 'cafe' in x or 'coffee' in x or 'café' in x
                        else 'other')
df[['business_name', 'business_type']].drop_duplicates()
