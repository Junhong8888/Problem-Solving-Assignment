from prettytable import PrettyTable

# Player information
name = "Low"
id = "243"
time = 25
score = 10
rank = 1

# Function to get player data
def leaderboard():
    return rank, name, id, time, score

# Create PrettyTable
table = PrettyTable()

# Define field names (columns)
table.field_names = ["Rank", "Name", "ID", "Time", "Score"]

# Add row to the table with player data
table.add_row(leaderboard())

# Align columns
table.align["Rank"] = "l"
table.align["Name"] = "c"
table.align["ID"] = "c"
table.align["Time"] = "c"
table.align["Score"] = "r"

# Sort rows (if there are multiple rows)
# Note: Sorting requires multiple rows and a `sortby` parameter
# table.sortby = "Rank"

# Print the table
print(table)