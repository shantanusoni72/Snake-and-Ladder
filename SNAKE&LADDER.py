import random 
def game():
	print("The game have been started. \nYou are currently on position one.")
	throwOption = input("Instruction: Type 'D' to roll the die or 'E' to exit")
	if (throwOption == "D"):
		Play()
	elif (throwOption == "E"):
		exit()
	else:
		print("Invalid move")
def Play():
	dieList = [1,2,3,4,5,6]
	SnakeList = {25:3,59:1,56:48,69:32,83:57,91:73,94:26,99:80}
	LadderList = {4:14,9:31,20:38,28:84,36:44,42:63,51:67,62:81,71:90}
	recordList = []
	currentPosition = 0
	while currentPosition<100:
		throwOption = input("Type 'D' to roll")
		throw = random.choice(dieList)
		currentPosition = currentPosition + throw
		if (currentPosition in SnakeList):
			lastPosition = currentPosition
			currentPosition = SnakeList[currentPosition]
			recordList.append(lastPosition)
			print("Oops! You got Snake and you are now on ",currentPosition," from ",recordList[-1])
		if (currentPosition in LadderList):
			lastPosition = currentPosition
			currentPosition = LadderList[currentPosition]
			recordList.append(lastPosition)
			print("Good luck, you got ladder and you are now on ",currentPosition," from ",recordList[-1])
		lastPosition = currentPosition
		recordList.append(lastPosition)
		print("You are currently on ",currentPosition)
	print("Congratulation! You won the Snake and Ladder game.")

print("------SNAKE AND LADDER------")
print("1. Start the game")
print("2. Exit the game")
choice = int(input("Enter your choice"))
if (choice == 1):
	game()
elif (choice ==2):
	exit()
else:
	print("Invalid move")
