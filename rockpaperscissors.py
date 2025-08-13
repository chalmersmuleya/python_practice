import random

choices = ["rock", 'paper', 'scissors']
player_score = 0
computer_score = 0



def rockpaperscissors(player, computer):
    # Make inputs lowercase so 'Rock' or 'ROCK' also work
    player1 = player.lower()
    player2 = computer.lower()
    global player_score
    global computer_score
    

    if player1 == player2:
        return "Draw"
    player_score += 0
    computer_score += 0

    wins = {
        "rock": "scissors",   # rock beats scissors
        "scissors": "paper",  # scissors beats paper
        "paper": "rock"       # paper beats rock
    }
    
    if wins[player1] == player2:
        player_score += 1
        print()
        print("Player wins this round.")
        print(f"Player: {player_score} ... Computer: {computer_score}.") 
        print()

    elif player1 not in wins or player2 not in wins:
        return "Invalid move"
        
        
    else:
        computer_score += 1
        print()
        print("Computer wins this round.")
        print(f"Computer: {computer_score} ... Player: {player_score}")  
        print()


def finalScore():
    if player_score > computer_score:
        print(f"Player wins the game with {player_score} points while the Computer has {computer_score} points")
    
    elif player_score < computer_score:
        print(f"Computer wins the game with {computer_score} points while the Player has {player_score} points")
    
    else:
        print("It is a draw...")
        print(f'The Computer has {computer_score} points while the Player has {player_score} points')

def play():
    rounds = 3
    current = 1
    while current <= rounds:
        player = input("Rock, Paper or Scissors? ")
        computer = choices[random.randint(0,2)]
        rockpaperscissors(player,computer)
        current += 1

    finalScore()

play()
    



