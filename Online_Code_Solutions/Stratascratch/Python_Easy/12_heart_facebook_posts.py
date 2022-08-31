# OUTPUts: All columns from posts table with heart reactions

# Import your libraries
import pandas as pd

# Start writing code
combine = facebook_posts.merge(facebook_reactions,
                                left_on='post_id',
                                right_on='post_id',
                                how='left')
                                
combine[combine['reaction'] == 'heart'].drop_duplicates(subset='post_id')
