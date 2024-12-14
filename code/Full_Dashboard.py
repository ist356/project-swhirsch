import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data_path = './Cache/cleaned_passing_data.csv'
df = pd.read_csv(data_path)

# Streamlit app title
st.title('NFL Passing Data Dashboard - 2023 Season')
st.markdown('<p style="font-size:12px;">Data obtained from Pro-Football-Reference.com</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size:12px;">Data Cleaning, Analysis, and Visualization by Sam Hirsch (IST 356)</p>', unsafe_allow_html=True)

# Sidebar for user input
st.sidebar.header('User Input Features for Player / Team Select')
selected_team = st.sidebar.selectbox('Team', df['Team'].unique())
selected_player = st.sidebar.selectbox('Player', df[df['Team'] == selected_team]['Name'].unique())

# Filter data based on user input
filtered_data = df[(df['Team'] == selected_team) & (df['Name'] == selected_player)]

# Display player stats
st.header(f'Statistic Viewer: {selected_player}')
st.write(filtered_data)

# Analysis One: Distribution of Ages
st.title("Distribution of Ages of Quarterbacks in the 2023 NFL Season")
csv_path = "./Cache/cleaned_passing_data.csv"
df = pd.read_csv(csv_path)

plt.figure(figsize=(12, 8))
histplot = sns.histplot(df['Age'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title("Analysis One: Distribution of Ages of Quarterbacks", fontsize=16)
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
    
st.pyplot(plt)

st.caption('Note: Ages are of Beginning of the 2023 NFL Season, September 2023')

st.caption('The histogram of quarterback ages at the beginning of the 2023 NFL Season shows most quarterbacks are between 24-30 years old, 70.8% to be specific, reflecting the combination of rising talent and players in their primes dominating the league. The 8 quarterbacks still playing at age 35 or older suggest the challenge of longevity at the quarterback position. Few quarterbacks play games under the age of 24, suggesting a preference of teams for more experience quarterbacks. The average age of quarterbacks who played in 2023 was 28.08, a balance between the influx fo youth and the older generation of talent in the league.')


# Analysis Two: Distribution of Passer Ratings
st.header('Analysis Two: Distribution of Passer Ratings')
plt.figure(figsize=(12, 8))
histplot = sns.histplot(df['Passer Rating'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribution of Passer Ratings in 2023 NFL Season', fontsize=16)
plt.xlabel('Passer Rating', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

mean_passer_rating = df['Passer Rating'].mean()

plt.axvline(mean_passer_rating, color='red', linestyle='dashed', linewidth=1)
plt.text(mean_passer_rating + 0.5, max(plt.gca().get_ylim()) * 0.9, f'Mean Passer Rating: {mean_passer_rating:.2f}', color='red', fontsize=12)

for p in histplot.patches:
    height = p.get_height()
    histplot.annotate(f'{int(height)}', 
                      xy=(p.get_x() + p.get_width() / 2, height), 
                      xytext=(0, 5),  
                      textcoords="offset points", 
                      ha='center', fontsize=12)

st.pyplot(plt)
st.caption('Passer Rating is the most popular metric of passing efficiency in the NFL. Scored on a scale from 0 to 158.3, the metric takes into account passing yards, touchdowns, attempts, completions, and interceptions. For the 2023 season, the average passer rating among quarterbacks was just over 80, significantly down from the 2020 season’s figure of 93.6. Players with the highest Passer Ratings tend to be back-ups who seized their limited opportunities. These quarterbacks include Jacoby Brissett (146) and Mason Rudolph (118). Among players with over 100 passing attempts, the top quarterbacks in 2023, according to passer rating were Brock Purdy (113), Dak Prescott (105), and Kirk Cousins (103).')

# Analysis Three: Top 10 Players with the Most Passing Touchdowns
st.header('Analysis Three: Top 10 Quarterbacks with the Most Passing Touchdowns')
top_10_td = df.sort_values(by='Passing Touchdowns', ascending=False).head(10)
plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='Passing Touchdowns', y='Name', data=top_10_td, palette='coolwarm')

#A3 Labels
for index, value in enumerate(top_10_td['Passing Touchdowns']):
    barplot.text(value, index, str(value), color='black', ha="left", va="center", fontsize=12)

plt.xlabel('Passing Touchdowns', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.title('Top 10 Players with the Most Passing Touchdowns in the 2023 Season', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)
st.caption('The Dallas Cowboys’s Dak Prescott led the NFL in passing touchdowns in the 2023 season with 3), followed by Jordan Love (32), Brock Purdy (31), and a tie between Jared Goff and Tua Tagovailoa (29). A strong positive correlation of 93.4 can be observed between touchdowns and attempts, which comes as no surprise. However, just a weak correlation (23.3) exists between passing touchdowns and completion percentage, suggesting efficiency and accuracy may not be vital for scoring touchdowns. The top 10 touchdown passers averaged a 98.5 Passer Rating, while the league-wide average touchdowns among all Quarterbacks who played a snap in 2023 was 9.5. This figure rose to 14.85 for quarterbacks with over 100 passing attempts. This suggests high touchdown production may depend more on opportunities and outside factors, such as a good surrounding cast than pure accuracy and efficiency.')

# Analysis Four: Top 10 Quarterbacks with the Most Passing Yards
st.header('Analysis Four: Top 10 Quarterbacks with the Most Passing Yards')
top_10_yards = df.sort_values(by='Passing Yards', ascending=False).head(10)
plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='Passing Yards', y='Name', data=top_10_yards, palette='coolwarm')

#A4 Labels
for index, value in enumerate(top_10_yards['Passing Yards']):
    barplot.text(value, index, str(value), color='black', ha="left", va="center", fontsize=12)

plt.xlabel('Passing Yards', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.title('Top 10 Quarterbacks with the Most Passing Yards in the 2023 Season', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)
st.caption('The 2023 NFL season held historically impressive passing performances, with Tua Tagovailoa leading the league in passing yards (4,624), followed by Jared Goff (4,575), Dak Prescott (4,516), Josh Allen (4,306), and Brock Purdy (4,280). The top 10 quarterbacks in passing yards averaged a touchdown percentage of 5.0%, significantly higher than the league average of 3.15%. This suggests that high-yardage quarterbacks were more efficient in turning opportunities into touchdowns. However, a high positive correlation of 0.85 between passing yards and interceptions suggests that quarterbacks who throw for more yards are more prone to turnover mistakes. ')

# Analysis Five: Top 10 Players with the Most Interceptions
st.header('Analysis Five: Top 10 Quarterbacks with the Most Interceptions')
top_10_interceptions = df.sort_values(by='Interceptions', ascending=False).head(10)
plt.figure(figsize=(12, 8))
barplot = sns.barplot(x='Interceptions', y='Name', data=top_10_interceptions, palette='coolwarm')

# A5 Labels
for index, value in enumerate(top_10_interceptions['Interceptions']):
    barplot.text(value, index, str(value), color='black', ha="left", va="center", fontsize=12)

plt.xlabel('Interceptions', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.title('Top 10 Quarterbacks with the Most Interceptions in the 2023 Season', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
st.pyplot(plt)

st.caption('The 2023 NFL season had an interesting batch of quarterbacks in the top 10 of interceptions, led by Sam Howell (21), Sam Howell (21), Josh Allen (18), Jalen Hurts (15),  and a three-way tie between Trevor Lawrence, Patrick Mahomes, and Tua Tagovailoa (14). Fundamentally, quarterbacks who throw more often tend to take more risks, increasing their chances of interceptions. Quarterbacks in this top 10 group attempted 530.1 passes this season, well above the average 445.8 for quarterbacks who appeared in 10 or more games. Their aggressive tendencies were reflected in their average passer rating of 88.5, which is lower than elite standards, but higher than the league average of 80.4. Interestingly, the data did not support my hypothesis that the more aggressive quarterbacks throw more interceptions. There is a weak positive correlative correlation of .02 between interceptions and Yards per Passing Attempt and a weak positive correlation of .21 between Interceptions and Completion Percentage. There are two categories of Quarterbacks in this top 10. The stars with job security (Mahomes, Allen) and those risk-takers who may struggle to find another starting position (Sam Howell, Desmond Ridder). Both Sam Howell and Desmond Ridder threw for as many touchdowns, as they did interceptions in 2023. ')

# Analysis6 p1: Linear Regression of Passes Attempted vs Completion Percentage
data = pd.read_csv('./Cache/cleaned_passing_data.csv')
st.header('Linear Regression of Passes Attempted vs Completion Percentage')
plt.figure(figsize=(12, 8))
sns.regplot(x='Completion Percentage', y='Passes Attempted', data=data, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Linear Regression of Passes Attempted vs Completion Percentage', fontsize=16)
plt.xlabel('Completion Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# a6p1 labels
players_to_label = ["Patrick Mahomes", "Dak Prescott", "Jared Goff", "Will Levis"]
label_offsets = [(5, -50), (5, -150), (5, -250), (15, -100)]  # Different offsets for each player to spread out the arrows
for i, (index, row) in enumerate(data[data['Name'].isin(players_to_label)].iterrows()):
    offset = label_offsets[i % len(label_offsets)]
    plt.annotate(f"{row['Name']} ({row['Passes Attempted']}, {row['Completion Percentage']:.2f}%)",
                 xy=(row['Completion Percentage'], row['Passes Attempted']),
                 xytext=(row['Completion Percentage'] + offset[0], row['Passes Attempted'] + offset[1]),
                 arrowprops=dict(facecolor='black', arrowstyle="->"),
                 fontsize=12, color='black')


st.pyplot(plt)
st.caption('The linear regression analysis shows a weak positive correlation of 0.23 between passes attempted and completion percentage. This suggests that there is some connection between these variables, but the number of passes attempted does not strongly predict a quarterbacks accuracy. The regression equation, with an intercept of 54.55 and a coefficient of 2.91, indicates that the completion percentage increases by 2.91 for each additional pass attempted. These statistics suggest other factors at play contribute to a player’s passing percentage. These may include the player’s play style, the team’s offensive scheme, or the talent surrounding the quarterback. Some players who stood out positively are Jared Goff (67% completion on 605 passes), Dak Prescott (69% on 590 attempts), and Patrick Mahomes (67% on 597). These performances all helped their teams reach the 2023 playoffs. On the other end, Will Levis struggled, with a league-low 58% completion percentage of all quarterbacks with over 200 passing attempts. Levis’s Tennesse Titans finished near the bottom of the league, and Levis continues to battle for his job. The league average was 60.75% for completion percentage, but this figure was skewed downward by quarterbacks who struggled in under 100 passing attempts. The data hints at the difficulty of having a high number of passing attempts while maintaining a high completion percentage. Those quarterbacks who do help their teams reach playoff success.')


# Analysis6 p2
st.header('Linear Regression of Passes Attempted vs Touchdown Percentage')
plt.figure(figsize=(12, 8))
sns.regplot(x='Touchdown Percentage', y='Passes Attempted', data=data, scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Linear Regression of Passes Attempted vs Touchdown Percentage', fontsize=16)
plt.xlabel('Touchdown Percentage', fontsize=14)
plt.ylabel('Passes Attempted', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

#a6p2 labels
players_to_label = ["Brock Purdy", "Tua Tagovailoa", "Josh Allen"]
label_offsets = [(0.5, -50), (1.5, 50), (-0.5, -25.0)]  # Different offsets for each player to spread out the arrows
for i, (index, row) in enumerate(data[data['Name'].isin(players_to_label)].iterrows()):
    offset = label_offsets[i % len(label_offsets)]
    plt.annotate(f"{row['Name']} ({row['Passes Attempted']}, {row['Touchdown Percentage']:.2f}%)",
                 xy=(row['Touchdown Percentage'], row['Passes Attempted']),
                 xytext=(row['Touchdown Percentage'] + offset[0], row['Passes Attempted'] + offset[1]),
                 arrowprops=dict(facecolor='black', arrowstyle="->"),
                 fontsize=12, color='black')

st.pyplot(plt)