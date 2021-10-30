import random
user_score = 0
computer_score = 0
i = 1
print("|---------------------------|")
print("    SNAKE WATER GUN GAME        ")
print("|---------------------------|")
name = str(input("Enter your Name Please!\n"))
print("Welcome",name,"in a SNAKE WATER GUN GAME\n")
prmison = str(input("Enter yes for play game Or no for exit\n"))
if prmison == "yes" :
    print("OKk",name)
    while(i<=2) :

        print("type snake , water , gun for play the game\n")
        print(name,"turn!")
        user = str(input("Enter please\n"))
        print("Computer Turn!")
        list1 = ["snake","water","gun"]
        computer = random.choice(list1)
        print(computer)
        if user == "snake" and computer == "snake" :
            print("Match Drwa!")
            print("computer score=",computer_score)
            print("user score=",user_score)

        elif user == "water" and computer == "water":
            print("Match Drwa!")
            print("computer score=", computer_score)
            print("user score=", user_score)

        elif user == "gun" and computer == "gun" :
            print("Match Drwa!")
            print("computer score=", computer_score)
            print("user score=", user_score)

        elif user == "snake" and computer == "water" :
            print(name,"win!")
            print("computer score=", computer_score)
            user_score = user_score + 1
            print("user score=", user_score)

        elif user == "snake" and computer == "gun" :
            print("Computer win!")
            computer_score = computer_score + 1
            print("computer score=", computer_score)
            print("user score=", user_score)

        elif user == "water" and computer == "snake" :
            print("Computer win!")
            computer_score = computer_score + 1
            print("computer score=", computer_score)
            print("user score=", user_score)


        elif user == "water" and computer == "gun" :
            print(name,"win!")
            print("computer score=", computer_score)
            user_score = user_score + 1
            print("user score=", user_score)

        elif user == "gun" and computer == "snake" :
            print(name,"win!")
            print("computer score=", computer_score)
            user_score = user_score + 1
            print("user score=", user_score)

        elif user == "gun" and computer == "water" :
            print("computer win!")
            computer_score = computer_score + 1
            print("computer score=", computer_score)
            print("user score=", user_score)

        else :
            print("ERROR! you entered the wrong keyword")
        i = i + 1

else :
    print("OK! you doesn't want to play game...")
    exit()

print("|---------------------------|")
print("    SNAKE WATER GUN GAME        ")
print("|---------------------------|")
print("|---------------------------|")
print("|       TOTAL SCORE         |")
print("|---------------------------|")
print("| Computer total score:-",computer_score)
print("| user total score:-",user_score)



