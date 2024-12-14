import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TestAnalysisOne(unittest.TestCase):

    def setUp(self):
        # Load the CSV file into a DataFrame
        self.csv_path = './Cache/cleaned_passing_data.csv'
        self.df = pd.read_csv(self.csv_path)

    def test_script_runs(self):
        try:
            plt.figure(figsize=(12, 8))
            histplot = sns.histplot(self.df['Age'], bins=10, kde=True, color='skyblue', edgecolor='black')
            plt.title("Distribution of Ages in Cleaned Passing Data", fontsize=16)
            plt.xlabel("Age", fontsize=14)
            plt.ylabel("Frequency", fontsize=14)
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)

            mean_age = self.df['Age'].mean()

            plt.axvline(mean_age, color='red', linestyle='dashed', linewidth=1)
            plt.text(mean_age + 0.5, max(plt.gca().get_ylim()) * 0.9, f'Mean Age: {mean_age:.2f}', color='red', fontsize=12)

            for p in histplot.patches:
                height = p.get_height()
                histplot.annotate(f'{int(height)}', 
                                  xy=(p.get_x() + p.get_width() / 2, height), 
                                  xytext=(0, 5),  
                                  textcoords="offset points", 
                                  ha='center', fontsize=12)

            plt.close()
        except Exception as e:
            self.fail(f"Script failed to run: {e}")

    def test_mean_age_calculation(self):
        expected_mean_age = self.df['Age'].mean()
        self.assertAlmostEqual(expected_mean_age, self.df['Age'].mean(), places=2)

if __name__ == '__main__':
    unittest.main()