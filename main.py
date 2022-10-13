from snake_and_ladder import *

if __name__ == '__main__':
	g = snake_and_ladder()
	g.banner()
	choice = g.menu()
	if (choice == 1):
		g.game()
	elif (choice ==2):
		exit()
	else:
		print("Invalid move")
