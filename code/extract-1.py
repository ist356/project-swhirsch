import pandas as pd
import os
from playwright.sync_api import sync_playwright

# Ensure Cache folder exists
if not os.path.exists("Cache"):
    os.makedirs("Cache")

def extract_data():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.pro-football-reference.com/years/2023/passing.htm#passing")
        
        # Extract table data
        table = page.query_selector("#passing")
        rows = table.query_selector_all("tbody tr")
        
        data = []
        for row in rows:
            cells = row.query_selector_all("td")
            data.append([cell.inner_text() for cell in cells])
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Save to CSV in Cache folder
        csv_path = "Cache/passing_data.csv"
        df.to_csv(csv_path, index=False)
        print(f"CSV file saved to {csv_path}")
        
        browser.close()

# Run the extraction function
extract_data()

# Read and display the CSV file
df = pd.read_csv("Cache/passing_data.csv")
print(df.head())