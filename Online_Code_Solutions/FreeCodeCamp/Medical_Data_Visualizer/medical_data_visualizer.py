# could not fix replit. Pandas not working so I did this in jupyter notebook and then transferred your result here to turn in.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
# To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
#  1 cm = .01 meteres so we need to divide heigh by 100 before we square it

df['overweight'] = df.apply(lambda x : 1 if x['weight'] / ((x['height'] / 100)**2) > 25 else 0, axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df.apply(lambda x: 0 if x['cholesterol'] == 1 else 1, axis=1)
df['gluc'] = df.apply(lambda x: 0 if x['gluc	'] == 1 else 1, axis=1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars = ['cholesterol','gluc','smoke','alco','active'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df1['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    

    # Draw the catplot with 'sns.catplot()'
    


    # Get the figure for the output
    fig = sns.catplot(x='variable', y='total', data=df1, hue='value', kind='bar',col='cardio')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]

    # Calculate the correlation matrix
    corr = df_heat.corr(method='pearson')

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, linewidths=1, annot=True, square = True, mask =mask, fmt=".1f", center=0.08, cbar_kws={"shrink":0.5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
