# OUTPUTs: library code
# find libraries with no email address but choise to be contacted by email

# Import your libraries
import pandas as pd

# Start writing code
library_usage[(library_usage['provided_email_address'] == False) & (library_usage['notice_preference_definition'] == 'email')\
              & (library_usage['circulation_active_year'] == 2016)]['home_library_code'].drop_duplicates()
