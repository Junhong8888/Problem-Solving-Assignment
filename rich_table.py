from rich.console import Console
from rich.table import Table

# Player information
name = ("Low","Jun")
id = ("243","242")
time = ("25","24")
score = ("10","12")
rank = ("1","2")
student_info = (name,id,time,score,rank)



table = Table(title= "Leaderboard")

table.add_column("Rank",style= "blue")
table.add_column("Name",style= "blue")
table.add_column("ID",style= "blue")
table.add_column("Time",style= "blue")
table.add_column("Score",style= "blue")

i = 0 
while i < len(name):
    table.add_row(rank[i],name[i],id[i],time[i],score[i])
    i += 1
console = Console()
console.print(table)