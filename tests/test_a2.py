#5-Analysis_Two Test

import pytest
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

csv_path = './Cache/cleaned_passing_data.csv'

def test_should_pass():
    print("\nAlways True!")
    assert True

def test_csv_file_exists():
    print(f"TESTING: {csv_path} file exists")
    assert os.path.exists(csv_path)

def test_csv_file_read():
    print(f"TESTING: {csv_path} read_csv")
    df = pd.read_csv(csv_path)
    assert not df.empty

def test_mean_age_calculation():
    df = pd.read_csv(csv_path)
    expected_mean_age = df['Age'].mean()
    print(f"TESTING: Mean age calculation")
    assert expected_mean_age == df['Age'].mean()

def test_histplot():
    df = pd.read_csv(csv_path)
    plt.figure(figsize=(12, 8))
    histplot = sns.histplot(df['Age'], bins=10, kde=True, color='skyblue', edgecolor='black')
    plt.title("Distribution of Ages in Cleaned Passing Data", fontsize=16)
    plt.xlabel("Age", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    mean_age = df['Age'].mean()

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

if __name__ == "__main__":
    test_should_pass()
    test_csv_file_exists()
    test_csv_file_read()
    test_mean_age_calculation()
    test_histplot()