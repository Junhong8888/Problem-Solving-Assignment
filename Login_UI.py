##--Quiz login--##
import json
def save_creds(name,id):
     creds = {"Name":name, "ID":id}
     with open ("credentials.json","W") as file:
       json.dump(creds,file)
     print ("Name and ID Saved Successfully")

def login():
    correct_name = "Yuu"
    correct_id = "0808"
    attempts = 0
    
    while attempts < 3:
      name = input("Enter Your Name:")
      id = input("Enter Your Student ID:")

      if name == correct_name and id == correct_id:
        print ("Login Sucessful!")
        save_option = input("Do You Want To Save Your Credentials? (Yes/No):").strip().lower()
      if save_option == "Yes":
        save_creds(name,id)
        return True
    else:
        print ("Login Failed.Please Try Again.")
        attempts += 1
        print("Too Many Attempts!!! BYE BYE.")
        return False


print ("Welcome to THE MATH QUIZ!")