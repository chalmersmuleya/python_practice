import random 

guessNumber = random.randint(1,15)
score = 20

while True:
    UserGuessNumber = int(input("Guess: "))

    if UserGuessNumber == guessNumber:
        print ("You got it correct, your score is " + str(score))
        break
    else:
        print("You got it wrong, Better luck next time!!!!")
        score -= 1