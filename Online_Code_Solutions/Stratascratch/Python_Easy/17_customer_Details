# OUTPUTs: first name, last name, city, order details
# find details of each customer
# show all customers with or witout orders made
# there may be duplicates
# sort values by customer name first then order details in ascending order

# Import your libraries
import pandas as pd

# Start writing code
df = customers.copy()
combined = customers.merge(orders,
                        left_on='id',
                        right_on='cust_id',
                        how='outer')

combined[['first_name', 'last_name', 'city', 'order_details']].sort_values(['first_name','order_details'])
