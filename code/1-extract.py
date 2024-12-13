import pandas as pd
import os
from playwright.sync_api import sync_playwright

if not os.path.exists("code"):
    os.makedirs("code")

def extract_data():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.pro-football-reference.com/years/2023/passing.htm#passing")
        

        table = page.query_selector("#passing")
        rows = table.query_selector_all("tbody tr")
        
        data = []
        for row in rows:
            cells = row.query_selector_all("td")
            data.append([cell.inner_text() for cell in cells])
        

        df = pd.DataFrame(data)
        

        csv_path = "code/passing_data.csv"
        df.to_csv(csv_path, index=False)
        print(f"CSV file saved to {csv_path}")
        
        browser.close()

extract_data()

df = pd.read_csv("code/passing_data.csv")
print(df.head())