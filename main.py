import random

print("----Let's Bigin the Game----")

Player_score = 0
Computer_score = 0

Name = input("Please enter your name:")

print("""
Games Rules:
1) Paper vs Rock --> Paper win
2) Scissor vs Paper --> Scissor win
3) Rock vs Scissor --> Rock win 
""")

while True:
    player = int(input('''
 1- Start The Game
 2- Exit
    '''))
    if player==1:
        for i in range(1,5):
            print("""Choices are:
            Rock = 1
            Paper = 2
            Scissor = 3
            """)

            option = int(input("Your Turn choose from 1-3:"))

            while (option > 3 or option < 1):
                option = int(input("Please enter valid number"))

            if option == 1:
                your_choice = "Rock"
            elif option == 2:
                your_choice = "Paper"
            else:
                your_choice = "Scissor"

            print("You chose:-",your_choice)

            print("Computer Turn....")

            RandNo = random.randint(1, 3)

            if RandNo == 1:
                comp_choice = "Rock"
            elif RandNo == 2:
                comp_choice = "Scissor"
            else:
                comp_choice = "Paper"

            print("Computer chose:-",comp_choice)

            if(your_choice == comp_choice):
                print("This game is tie!")
                Player_score = Player_score
                Computer_score = Computer_score

            elif ((your_choice == "Paper" and comp_choice == "Rock") or (your_choice == "Rock" and comp_choice == "Scissor") or (your_choice == "Scissor" and comp_choice == "Paper")):
                print("You Win!")
                Player_score = Player_score+1

            else:
                print("Computer Win!")
                Computer_score = Computer_score+1

        if Player_score==Computer_score:
            print("!!!--Game Draw--!!!"
            )
            print("Your Score",Player_score)
            print("Computer Score",Computer_score)

        elif Player_score>Computer_score:
            print("!!!!---",Name,"Win The Finel Game---!!!!")
            print("Your Score", Player_score)
            print("Computer Score", Computer_score)

        else:
            print("!!!!---Computer Win The Finel Game---!!!! ")
            print("Your Score", Player_score)
            print("Computer Score", Computer_score)

    else:
        break




