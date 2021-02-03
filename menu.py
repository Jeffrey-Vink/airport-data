import airport

class Menu:
	def __init__(self):
		menu_item = input("What would you like to do?\n\t")
		if menu_item == "list":
			list()
		elif menu_item == "help":
			help()
		elif menu_item == "exit":
			_exit()

		
	def help(self):
		print("Menu options:\n\thelp - brings up this menu")
		print("\tlist - displays all airports")
		main()
		

	def list(self):
		list_airports()
		main()
		
		
	def _exit(self):
		exit()