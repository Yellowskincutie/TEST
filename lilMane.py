import random 
randomNumber = random.randint(1,20)
def guessingGame():
    print("Whats the number?")
    guess = int(input())
    if guess == randomNumber:
        print("GG\nDo it again!")
    else: 
        print("Wrong!")
        guessingGame()

guessingGame()        

        