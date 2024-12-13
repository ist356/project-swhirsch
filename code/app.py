import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data_path = './Cache/cleaned_passing_data.csv'
df = pd.read_csv(data_path)

# Streamlit app title
st.title('NFL Passing Data Dashboard')

# Sidebar for user input
st.sidebar.header('User Input Features')
selected_team = st.sidebar.selectbox('Team', df['Team'].unique())
selected_player = st.sidebar.selectbox('Player', df[df['Team'] == selected_team]['Name'].unique())

# Filter data based on user input
filtered_data = df[(df['Team'] == selected_team) & (df['Name'] == selected_player)]

# Display player stats
st.header(f'Stats for {selected_player}')
st.write(filtered_data)

# Analysis One: Distribution of Ages
st.header('Analysis One: Distribution of Ages')
plt.figure(figsize=(12, 8))
sns.histplot(df['Age'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribution of Ages in Cleaned Passing Data', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)

# Analysis Two: Distribution of Passer Ratings
st.header('Analysis Two: Distribution of Passer Ratings')
plt.figure(figsize=(12, 8))
sns.histplot(df['Passer Rating'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribution of Passer Ratings in Cleaned Passing Data', fontsize=16)
plt.xlabel('Passer Rating', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)

# Analysis Three: Top 10 Players with the Most Passing Touchdowns
st.header('Analysis Three: Top 10 Players with the Most Passing Touchdowns')
top_10_td = df.sort_values(by='Passing Touchdowns', ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x='Passing Touchdowns', y='Name', data=top_10_td, palette='coolwarm')
plt.xlabel('Passing Touchdowns', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.title('Top 10 Players with the Most Passing Touchdowns in the 2023 Season', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)

# Analysis Four: Top 10 Players with the Most Passing Yards
st.header('Analysis Four: Top 10 Players with the Most Passing Yards')
top_10_yards = df.sort_values(by='Passing Yards', ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x='Passing Yards', y='Name', data=top_10_yards, palette='coolwarm')
plt.xlabel('Passing Yards', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.title('Top 10 Players with the Most Passing Yards in the 2023 Season', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)

# Analysis Five: Top 10 Players with the Most Interceptions
st.header('Analysis Five: Top 10 Players with the Most Interceptions')
top_10_interceptions = df.sort_values(by='Interceptions', ascending=False).head(10)
plt.figure(figsize=(12, 8))
sns.barplot(x='Interceptions', y='Name', data=top_10_interceptions, palette='coolwarm')
plt.xlabel('Interceptions', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.title('Top 10 Players with the Most Interceptions in the 2023 Season', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)

# Analysis Six: Linear Regression of Passes Attempted vs Completion Percentage
st.header('Analysis Six: Linear Regression of Passes Attempted vs Completion Percentage')
plt.figure(figsize=(12, 8))
sns.regplot(x='Completion Percentage', y='Passes Attempted', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Linear Regression of Passes Attempted vs Completion Percentage', fontsize=16)
plt.xlabel('Completion Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
players_to_label = ["Patrick Mahomes", "Dak Prescott", "Jared Goff", "Brock Purdy", "Tua Tagovailoa", "Josh Allen"]
label_offsets = [(5, -50), (5, -150), (5, -250), (-5, 50), (-5, 150), (-5, 250)]
for i, (index, row) in enumerate(df[df['Name'].isin(players_to_label)].iterrows()):
    offset = label_offsets[i % len(label_offsets)]
    plt.annotate(f"{row['Name']} ({row['Passes Attempted']}, {row['Completion Percentage']:.2f}%)",
                 xy=(row['Completion Percentage'], row['Passes Attempted']),
                 xytext=(row['Completion Percentage'] + offset[0], row['Passes Attempted'] + offset[1]),
                 arrowprops=dict(facecolor='black', arrowstyle="->"),
                 fontsize=12, color='black')
st.pyplot(plt)

# Analysis Six: Linear Regression of Passes Attempted vs Touchdown Percentage
st.header('Analysis Six: Linear Regression of Passes Attempted vs Touchdown Percentage')
plt.figure(figsize=(12, 8))
sns.regplot(x='Touchdown Percentage', y='Passes Attempted', data=df, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Linear Regression of Passes Attempted vs Touchdown Percentage', fontsize=16)
plt.xlabel('Touchdown Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
players_to_label = ["Brock Purdy", "Tua Tagovailoa", "Josh Allen"]
label_offsets = [(0.5, 50), (0.5, -50), (-0.5, 50)]
for i, (index, row) in enumerate(df[df['Name'].isin(players_to_label)].iterrows()):
    offset = label_offsets[i % len(label_offsets)]
    plt.annotate(f"{row['Name']} ({row['Passes Attempted']}, {row['Touchdown Percentage']:.2f}%)",
                 xy=(row['Touchdown Percentage'], row['Passes Attempted']),
                 xytext=(row['Touchdown Percentage'] + offset[0], row['Passes Attempted'] + offset[1]),
                 arrowprops=dict(facecolor='black', arrowstyle="->"),
                 fontsize=12, color='black')
st.pyplot(plt)
