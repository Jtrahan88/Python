#  OUTPUTs: business name, total num reviews
# top 5 business most reviews
# each business has  unique business id
# Sort values by total reviews descending 

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business.copy()

df.groupby(['name'])['review_count'].sum().reset_index().sort_values(by='review_count', ascending=False).head(5)
