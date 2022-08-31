# OUTPUTs: activity date and the pe_description
#  facilities with teh name 'STREET CHURROS'
#  score < 95

# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections.copy()
df['activity_date'] = df['activity_date'].dt.date
df[(df['facility_name'] == 'STREET CHURROS') & (df['score'] < 95)][['activity_date','pe_description']]
