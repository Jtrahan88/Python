# OUTPUTs: rank, group name, song name
# find top 10 ranked sogns in 2010
# do not show duplicates
# sort values by year rank in ascending order

# Import your libraries
import pandas as pd

# Start writing code
df = billboard_top_100_year_end.copy()

df_year = df[df['year'] == 2010].sort_values(by='year_rank')

results = df_year[['year_rank', 'group_name', 'song_name']].drop_duplicates().head(10)
