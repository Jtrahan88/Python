# OUTPUTs: host id, guest id
#  host and gust must have same gender and nationality

# Import your libraries
import pandas as pd

# Start writing code
combined = airbnb_hosts.merge(airbnb_guests,
                            left_on=['nationality','gender'],
                            right_on=['nationality','gender'],
                            how='left')
combined[['host_id', 'guest_id']].drop_duplicates() 
