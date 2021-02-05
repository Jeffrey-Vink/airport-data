from airport import *
import_of_airports = True


class Menu:
	def __init__(self):
		self.initialize()
		self.main()
		
		
	def main(self):
		menu_item = input("What would you like to do?\n\t")
		if menu_item == "list":
			self.list()
		elif menu_item == "help":
			self.help()
		elif menu_item == "exit":
			self._exit()
		else:
			self.invalid_menu_choice()
	
	
	def invalid_menu_choice(self):
		print("Invalid input, type 'help' to view valid options")
		self.main()
	
		
	def help(self):
		print("Menu options:\n\thelp - brings up this menu")
		print("\tlist - displays all airports")
		print("\texit - stops the application")
		self.main()
		

	def list(self):
		list_airports()
		self.main()
		
		
	def _exit(self):
		exit()
		
	
	def initialize(self):
		print("Import airports: "+str(import_of_airports))
	
		if import_of_airports:
			res = requests.request("GET", url).text
	
		import_airports(res)