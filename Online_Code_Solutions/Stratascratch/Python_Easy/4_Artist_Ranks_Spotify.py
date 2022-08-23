# OUTPUTs: artist name, num of occurances
# count number of times artist was on spotify's ranking list

# Import your libraries
import pandas as pd

# Start writing code
counts = spotify_worldwide_daily_song_ranking.groupby(['artist'])['id'].count().reset_index().rename(columns={'id':'times_ranked'}).sort_values(by='times_ranked', ascending=False)
