#this one will have multiple choice
import random

# multiple choice questions
questions = [
    {
        'question' : "Who acts as Deadpool in the movie Deadpool?",
    'options' : ["Ryan Reynolds", "Robert Downey Jr", "Tom Holland", "Chris Hemsworth"],
    'answer' : "Ryan Reynolds"
    },


    {
        'question' : "Who acts as Ironman in the movie Ironman 3?",
    'options' : ["Ryan Reynolds", "Robert Downey Jr", "Tom Holland", "Chris Hemsworth"],
    'answer' : "Robert Downey Jr"
    },

    {
        'question' : "Who acts as Spiderman in the movie Captain America Civil War?",
    'options' : ["Ryan Reynolds", "Robert Downey Jr", "Tom Holland", "Chris Hemsworth"],
    'answer' : "Tom Holland"
    },

    {
        'question' : "What year was the first Avengers Movie released?",
        'options' : ["2012", "2015", "2013", "2011"],
        'answer' : "2012"
    }
    ]

#use the random function that i imported

random.shuffle(questions)

score = 0

print ("......... Welcome to the Game .........")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    options = q ['options'][:]
    random.shuffle(options)

    for idx, option in enumerate(options, 1):
        print(f"  {idx}. {option}")

# this makes sure that the 'game' does not crash or break when a person enters the wrong input
    while True:
        try:
            choice = int(input("Your answer (1 - 4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid Input!! Enter a number between 1 and 4.")



    if options[choice - 1] == q['answer']:
        print("You are correct")
        score += 1
    else:
        print("Wrong!! The answer is ", q['answer'])


# now i need to keep track of the score


