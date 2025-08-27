# so this is the game where you will be playing scissors , paper and rock

                              #Rock , Paper and Scissors

import random
#so this ramdom makes computer/programe to choose  random value
print("****************************************")
print("lets See who comes to the top   :)")
print("****************************************")
print("                                        ")
print("****************************************")


options = ("rock" , "paper" , "scissors") 
running = True

#now we are going to put some loop by using while

while running:
	player = None
	computer = random.choice(options)

	while player not in options:
		player  = input("Select an option Rock , Paper , Scissors : ").lower()
	
	print(f"player: {player}")
	print(f"computer : {computer}")



#now the condition 

	if player == computer:
		print("you are a Tough! player, its a Tie!!")

	elif player == "rock" and computer == "scissors" :
		print("you are amazing, you win!!")

	elif player == "paper" and computer == "rock" :
		print("you are awsome. YOU win!!")

	elif player == "scissors" and computer == "paper":
		print("It's hard to beat you, guess what you Win!!")

	else:
		print("sorry, But you lose!!")

	run = input("press 'q'to quit or press any other key to continue ::").lower()

	if run == "q":
		break

Print("Thank you for playing game with me")
