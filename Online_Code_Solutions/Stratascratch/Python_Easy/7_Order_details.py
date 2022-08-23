# OUTPUTs: Order date, details, cost, first name
# Find orders made by Jill and Eva
# Sort values by customer ID

# Import your libraries
import pandas as pd

# Start writing code
# join teh two tables:
combined = customers.merge(orders,
                        left_on='id',
                        right_on='cust_id',
                        how='outer')
combined[combined['first_name'].isin(['Jill', 'Eva'])][['order_date', 'order_details', 'total_order_cost','first_name']]
