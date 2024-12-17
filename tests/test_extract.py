#4-Extract Test

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

if __name__ == "__main__":
    test_should_pass()
    test_csv_file_exists()
    test_csv_file_read()