import pandas as pd
import matplotlib.pyplot as plt

# Path to the dataset
playoff_totals_path = '../data/NBA-Data-2010-2024-main/play_off_totals_2010_2024.csv'

# Load the dataset
try:
    playoff_totals = pd.read_csv(playoff_totals_path)
    print("Playoff Totals Dataset Loaded Successfully!")
    print(playoff_totals.head())  # Display the first 5 rows

    # Inspect all column names
    print("\nColumns in the dataset:")
    print(playoff_totals.columns)
except FileNotFoundError:
    print(f"File not found: {playoff_totals_path}")

# Example Analysis: Points Per Game (PPG)
points_column = 'PTS'  # Points column

if points_column in playoff_totals.columns:
    # Group by player or team to count the number of games played
    games_played = playoff_totals.groupby('TEAM_NAME').size()  # Replace with 'Player' if needed
    points = playoff_totals.groupby('TEAM_NAME')[points_column].sum()  # Total points by team/player

    # Calculate Points Per Game (PPG)
    ppg = points / games_played
    top_scorers = ppg.sort_values(ascending=False).head(10)
    print("\nTop 10 Scorers by Points Per Game (PPG):")
    print(top_scorers)

    # Create and save a visualization
    top_scorers.plot(kind='barh', color='blue')
    plt.xlabel('Points Per Game (PPG)')
    plt.ylabel('Team')
    plt.title('Top 10 Scorers (Playoffs 2010-2024)')
    plt.gca().invert_yaxis()  # Reverse the order of players for better readability
    plt.savefig('../visuals/top_10_scorers_playoffs.png')
    plt.show()
else:
    print(f"Error: The dataset does not contain '{points_column}' column.")

# Top 10 teams/players by total points
if 'PTS' in playoff_totals.columns:
    top_teams = playoff_totals.groupby('TEAM_NAME')['PTS'].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 Teams by Total Points:")
    print(top_teams)
else:
    print("Error: The dataset does not contain 'PTS' column.")

# Total games per team
games_per_team = playoff_totals.groupby('TEAM_NAME').size()
print("\nTotal Games Per Team:")
print(games_per_team)

# Bar chart for top 5 teams by total points
if 'PTS' in playoff_totals.columns:
    top_5_teams = playoff_totals.groupby('TEAM_NAME')['PTS'].sum().sort_values(ascending=False).head(5)
    top_5_teams.plot(kind='bar', color='skyblue')
    plt.title('Top 5 Teams by Total Points')
    plt.xlabel('Team')
    plt.ylabel('Total Points')
    plt.savefig('../visuals/top_5_teams_points.png')  # Save the chart
    plt.show()  # Display the chart
else:
    print("Error: The dataset does not contain 'PTS' column.")

# Print all column names
print("\nColumn Names in Dataset:")
print(playoff_totals.columns)
