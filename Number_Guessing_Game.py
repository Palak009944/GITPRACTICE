import random

print("LET'S PLAY A GAME")
print("INSTRUCTIONS:- YOU HAVE TO KEEP GUESSING THE NUMBER UNTIL YOU GUESS THE NUMBER CHOSEN RANDOMLY BY SYSTEM. NUMBER WILL BE FROM 1-100 (including 1 and 100)")
print("1) YOU WILL BE TOLD IF YOUR NUMBER IS HIGHER/LOWER THAN ACTUAL NUMBER AFTER EVERY GUESS")
print("2) YOU HAVE TO GUESS THE NUMBER IN MAXIMUM 10 TURNS")
print("3) GAME WILL STOP AS SOON AS YOU GUESS THE CORRECT NUMBER")
print("LET'S PLAY")

secret_number=random.randint(1,100)
N=1
won=False #did flagging
while (N<=10):
    guess=int(input("ENTER YOUR GUESS: "))
    if guess>secret_number:
        print("YOU HAVE ENTERED A NUMBER HIGHER THAN ACTUAL NUMBER")
    elif guess<secret_number:
        print("YOU HAVE ENTERED A NUMBER LOWER THAN ACTUAL NUMBER")
    elif guess==secret_number:
        print("GREAT GUESS. YOU WON!!!!!")
        won=True
        break
    N=N+1
if not won:
    print("Better luck next time")     
    print("Correct number was", secret_number)
