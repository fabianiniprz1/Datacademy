#rock, paper, scissors game

def rock_paper_scissors(item1,item2):
	if item1==item2:
		return 0
	elif item1 == 1 and item2 == 3 or item1 == 2 and item2 ==1 or item1 == 3 and item2 == 2:
		return 1
	else:
		return 2

def rock_paper_scissors_game():
	score_player1 = 0
	score_player2 = 0
	times = 1

	while times <= 3:

		print('Welcome to round ', str(times))

		player1_item = int(input('\nPlayer 1, is your time!...\nEnter your selection \n 1. Rock \n 2. Paper \n 3. Scissors: '))
		player2_item = int(input('\nPlayer 2, is your time!...\nEnter your selection \n 1. Rock \n 2. Paper \n 3. Scissors: '))

		if rock_paper_scissors(player1_item,player2_item) == 0:
			print('\nThis is a draw')
		elif rock_paper_scissors(player1_item,player2_item) == 1:
			print('\nPlayer 1 is winner')
			score_player1 += 1
		else:
			print('\nPlayer 2 is winner')
			score_player2 += 1

		print('\n')

		times += 1
	print('========================================================================\nGAME OVER\n========================================================================')
	if score_player1 == score_player2:
		print('========================================================================\nGAME OVER\n========================================================================')
		print("\nI'm so sorry, you are losers\n")
	elif score_player1 > score_player2:
		print('========================================================================\nPlayer 1 you are the best\n========================================================================')		
	else:	
		print('========================================================================\nPlayer 2 you are the best\n========================================================================')
		

	selection = int(input("Would you like to play again? \n1.Yes \n2.No: "))
	
	if selection == 1:
		rock_paper_scissors_game()
	if selection == 2:
		print("See you later")