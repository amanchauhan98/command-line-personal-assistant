# stone paper scissor game
import random
from pygame import mixer
def musiconloop(file,stopper) :
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


user_score = 0
computer_score = 0
print("|---------------------------|")
print("  STONE, PAPER AND SCISSOR  ")
print("|---------------------------|")
name = str(input("Enter your name\n"))
print("Write stone,paper and scissor for play the game\n")
ready = str(input("Are you ready to play the game (yes/no)?\n"))
if ready == "yes" :
    print("Ok!! Good luck")
    print("Your Turn",name)
    user = str(input())
    print("Computer Turn")
    list1 = ["stone","paper","scissor"]
    computer = random.choice(list1)
    print(computer)
    if user == "stone" and computer == "stone" :
        print("Match Draw")
        musiconloop('physical.mp3','stop')
    elif user == "paper" and computer == "paper" :
        print("Match Draw")
        musiconloop('physical.mp3','stop')
    elif user == "scissor" and computer == "scissor" :
        print("Match Draw")
        musiconloop('physical.mp3','stop')
    elif user == "stone" and computer == "paper" :
        print("Computer Won")
        computer_score = computer_score + 1
        print("Computer score :",computer_score)
        musiconloop('water.mp3','stop')
    elif user == "stone" and computer == "scissor" :
        print(name,"won")
        user_score = user_score + 1
        print(f"{name} score :",user_score)
        musiconloop('water.mp3','stop')
    elif user == "paper" and computer == "stone" :
        print(name,"won")
        user_score = user_score + 1
        print(f"{name} score :",user_score)
        musiconloop('water.mp3','stop')
    elif user == "paper" and computer == "scissor" :
        print("computer won")
        computer_score = computer_score + 1
        print("Computer score :",computer_score)
        musiconloop('water.mp3','stop')
    elif user == "scissor" and computer == "stone" :
        print("computer won")
        computer_score = computer_score + 1
        print("Computer score :",computer_score)
        musiconloop('water.mp3','stop')
    elif user == "scissor" and computer == "paper" :
        print(name,"won")
        user_score = user_score + 1
        print(f"{name} score :",user_score)
        musiconloop('water.mp3','stop')
    else :
        print("you Entered the wrong keyword")

elif ready == "no" :
    print("OK!! you doesn't want to play")
    exit()

