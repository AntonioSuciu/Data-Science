import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
# bmi = kgs / (0.1 * height^2)

df['bmi'] = df['weight']/(0.01*df['height'])**2
df['overweight'] = [1 if (i > 25) else 0 for i in df['bmi']]
df = df.drop(columns='bmi')

# Normalize data by making 0 always good and 1 always bad.
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = [0 if (i == 1) else 1 for i in df['gluc']]
df['cholesterol'] = [0 if (i == 1) else 1 for i in df['cholesterol']]


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    # selected_columns = df[["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]]

    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = None

    # Draw the catplot with 'sns.catplot()'
    the_catplot = sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")
    the_catplot.set_ylabels("total")
    fig = the_catplot.fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    # diastolic pressure is higher than systolic
    # (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    # height is less than the 2.5th percentile
    # (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    # height is more than the 97.5th percentile
    # weight is less than the 2.5th percentile
    # weight is more than the 97.5th percentile

    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025))
                     & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025))
                     & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    # Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle.

    corr = df_heat.corr(method="pearson")

    # Generate a mask for the upper triangle

    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
