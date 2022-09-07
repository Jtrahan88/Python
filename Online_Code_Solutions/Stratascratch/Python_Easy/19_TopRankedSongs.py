# OUTPUTs: track name, num of times it ranked the top
# sort values by num time was in top postions descending order

# Import your libraries
import pandas as pd

# Start writing code
df = spotify_worldwide_daily_song_ranking.copy()

df_ranks =df.groupby(['trackname', 'position']).size().to_frame('size').reset_index().sort_values(by='size', ascending=False)

df_ranks = df_ranks[df_ranks['position'] == 1]
