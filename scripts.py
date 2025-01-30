from rich.console import Console
from rich.table import Table
from tabulate import tabulate
import json


#Initialize students
students = []
   
with open("user.json","r") as file:
    file = json.load(file)
    for user in file['user_info']:
        students.append(user)

print(students)   


# Sort by score (descending) and time (ascending)
sorted_students = sorted(students, key=lambda x: (-x["Score"], x["Time"]))

# Reassign ranks based on the sorted order
for rank, student in enumerate(sorted_students, start=1):
    student["rank"] = rank

# Create the table
table = Table(title="Leaderboard")

# Add columns
table.add_column("Rank", style="blue")
table.add_column("Name", style="blue")
table.add_column("Time", style="blue")
table.add_column("Score", style="blue")

# Add rows
for student in sorted_students:
    table.add_row(
        str(student["rank"]),
        student["Name"],
        str(student["Time"]),
        str(student["Score"]),
    )

# Print the table
console = Console()
console.print(table)

with open("leaderboard.txt","w") as file:
    file.write(tabulate(sorted_students,headers="keys"))