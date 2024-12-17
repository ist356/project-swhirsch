# Analysis Five - Top 10 Players with the Most Interceptions in the 2023 Season

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv('./Cache/cleaned_passing_data.csv')

# Sort the DataFrame by Interceptions in descending order and select the top 10
top_10_interceptions = data.sort_values(by='Interceptions', ascending=False).head(10)

# Create a bar chart using Seaborn
plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='Interceptions', y='Name', data=top_10_interceptions, palette='coolwarm')

# Set labels and title
plt.xlabel('Interceptions', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.title('Top 10 Players with the Most Interceptions in the 2023 Season', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Add data labels
for index, value in enumerate(top_10_interceptions['Interceptions']):
    plt.text(value, index, str(value), color='black', ha="left", va="center", fontsize=12)

# Display the plot
plt.show()