# Analysis 6: Linear Regressios of Passes Attempted vs Completion Percentage and Touchdown Percentage in 2023 NFL Season

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv('./Cache/cleaned_passing_data.csv')

# Remove major outliers using a more stringent IQR method
Q1 = data['Passes Attempted'].quantile(0.25)
Q3 = data['Passes Attempted'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 2.5 * IQR
upper_bound = Q3 + 2.5 * IQR
data = data[(data['Passes Attempted'] >= lower_bound) & (data['Passes Attempted'] <= upper_bound)]

# Create a linear regression plot for Completion Percentage
plt.figure(figsize=(12, 8))
sns.regplot(x='Completion Percentage', y='Passes Attempted', data=data, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Linear Regression of Passes Attempted vs Completion Percentage', fontsize=16)
plt.xlabel('Completion Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Label the points for "Patrick Mahomes", "Dak Prescott", and "Jared Goff"
players_to_label = ["Patrick Mahomes", "Dak Prescott", "Jared Goff"]
label_offsets = [(5, -50), (5, -150), (5, -250)]  # Different offsets for each player to spread out the arrows
for i, (index, row) in enumerate(data[data['Name'].isin(players_to_label)].iterrows()):
    offset = label_offsets[i % len(label_offsets)]
    plt.annotate(f"{row['Name']} ({row['Passes Attempted']}, {row['Completion Percentage']:.2f}%)",
                 xy=(row['Completion Percentage'], row['Passes Attempted']),
                 xytext=(row['Completion Percentage'] + offset[0], row['Passes Attempted'] + offset[1]),
                 arrowprops=dict(facecolor='black', arrowstyle="->"),
                 fontsize=12, color='black')

plt.show()

# Create a linear regression plot for Touchdown Percentage
plt.figure(figsize=(12, 8))
sns.regplot(x='Touchdown Percentage', y='Passes Attempted', data=data, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Linear Regression of Passes Attempted vs Touchdown Percentage', fontsize=16)
plt.xlabel('Touchdown Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Label the points for "Brock Purdy", "Tua Tagovailoa", and "Josh Allen"
players_to_label = ["Brock Purdy", "Tua Tagovailoa", "Josh Allen"]
label_offsets = [(0.5, -50), (1.5, 50), (-0.5, -25.0)]  # Different offsets for each player to spread out the arrows
for i, (index, row) in enumerate(data[data['Name'].isin(players_to_label)].iterrows()):
    offset = label_offsets[i % len(label_offsets)]
    plt.annotate(f"{row['Name']} ({row['Passes Attempted']}, {row['Touchdown Percentage']:.2f}%)",
                 xy=(row['Touchdown Percentage'], row['Passes Attempted']),
                 xytext=(row['Touchdown Percentage'] + offset[0], row['Passes Attempted'] + offset[1]),
                 arrowprops=dict(facecolor='black', arrowstyle="->"),
                 fontsize=12, color='black')

plt.show()
