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
    },
    {
        'question': "In Naruto, what is the name of Naruto's father?",
        'options': ["Minato Namikaze", "Kakashi Hatake", "Jiraiya", "Hiruzen Sarutobi"],
        'answer': "Minato Namikaze"
    },
    {
        'question': "In Attack on Titan, who is known as the 'Armored Titan'?",
        'options': ["Reiner Braun", "Eren Yeager", "Bertolt Hoover", "Levi Ackerman"],
        'answer': "Reiner Braun"
    },
    {
        'question': "In Dragon Ball Z, what is Goku's Saiyan birth name?",
        'options': ["Kakarot", "Bardock", "Raditz", "Vegeta"],
        'answer': "Kakarot"
    },
    {
        'question': "In One Piece, who is the captain of the Straw Hat Pirates?",
        'options': ["Monkey D. Luffy", "Zoro", "Sanji", "Shanks"],
        'answer': "Monkey D. Luffy"
    },
    {
        'question': "In Death Note, what is the real name of the character 'L'?",
        'options': ["L Lawliet", "Light Yagami", "Ryuk", "Near"],
        'answer': "L Lawliet"
    },
    {
        'question': "In Demon Slayer, what breathing style does Tanjiro initially learn?",
        'options': ["Water Breathing", "Flame Breathing", "Thunder Breathing", "Wind Breathing"],
        'answer': "Water Breathing"
    },
    {
        'question': "In My Hero Academia, what is Izuku Midoriya's hero name?",
        'options': ["Deku", "Shoto", "All Might Jr.", "Red Riot"],
        'answer': "Deku"
    },
    {
        'question': "In Hunter x Hunter, what is Gon Freecss's best friend's name?",
        'options': ["Killua Zoldyck", "Kurapika", "Leorio", "Hisoka"],
        'answer': "Killua Zoldyck"
    }
    ]

#use the random function that i imported

random.shuffle(questions)

score = 0

print ("......... Welcome to the Game .........")

for i, q in enumerate(questions, 1):
    print(f"Q {i}: {q['question']}")
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
print("Your final score is ",score)

