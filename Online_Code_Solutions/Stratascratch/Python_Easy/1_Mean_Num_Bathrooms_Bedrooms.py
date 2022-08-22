# OUTPUTs: avgerage bed adn bath, city name, and property type
# find avg num of bath and bedrooms
# group by city and property types. then find means
# will need to reset city and property types from index to series for outputs

# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.groupby(['city', 'property_type'])['bathrooms','bedrooms'].mean().reset_index()
