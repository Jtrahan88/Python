#  OUTPUTs: business name, review text, highest num of 'cool' votes


# Import your libraries
import pandas as pd

# Start writing code
df = yelp_reviews.copy()

result = df[df['cool'] == df['cool'].max()][['business_name', 'review_text']]
