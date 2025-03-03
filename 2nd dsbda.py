
import pandas as pd 

data = {
    "Match 1": [45, 60, 20, 80, 55],
    "Match 2": [30, 50, 40, 90, 65],
    "Match 3": [70, 20, 35, 60, 40],
    "Match 4": [25, 45, 15, 100, 75],
}

play = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]
x = pd.DataFrame(data, index=play)

#Q1
hd = x.head(3)
print("First three rows:",hd)

# Q2
n_player, n_match = x.shape
print(f"players:{n_player}, matches:{n_match}")

# Q3
print("Matches:", x.columns.tolist())
print("Players:", x.index.tolist())

#Q4
print("Data type of the elements\n",x.dtypes)

#Q5
print("missing values?\n",x.isnull().sum().sum())


#Q6
print("Scores of Player 4 across all matches:\n",x.loc["Player 4"])


#Q7
print("Scores in Match 2:\n",x["Match 2"])

#Q8
print("\nScores of Player 1 and Player 3 for Match 1 and Match 4:")
print(x.loc[["Player 1", "Player 3"], ["Match 1", "Match 4"]])

#Q9
print("\n:Scores of the first 3 players and the first 2 matches:")
print(x.iloc[:3, :2])

#Q10
print("\nScore of Player 5 in Match 3:")
print(x.loc["Player 5", "Match 3"])

#Q11
x.loc["Player 2", "Match 4"] = 50
print("\nUpdated performance after changing Player 2's score in Match 4:")
print(x)

#Q12
x.loc["Player 6"] = [50, 40, 60, 70]
print("\nPerformance after adding Player 6:")
print(x)

 
#Q13
x = x + 10
print("\nPerformance after adding 10 bonus runs to each score:")
print(x)

#Q14
x.loc["Player 3"] = x.loc["Player 3"] - 5
print("\nPerformance after deducting 5 runs from Player 3:")
print(x)


#Q15
x["Total Runs"] = x.sum(axis=1)  # Total runs for each player across matches
print("\nTotal runs scored by each player:")
print(x["Total Runs"])


# 16. Calculate the total runs scored in each match
total_runs_per_match = x.drop(columns="Total Runs").sum(axis=0)  # Total runs per match (excluding 'Total Runs' column)
print("\nTotal runs scored in each match:")
print(total_runs_per_match)

# 17. Find the player with the highest total runs
highest_total_runs_player = x["Total Runs"].idxmax()
print("\nPlayer with the highest total runs:")
print(highest_total_runs_player)

# 18. Identify the match with the lowest total runs
lowest_total_runs_match = total_runs_per_match.idxmin()  # Find the match with lowest total runs
print("\nMatch with the lowest total runs:")
print(lowest_total_runs_match)

# 19. Compute the average runs scored by each player across all matches
average_runs_per_player = x["Total Runs"] / 5
print("\nAverage runs scored by each player:")
print(average_runs_per_player)

# 21. Sort the DataFrame by the "Total Runs" column in descending order
x_sorted = x.sort_values(by="Total Runs", ascending=False)
print("\nDataFrame sorted by Total Runs in descending order:")
print(x_sorted)

# 22. Filter the players who scored a total of more than 200 runs
players_over_200_runs = x[x["Total Runs"] > 200]
print("\nPlayers who scored more than 200 runs:")
print(players_over_200_runs)
