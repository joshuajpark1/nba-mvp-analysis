# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load a dataset (replace with the path to one of your CSV files)
data = pd.read_csv('../data/play_off_totals_2010_2024.csv')

# Quick overview of the dataset
print(data.head())  # Display the first 5 rows
print(data.info())  # Display dataset information

# Example Analysis: Points per Game (PPG)
data['PPG'] = data['Points'] / data['Games']

# Display top 10 scorers based on PPG
top_scorers = data[['Player', 'PPG']].sort_values(by='PPG', ascending=False).head(10)
print("Top 10 Scorers by PPG:")
print(top_scorers)

# Create a bar chart for the top 10 scorers
plt.barh(top_scorers['Player'], top_scorers['PPG'], color='skyblue')
plt.xlabel('Points Per Game (PPG)')
plt.ylabel('Player')
plt.title('Top 10 Scorers (Playoffs, 2010-2024)')
plt.gca().invert_yaxis()  # Reverse the order of players
plt.show()

plt.savefig('../visuals/top_10_scorers_playoffs.png')
