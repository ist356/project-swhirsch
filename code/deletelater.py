import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('./Cache/cleaned_passing_data.csv')

# Calculate the correlation between 'Interceptions' and 'Yards per Passing Attempt'
correlation = df['Interceptions'].corr(df['Completion Percentage'])

# Print the correlation coefficient
print(f"Correlation between Interceptions and Yards per Passing Attempt: {correlation}")