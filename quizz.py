# *************************************************************************
# Program: quizz.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC1L / TL2L
# Trimester: 2430
# Names: LOW JUN HONG | HU GUANG JING | CHONG YU HAN | TAN KHAI ZHEN
# IDs: 242FC243BZ | 242FC242G1 | 242FC241TV | 242FC242MB
# Emails:  LOW.JUN.HONG@student.mmu.edu.my | HU.GUANG.JING@student.mmu.edu.my | CHONG.YU.HAN@student.mmu.edu.my | TAN.KHAI.ZHEN@student.mmu.edu.my
# *************************************************************************



import json
import os
from datetime import datetime
from colorama import Fore
import pyfiglet
import random
from rich.console import Console
from rich.table import Table
from tabulate import tabulate

def leaderboard():
    """add rank and display result in leaderboard"""
    #Initial students to a empty list
    students = []

    #Load data and add into students
    with open("user.json","r") as file:
       data = json.load(file)
       for user in data["user_info"]:
        students.append(user)
       

    # Sort by score (descending) and time (ascending)
    sorted_students = sorted(students, key=lambda x: (-x["Score"], x["Time"]))

    # Reassign ranks based on the sorted order
    for rank, student in enumerate(sorted_students, start=1):
      student["Rank"] = rank

    # Create the table
    table = Table(title="Leaderboard")

    # Add table columns
    table.add_column("Rank", style="blue")
    table.add_column("Name", style="blue")
    table.add_column("Time", style="blue")
    table.add_column("Score", style="blue")

    # Add table rows
    for student in sorted_students:
      table.add_row(
        str(student["Rank"]),
        student["Name"],
        str(student["Time"]),
        str(student["Score"]),
      )

     # Print the table
    console = Console()
    console.print(table)

    #Write table into file
    with open("leaderboard.txt","w") as file:
       file.write(tabulate(sorted_students,headers="keys"))

    return    

def question():
    global score 
    score = 0
    question_num = 1
    
    def generate_random_number(start=1, end=20):
        return random.randint(start, end)
                          

    while question_num <= 20:
        print("------------------------")
        print(f"Question {question_num}")
        operators = ["+", "-", "*",]
        x = generate_random_number()
        y = generate_random_number()
        op = random.choice(operators)#randomly choose one of the value in operators
        cor_ans = f"{x} {op} {y}"#use f-string to add placeholder
        print (cor_ans)
        correct_ans = eval(cor_ans)#evaluate the answer
        #try and except to prevent error
        try:
            ans = int(input("Enter your answer: ").strip())
        except ValueError:
            print ("Invalid input! Please re-enter a valid answer.")
            continue
        #scoring
        if ans == correct_ans:
            score += 1
            print ("correct")
        else:
            print (f"incorrect, the correct answer is {correct_ans}")
        question_num += 1#change to next question
        

