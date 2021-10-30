score = 0
def even(a) :
    if a%2 == 0:
        return f"correct! its a even number"
    else :
        return f"sorry! Wrong answer. Its a Even number"         
def odd(a):
    if a%2 != 0:
        return f"correct! its a odd number" 
    else :
        return f"sorry! Wrong answer. Its a odd number"    
def prime(a) :
    if a%2 == 0 or a%3 == 0:
        return f"sorry! its a wrong answer. its a prime number"
    else:
        return f"correct! its a prime number"
                 
        


import random
i = 1

print("|-----------------------|")
print("  ODD EVEN PRIME GAME")
print("|-----------------------|")
print("             by Aman chauhan")
name = str(input("Enter your name Please!\n"))
n = int(input("how many times you want to play\n"))
print(f"Ok! {name}  Lets Play the game...")
while(i<n):

    number = [1,2,3,4,5,6,7,8,9,0]  

    a = random.choice(number)
    print(f"{a} is which type of number? [1] ODD [2] EVEN [3] PRIME")
    answer = int(input("Enter your answer here:\n"))
    if answer == 1:
        print(odd(a))
        score = score + 1
        print("score is",score)
    elif answer == 2:
        print(even(a))
        score = score + 1
        print("score is",score)
    elif answer== 3:
        print(prime(a)) 
        score = score + 1
        print("score is",score)
    i = i + 1           



