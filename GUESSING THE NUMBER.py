#GUESSING THE NUMBER GAME
import random as rnd
n=rnd.randint(0,100)
a=6
print("\n\t GUESSING THE NUMBER GAME ")
print("\nTOTAL NUMBER OF GUESSES YOU HAVE:",a)
while a!=0:
    num=int(input(" \nGUESS THE NUMBER FROM 1-100 :"))
    a=a-1
    if num==n:
        print("     \nYAYY!!!  GAME WON ")
        print("CONGRATS YOU HAVE WON THE GAME IN",6-a,"CHANCES") 
        break
    elif num>n:
        print('\nWRONG CHOICE, THE NUMBER IS SMALLER THAN',num)
    else:
        print('\nWRONG CHOICE, THE NUMBER IS GREATER THAN',num)
    if a!=0:
        print("TOTAL CHANCES REMAINING:",a)
if a==0 and num!=n:
    print("NO CHANCES LEFT")
    print("\nTHE NUMBER WAS",n)
    print("YOU LOST")
    print("     \n\t ***GAME OVER*** ")
