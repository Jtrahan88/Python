# OUTPUTs: olympics, num of athletes with teh highest amount
# find highest num of athletes 
# use year, season, games columns

# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events.copy()

df.groupby(['games'])['name'].nunique().to_frame('num_athletes').reset_index().sort_values(by='num_athletes', ascending=False).head(1)
