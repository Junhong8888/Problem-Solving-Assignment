from rich.console import Console
from rich.table import Table

# Data: List of dictionaries
students = [
    {"name": "Low", "id": "243", "time": 25, "score": 10},
    {"name": "Jun", "id": "242", "time": 24, "score": 12},
    {"name": "May", "id": "244", "time": 23, "score": 12},
]

# Sort by score (descending) and time (ascending)
sorted_students = sorted(students, key=lambda x: (-x["score"], x["time"]))

# Reassign ranks based on the sorted order
for rank, student in enumerate(sorted_students, start=1):
    student["rank"] = rank

# Create the table
table = Table(title="Leaderboard")

# Add columns
table.add_column("Rank", style="blue")
table.add_column("Name", style="blue")
table.add_column("ID", style="blue")
table.add_column("Time", style="blue")
table.add_column("Score", style="blue")

# Add rows
for student in sorted_students:
    table.add_row(
        str(student["rank"]),
        student["name"],
        student["id"],
        str(student["time"]),
        str(student["score"]),
    )

# Print the table
console = Console()
console.print(table)
