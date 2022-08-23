# OUTPUTs: all results for question
# Find drivers who earn <= 30k OR >=70k

# Import your libraries
import pandas as pd

# Start writing code
results  = lyft_drivers[(lyft_drivers['yearly_salary'] <= 30000) | (lyft_drivers['yearly_salary'] >= 70000)]
