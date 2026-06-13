
Questions = ["What is my favorite color?: ", "What is my favorite sport?: ", "what is my favorite music?: ", "How can you do a function?: ",
             "What is the technology i most use?: "]
answer = ["blue", "swimming", "jazz", "def", "phone"]
score = 0
max_score = 5
while True:
    for i in range(5):

        User_Answer = input(Questions[i])
        if User_Answer.lower() == answer[i]:
            score += 1

    else:
        print(f"You have {score}/{max_score}")
        if score == max_score:
            print("Congratulations you won")
        User_Answer = input("Do you want to try again? (y/n)")
        if User_Answer.lower() == "n":
            break
