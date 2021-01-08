import random 
import pyfiglet
from termcolor import colored
def banner():
	print(pyfiglet.figlet_format("SnakeLadder"))
	print(
	'''
	-----------------------------------Code by shaan453
	-----------------------------------Version 2021.2.3
	'''
	)
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
			status = "Oops! You got Snake and you are now on "+str(currentPosition)+" from "+str(recordList[-1])
			print(colored(status,"red"))
		if (currentPosition in LadderList):
			lastPosition = currentPosition
			currentPosition = LadderList[currentPosition]
			recordList.append(lastPosition)
			status = "Good luck, you got ladder and you are now on "+str(currentPosition)+" from "+str(recordList[-1])
			print(colored(status,"green"))
		lastPosition = currentPosition
		recordList.append(lastPosition)
		print("You are currently on ",currentPosition)
	status = "Congratulation! You won the Snake and Ladder game."
	print(colored(status,"green"))

banner()
print("-------------------------Main-Menu-------------------------")
print("1. Start the game")
print("2. Exit the game")
print("-----------------------------------")
choice = int(input("Enter your choice"))
if (choice == 1):
	game()
elif (choice ==2):
	exit()
else:
	print("Invalid move")
