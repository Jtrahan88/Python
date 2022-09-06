# OUTPUTs: num users event by macbookpro, and event name
#  macbookpro only
#  Count events
#  sort by event count in descending order

# Import your libraries
import pandas as pd

# Start writing code

df = playbook_events.copy()
df = df[df['device'] == 'macbook pro']
df.groupby(['event_name']).size().to_frame('size').reset_index().sort_values(['size'], ascending=False)
