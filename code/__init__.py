import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file
csv_path = "Cache/cleaned_passing_data.csv"
df = pd.read_csv(csv_path, header=None)

# Create a histogram using Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title("Distribution of Ages in Cleaned Passing Data")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()