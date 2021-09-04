import random
"""
rock vs paper --> paper win
paper vs scissors --> scissors win
scissors vs rock --> rock win
"""
l = ["rock", "paper", "scissors"]

while True:
    user_count = 0
    computer_count = 0
    choice_to_play = int(input("""
Do you want to play?
1 yes
2 No | Exit
type 1 or 2:    """))
    if choice_to_play == 1:
        for i in range(1, 6):
            user_input = int(input("""
            1 Paper
            2 Rock
            3 Scissors
            Please enter your choice: 
            """))
            if user_input == 1:
                user_choice = "paper"
            elif user_input == 2:
                user_choice = "rock"
            elif user_input == 3:
                user_choice = "scissors"

            computer_choice = random.choice(l)
            if user_choice == computer_choice:
                print("User Choice: ", user_choice)
                print("Computer Choice: ", computer_choice)
                print("Match Draw")
                user_count += 1
                computer_count += 1
            elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper"):
                print("User Choice: ", user_choice)
                print("Computer Choice: ", computer_choice)
                print("You Win")
                user_count += 1
            else:
                print("User Choice: ", user_choice)
                print("Computer Choice: ", computer_choice)
                print("Computer Win")
                computer_count += 1

        print("***** Final Result *****")
        if user_count == computer_count:
            print("Your Total Point: ", user_count)
            print("Computer Total Point: ", computer_count)
            print("Match Draw")
        elif user_count > computer_count:
            print("Your Total Point: ", user_count)
            print("Computer Total Point: ", computer_count)
            print("You Win")
        else:
            print("Your Total Point: ", user_count)
            print("Computer Total Point: ", computer_count)
            print("Computer Win")

    else:
        break

