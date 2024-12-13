#Analysis Two - Distribution of Passer Ratings in the 2023 NFL Season

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_path = "./Cache/cleaned_passing_data.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(12, 8))
histplot = sns.histplot(df['Passer Rating'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title("Distribution of Passer Ratings in Cleaned Passing Data", fontsize=16)
plt.xlabel("Passer Rating", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

mean_passer_rating = df['Passer Rating'].mean()

plt.axvline(mean_passer_rating, color='red', linestyle='dashed', linewidth=1)
plt.text(mean_passer_rating + 0.5, max(plt.gca().get_ylim()) * 0.9, f'Mean Passer Rating: {mean_passer_rating:.2f}', color='red', fontsize=12)

for p in histplot.patches:
    height = p.get_height()
    histplot.annotate(f'{int(height)}', 
                      xy=(p.get_x() + p.get_width() / 2, height), 
                      xytext=(0, 5), 
                      textcoords="offset points", 
                      ha='center', fontsize=12)

plt.show()