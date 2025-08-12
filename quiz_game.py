# a mini quiz game thats not too complicated

questions = [
    {'question': "What year was the movie Avengers Infinity War released in?",'answer' : "2018"},
    {'question': "What year was the movie Deadpool released in?",'answer' : "2016"},
    {'question': "Who is Thor's brother?",'answer' : "Loki"}
]

score = 0

for q in questions :
    user_answer = input(q['question'] + " ").strip().lower()
    if user_answer == q['answer']:
        print("You're correct")
        score += 2
    else:
        print("Wrong!!! The correct answer is ",q['answer'])
        score -= 2

print("Your final score is ", score)        