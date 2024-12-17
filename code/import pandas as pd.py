import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('./Cache/cleaned_passing_data.csv')

# Filter the DataFrame for quarterbacks with over 100 passing attempts
filtered_data = data[data['Passes Attempted'] > 400]

# Sort the filtered data by the Touchdown Percentage in descending order
sorted_data = filtered_data.sort_values(by='Touchdown Percentage', ascending=False)

# Print the players with the highest touchdown percentage
print("Players with the highest touchdown percentage over 100 passing attempts:")
print(sorted_data[['Name', 'Passes Attempted', 'Touchdown Percentage']])