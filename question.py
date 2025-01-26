# to generate random value
import random
#let the number randamly chosen from 1 to 10
def generate_random_number(start=1, end=10):
    return random.randint(start, end)

username = input("Enter your username: ")
print (f"Hello, {username}")
#loop for the whole question and let the user select to quit
repeat = 0
while repeat < 1:
    #initialize
    question_num = 0
    score = 0
    options = ["A", "B", "C", "D"]
    MCQ = 0
    quit_or_continue = 0
    #read files
    question = open("question.txt", "r")
    answer = open("answer.txt", "r")
    #set 10 mcq question and loop
    while MCQ < 10:
        #read the question.txt file 5 line by 5 line 
        lines = [question.readline() for _ in range(5)]
        #let it stop when no more line left
        if not any(lines):
            break
        #show the lines, use strip() to remove whitespaces
        for line in lines:
            print(line.strip())
        #make sure the user input are in options
        user_answer = input("Enter your answer(A/B/C/D): ").upper().strip()
        if user_answer in options:
            correct_answer = answer.readline().strip()
            if user_answer in correct_answer:
                print ("Correct")
                score += 1
            else:
                print (f"Incorrect, the correct answer is {correct_answer}")
            MCQ += 1#change to next question
        else:
            print(f"The value '{user_answer}' is invalid. Please enter A, B, C, or D.")

    #10 more question
    while question_num < 10:
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
    #ask the user want to quit or not
    while quit_or_continue < 1:
        choice = ["Q", "C"]#initialize
        #prevent error
        try:
            quit = str(input("Would you like to quit or challenge again? (press q to quit / press c to continue): ")).upper().strip()
        except:
            print ("Invalid input! Please re-enter a valid answer.")
            continue
        #prevent user form entering other value
        if quit not in choice:
            print ("Invalid input! Please re-enter a valid answer.")
            continue
        elif quit == "Q":
            repeat += 1
            quit_or_continue += 1
        else:
            quit_or_continue += 1
print (f"goodbye {username}")
print ("Hava a nice day!")
