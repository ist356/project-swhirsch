import pandas as pd
import os
from playwright.sync_api import sync_playwright

# Ensure Cache folder exists
if not os.path.exists("code"):
    os.makedirs("code")

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
        csv_path = "code/passing_data.csv"
        df.to_csv(csv_path, index=False)
        print(f"CSV file saved to {csv_path}")
        
        browser.close()

# Run the extraction function
extract_data()

# Read the CSV file
csv_path = "code/passing_data.csv"
df = pd.read_csv(csv_path, header=None)

# Delete the row with the name "League Average"
df = df[df[0] != "League Average"]

# Rename columns
df.rename(columns={
    0: "Name",
    1: "Age",
    2: "Team",
    3: "Position",
    4: "Games Played",
    5: "Games Started",
    6: "Record",
    7: "Completed Passes",
    8: "Passes Attempted",
    9: "Completion Percentage",
    10: "Passing Yards",
    11: "Passing Touchdowns",
    12: "Touchdown Percentage",
    13: "Interceptions",
    14: "Interception Percentage",
    15: "Passing First Downs",
    17: "Longest Pass Thrown",
    18: "Yards per Passing Attempt",
    22: "Passer Rating",
    23: "Quarterback Rating"
}, inplace=True)

# Delete the specified columns
df.drop(columns=[16, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31], inplace=True)

# Delete rows where Position is not "QB"
df = df[df["Position"] == "QB"]

# Remove rows where Name is "Joshua Dobbs" and Team is "ARI" or "MIN"
df = df[~((df["Name"] == "Joshua Dobbs") & (df["Team"].isin(["ARI", "MIN"])))]

# Convert columns to integers except for Name, Team, and Position
columns_to_convert = df.columns.difference(["Name", "Team", "Position", "Record"])
df[columns_to_convert] = df[columns_to_convert].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

# Save the cleaned data to a new CSV file
cleaned_csv_path = "code/cleaned_passing_data.csv"
df.to_csv(cleaned_csv_path, index=False)
print(f"Cleaned CSV file saved to {cleaned_csv_path}")