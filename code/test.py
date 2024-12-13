import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title("Distribution of Ages in Cleaned Passing Data")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()