import random
import string



#define play
def play():
    total_pscore = []
    total_cscore = []
    matrix = ((total_pscore, total_cscore))
    numGames = []#delete this if you see no use for it 6.29.18
    #input what the outcome will be if you continue playing
    continue_playing = True
    while continue_playing:
        player_score = 0
        cpu_score = 0
        
        #ask the player if they pick rock, paper, scissors
        player_choice = input('What will you choose? 1. Rock | 2. Paper | 3. Scissors: ')
        while player_choice not in ('1', '2', '3'):
            print('Try Again')
            player_choice = input('What will you choose?: ')
        cpu_choice = random.choice(('1', '2', '3'))

        if player_choice == cpu_choice:
            print("You Tied!")
            player_score += 1
            cpu_score += 1
            print('Your Score: ', player_score, '| CPU Score: ', cpu_score)
            print()
        elif player_choice == "1" and cpu_choice == "2":
            print("You Win!")
            player_score += 1
            print('Your Score: ', player_score, '| CPU Score: ', cpu_score)
            print()
        elif player_choice == "2" and cpu_choice == "1":
            print("You Lose!")
            cpu_score += 1
            print('Your Score: ', player_score, '| CPU Score: ', cpu_score)
            print()
        elif player_choice == "1" and cpu_choice == "3":
            print("You Win!")
            player_score += 1
            print('Your Score: ', player_score, '| CPU Score: ', cpu_score)
            print()
        elif player_choice == "3" and cpu_choice == "1":
            print("You Lose!")
            cpu_score += 1
            print('Your Score: ', player_score, '| CPU Score: ', cpu_score)
            print()
        elif player_choice == "2" and cpu_choice == "3":
            print("You Lose!")
            cpu_score += 1
            print('Your Score: ', player_score, '| CPU Score: ', cpu_score)
            print()
        elif player_choice == "3" and cpu_choice == "2":
            print("You Win!")
            player_score += 1
            print('Your Score: ', player_score, '| CPU Score: ', cpu_score)
            print()
        
        play_again = input("Play again?: ")
        while play_again not in ("Yes", "No"): #validate user input
            print("Try Again")
            play_again = input("Play again?: ")
        if play_again == "Yes":
            continue_playing = True
            total_pscore.append(player_score)
            total_cscore.append(cpu_score)
            x = [[sum(total_pscore)], [sum(total_cscore)]]
            print()
            print('YOUR SCORE TOP/CPU SCORE BOTTOM:')
            for i in range(len(x)):
                for j in range(len(x[i])):
                    print(x[i][j])
                    print()
            
        elif play_again == "No":
            total_pscore.append(player_score)
            total_cscore.append(cpu_score)
            x = [[sum(total_pscore)], [sum(total_cscore)]]
            print("Game Over")
            print()
            print('\t\t\tYOUR GAME SUMMARY')
            print('______________________________________________________________________')
            print('Score Board: ')
            print('Total Player Score:', sum(total_pscore), '| Total CPU Score: ', sum(total_cscore))
            print()
            print()
            print('Number of Games Played: ')
            print(len(total_pscore))
            print('______________________________________________________________________')
            print()
            continue_playing = False
        
                
            
            

def game_start():
    while True:
        begin = input("Would you like to play Rock, Paper, Scissors? Type Yes or No: ")
        if begin == "Yes":
            play()
        elif begin == "No":
            print('Goodbye')
            break


game_start()

    
