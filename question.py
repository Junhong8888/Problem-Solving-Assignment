import random

def generate_random_number(start=1, end=10):
    return random.randint(start, end)

username = input("Enter your username: ")
print (f"Hello, {username}")
repeat = 0
while repeat < 1:

    question_num = 0
    score = 0
    options = ["A", "B", "C", "D"]
    MCQ = 0
    quit_or_continue = 0

    question = open("question.txt", "r")
    answer = open("answer.txt", "r")

    while MCQ < 10:
        lines = [question.readline() for _ in range(5)]
        if not any(lines):
            break
        for line in lines:
            print(line.strip())
        user_answer = input("Enter your answer(A/B/C/D): ").upper().strip()
        if user_answer in options:
            correct_answer = answer.readline().strip()
            if user_answer in correct_answer:
                print ("Correct")
                score += 1
            else:
                print (f"Incorrect, the correct answer is {correct_answer}")
            MCQ += 1
        else:
            print(f"The value '{user_answer}' is invalid. Please enter A, B, C, or D.")

    while question_num < 10:
        operators = ["+", "-", "*",]
        x = generate_random_number()
        y = generate_random_number()
        op = random.choice(operators)
        cor_ans = f"{x} {op} {y}"
        print (cor_ans)
        correct_ans = eval(cor_ans)

        try:
            ans = int(input("Enter your answer: ").strip())
        except ValueError:
            print ("Invalid input! Please re-enter a valid answer.")
            continue

        if ans == correct_ans:
            score += 1
            print ("correct")
        else:
            print (f"incorrect, the correct answer is {correct_ans}")
        question_num += 1
        
    print (f"Your score is {score} / 20")
    if score < 8:
        print("Don't be discouraged, keep up the good work")
    elif score < 16:
        print ("Not bad, let's challenge it once")
    elif score < 20:
        print ("Almost there, very close to the perfect score")
    else:
        print ("Congratulations, you got full marks")

    while quit_or_continue < 1:
        choice = ["Q", "C"]
        try:
            quit = str(input("Would you like to quit or challenge again? (press q to quit / press c to continue): ")).upper().strip()
        except:
            print ("Invalid input! Please re-enter a valid answer.")
            continue
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
