# def rockpaperscissors(player1,player2):
#     p1_score = 0
#     p2_score = 0
#     rock = 'rock'
#     paper = 'paper'
#     scissors = 'scissors'
#     #player1 logic ..rock 
#     if player1 == rock and player2 == paper:
#         return "player1 wins"
#     p1_score += 1


#     if player1 == rock and player2 == scissors:
#         return "player1 wins"
#     p1_score += 1
    

#     #player1 logic ..scissors 
#     if player1 == scissors and player2 == paper:
#         return "player1 wins"
#     p1_score += 1


#     if player1 == scissors and player2 == rock:
#         return "player2 wins"
#     p2_score += 1

#     #player1 logic ..paper
#     if player1 == paper and player2 == scissors:
#         return "player2 wins"
#     p2_score += 1


#     if player1 == paper and player2 == rock:
#         return "player1 wins"
#     p1_score += 1



#     #draw logic
#     if player1 == player2:
#         return "draw"
#     p1_score += 1
#     p2_score += 1
   

# #player2 logic ... rock
#     if player2 == rock and player1 == paper:
#         return "player1 wins"
#     p1_score += 1


#     if player2 == rock and player1 == scissors:
#         return "player2 wins"
#     p2_score += 1

# def finalScore():
       

# print(rockpaperscissors("paper","rock"))



def rockpaperscissors(player1, player2):
    # Make inputs lowercase so 'Rock' or 'ROCK' also work
    player1 = player1.lower()
    player2 = player2.lower()
    p1_score = 0
    p2_score = 0

    if player1 == player2:
        return "Draw"
    p1_score += 0
    p2_score += 0

    wins = {
        "rock": "scissors",   # rock beats scissors
        "scissors": "paper",  # scissors beats paper
        "paper": "rock"       # paper beats rock
    }
    if player1 not in wins or player2 not in wins:
        return "Invalid move"

    if wins[player1] == player2:
        p1_score += 1
        return "Player 1 wins this round. Player 1 has", p1_score,"points"
        
    else:
        p2_score += 1
        return "Player 2 wins this round. Player 2 has", p2_score,"points"
        


    



print(rockpaperscissors("rock", "paper"))