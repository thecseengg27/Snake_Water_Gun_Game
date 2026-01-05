#Rule of the game:
"""
Snake drinks Water → Snake wins

Water douses Gun → Water wins

Gun kills Snake → Gun wins

"""
#there is a module for generating random numbers:
import random
computer = random.choice([1,0,-1])
youstr = input("Enter your choice either s for Snake, w for Water, g for Gun:")
youdict = {"s": 1,"w":-1,"g":0}
compdict = {1:"s",-1:"w",0:"g"}
you = youdict[youstr]
comp = compdict[computer]
#why we do this like --> dict is there we choose s if s and the dictionary is selsected it gets saved in you 
print(f"You chose:{you}\n and Computer chose:{comp}")
#since we already assigned string value the dict key must be string they must be same
#but if we do this like its pointing to something went wrong
#so thereby, our input must be string and computer input must be integer


# so in the output we will be using string it returns the number assigned and viceversa for computer.
'''
if (computer == you):
    print("Its Draw")

else:
    if (computer == -1 and you == 1): #w+s=s wins
        print("You Won")
    elif (computer == -1 and you == 0):#w+g=w wins
        print("You Lose")
    if (computer == 0 and you == -1):#G+w=w wins
        print("You Won") 
    elif(computer == 0 and you ==1):#g+s=g win
        print("You Won")
    if (computer == 1 and you == 0):#s+g=g win
        print("You won")
    elif (computer == 1 and you == -1):#s+w=s
        print("You Lose")

'''   
# now lets use a logic like computer - you 
'''
-1 - 1 = -2 =>-2 you win 
-1-0=-1 =>-1 you lose
0--1= 1 =>1 you win
0--1= 1 =>you win
1-0= 1 =>=1 you lose
1--1= 2 =>2 you lose
'''
#you win on 1,-2 so...,

if (computer == you):
    print("Its Draw")

elif(computer - you == 1 or computer-you == -2):
    print("You Won")

elif(computer-you == -1 or computer-you == 2 ):
    print("You Lose")

