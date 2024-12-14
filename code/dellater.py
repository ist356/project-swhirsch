import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the CSV file into a DataFrame
data = pd.read_csv('./Cache/cleaned_passing_data.csv')

# Plot the linear regression
st.header('Linear Regression of Passes Attempted vs Completion Percentage')
plt.figure(figsize=(12, 8))
sns.regplot(x='Completion Percentage', y='Passes Attempted', data=data, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Linear Regression of Passes Attempted vs Completion Percentage', fontsize=16)
plt.xlabel('Completion Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)

# Annotate specific players
players_to_label = ["Patrick Mahomes", "Dak Prescott", "Jared Goff"]
label_offsets = [(5, -50), (5, -150), (5, -250)]  # Different offsets for each player to spread out the arrows
for i, (index, row) in enumerate(data[data['Name'].isin(players_to_label)].iterrows()):
    offset = label_offsets[i % len(label_offsets)]
    plt.annotate(f"{row['Name']} ({row['Passes Attempted']}, {row['Completion Percentage']:.2f}%)",
                 xy=(row['Completion Percentage'], row['Passes Attempted']),
                 xytext=(row['Completion Percentage'] + offset[0], row['Passes Attempted'] + offset[1]),
                 arrowprops=dict(facecolor='black', arrowstyle="->"),
                 fontsize=12, color='black')

st.pyplot(plt)

# Calculate and print the correlation coefficient using pandas
correlation = data['Completion Percentage'].corr(data['Passes Attempted'])
st.write(f"Correlation between Completion Percentage and Passes Attempted: {correlation:.2f}")

# Calculate the linear regression coefficients manually
x = data['Completion Percentage']
y = data['Passes Attempted']
n = len(x)

# Calculate the means of x and y
x_mean = x.mean()
y_mean = y.mean()

# Calculate the slope (m) and intercept (b) of the regression line
numerator = sum((x - x_mean) * (y - y_mean))
denominator = sum((x - x_mean) ** 2)
slope = numerator / denominator
intercept = y_mean - slope * x_mean

# Print the regression coefficients
st.write(f"Intercept: {intercept:.2f}")
st.write(f"Coefficient for Completion Percentage: {slope:.2f}")

# Predict and plot the regression line
data['Predicted Passes Attempted'] = intercept + slope * x
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Completion Percentage', y='Passes Attempted', data=data, s=50)
sns.lineplot(x='Completion Percentage', y='Predicted Passes Attempted', data=data, color='red')
plt.title('Linear Regression of Passes Attempted vs Completion Percentage', fontsize=16)
plt.xlabel('Completion Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)


# Filter the data for players with over 200 passes attempted
filtered_data = data[data['Passes Attempted'] > 200]

# Find the player with the worst Completion Percentage
worst_player = filtered_data[filtered_data['Completion Percentage'] == filtered_data['Completion Percentage'].min()]['Name'].values[0]

# Print the name of the player with the worst Completion Percentage
st.write(f"Player with the worst Completion Percentage (with over 200 passes attempted): {worst_player}")
# Calculate and print the average completion percentage
average_completion_percentage = data['Completion Percentage'].mean()
st.write(f"Average Completion Percentage: {average_completion_percentage:.2f}")




