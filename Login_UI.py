import json
import os

user = {}

def load_user():
    if os.path.exists("user.json"):
        with open("user.json","r") as file:
            return json.load(file)
    return {}
   
def save_user():
   with open ("user.json","w") as file:
       json.dump (user, file)

def create_Account():
    name = input("To Create Account, Enter A Name: ")
    if name in user:
        print("Username Already Exist! Try Annother One.") 
        create_Account()
   
    else:
        password = input ("Enter A New Password: ")
        user[name] = password
        save_user()
        print ("Account created Successfully!!!")
        login()
        

def login():
    name = input("Enter Your Name (Type 'Back' To Return Main Menu):  ")
    if name.lower() == "back" :
        main()
        return
    if name not in user:
       print ("Name Does Not Exist! Try Again...")
       login()
    else:
        attempts = 3
        while attempts > 0:
            id = input("Enter Your Password/ID: ")
            if user[name] == id:
                print ("Login Sucessful!")
                play_game()
                return 
            else:
                attempts -= 1
                print ("Login Failed.Please Try Again.")
        print("Too Many Attempts!!! BYE BYE.")
        main()

def play_game():
   print ("Welcome to THE MATH QUIZ!")

def main():
    global user
    user = load_user()
    print("Welcome To The Quiz!")
    choice = input ("Do You Have an Existing Account? (yes/no): ").lower()
    if choice == "yes" :
        login()

    elif choice == "no" :
        create_Account()

    else: 
        print ("Not An Option. Please Enter YES or NO. ")
        main()

if __name__ == "__main__":
  main()

      