def track_time(start_time,end_time):
    """Track time """
    time_difference = end_time - start_time 
    total_seconds = time_difference.total_seconds() 
    hours = int(total_seconds // 3600) 
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
    return time_str


def admin_menu():
    """Super Admin Menu"""
    while True:
        print("\n--- Super Admin Menu ---")
        print("1. Add User")
        print("2. Remove User")
        print("3. Reset Leaderboard")
        print("4. Logout")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_user()
        if choice == "2":
            remove_user()
        if choice == "3":
            reset_leaderboard()
        if choice == "4":
            print("Logging out...")
            main()
            break
        if choice not in ["1", "2", "3", "4","5"]:
            print("Invalid choice, try again!")



def add_user():
    """Super Admin can manually add a user"""
    name = input("Enter new user name: ")
    if any(user["Name"] == name for user in user_data["user_info"]):
        print("User already exists!")
        return
    password = input("Enter a password: ")
    
    new_user = {
        "Name": name,
        "Password": password,
        "Time": "00:00:00",
        "Score": 0
    }
    
    user_data["user_info"].append(new_user)
    save_user()
    print(f"User '{name}' added successfully!")
    
def remove_user():
    """Super Admin can remove a user"""
    name = input("Enter the name of the user to remove: ")
    for user in user_data["user_info"]:
        if user["Name"] == name:
            user_data["user_info"].remove(user)
            save_user()
            print(f"User '{name}' has been removed.")
            return
    print("User not found!")
    

def reset_leaderboard():
    """Super Admin can reset the leaderboard"""
    for user in user_data["user_info"]:
        user["Score"] = 0
        user["Time"] = "00:00:00"
    
    save_user()
    print("Leaderboard has been reset!")
    

def login():
    """Authenticate existing user or Super Admin"""
    global current_user
    while True:
        name = input("Enter Your Name (Type 'Back' To Return Main Menu): ")
        if name.lower() == "back":
            main()
            return

        # Check if Super Admin
        if name == "SUPER_ADMIN_NAME" :
            password = input("Enter Super Admin Password: ")
            if password == "SUPER_ADMIN_PASSWORD":
                print("Super Admin Login Successful!")
                return admin_menu()            
            continue

        for user in user_data["user_info"]:
            if user["Name"] == name:
                attempts = 3
                while attempts > 0:
                    password = input("Enter Your Password: ")
                    if user["Password"] == password:
                        current_user = user
                        print("Login Successful!")
                        return play_game()
                    attempts -= 1
                    print(f"Login Failed. {attempts} attempts remaining.")
                print("Too Many Attempts!!! BYE BYE.")
                return main()
        
        print("Name Does Not Exist! Try Again...")

def load_user():
    """Load user data from JSON file"""
    if os.path.exists("user.json"):
        with open("user.json", "r") as file:
            return json.load(file)
    return {"user_info": []}

def save_user():
    """Save user data to JSON file"""
    with open("user.json", "w") as file:
        json.dump(user_data, file, indent=4)

def create_account():
    """Create a new user account"""
    while True:
        name = input("To Create Account, Enter A Name: ")
        if any(user["Name"] == name for user in user_data["user_info"]):
            print("Username Already Exists! Try Another One.")
            continue
        
        password = input("Enter A New Password: ")
        new_user = {
            "Name": name,
            "Password": password,
            "Time": "00:00:00",
            "Score": 0
        }
        user_data["user_info"].append(new_user)
        save_user()
        print("Account Created Successfully!!!")
        return login()



def play_game():
    """Main game logic"""
    global start_time
    start_time = datetime.now()
    
    # Display welcome message
    font = pyfiglet.figlet_format("Welcome  to  MATH  QUIZ ! ")
    print(Fore.YELLOW + font)
    
    #Display question 
    question()
    
    # Calculate final results
    end_time = datetime.now()
   
    
    # Update user data
    if current_user:
        current_user["Time"] = str(track_time(start_time,end_time))
        current_user["Score"] = score
        save_user()
    
    #show the score
    print (f"Your score is {score} / 20")

    if score < 8:
        print("Don't be discouraged, keep up the good work")
    elif score < 16:
        print ("Not bad, let's challenge it once")
    elif score < 20:
        print ("Almost there, very close to the perfect score")
    else:
        print ("Congratulations, you got full marks")

    print(f"Time Taken: {track_time(start_time,end_time)}")
    
    #Display Leaderboard
    leaderboard()

    main()

def main():
    """Main program flow"""
    global user_data, current_user
    user_data = load_user()
    current_user = None
    print("\nWelcome To The Quiz!")
    
    while True:
        choice = input("Do You Have an Existing Account? (yes/no/exit): ").lower()
        if choice == "exit":
            print("Goodbye!")
            return
        if choice == "yes":
            login()
            break
        elif choice == "no":
            create_account()
            break
        else:
            print("Invalid option. Please enter yes/no/exit.")

# Global variables
user_data = {"user_info": []}
current_user = None  # To track logged-in user
start_time = None    # To track quiz start time
qustion_number = 0 # Initial question_number            

if __name__ == "__main__":
    main()




