# OUTPUTs:  most profitable company and continent
# sectror = financial


# Import your libraries
import pandas as pd

# Start writing code
sector = forbes_global_2010_2014[forbes_global_2010_2014['sector'] == 'Financials']

result = sector.groupby(['company','continent'])['profits'].max().reset_index().sort_values(by='profits',ascending=False).head(1)

result[['company', 'continent']]
