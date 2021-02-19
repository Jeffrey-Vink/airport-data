import requests
from io import StringIO  

##Data to be retrieved
url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
res = ""
##Other variables
import_of_airports = True
unformatted_airports = ""
airports = list()


class Airport:
	def __init__(self, unformatted_airport):
		_airport = unformatted_airport.split(",")
		self.id = _airport[0]
		self.name = _airport[1]
		self.city = _airport[2]
		self.country = _airport[3]
		self.iata = _airport[4]
		self.icao = _airport[5]
		self.latitude = _airport[6]
		self.longitude = _airport[7]
		self.altitude = _airport[8]
		self.timezone = _airport[9]
		self.dst = _airport[10]
		self.tz = _airport[11]
		self.type = _airport[12]
		self.source = _airport[13]
		airports.append(self)
		
		
	def list_airport(self):
		print(self.name+": "+self.iata)
		print("\tLocation: "+self.latitude+", "+self.longitude)
		print("\tType: "+self.type)
		print("\tTimezone: "+self.timezone)
        ##print("\tTimezone: "+self.timezone)
		
		
def import_airports(res):
	print("Importing airports...")
	unformatted_airports = res.splitlines(True)
	for unformatted_airport in unformatted_airports:
		airports.append(Airport(unformatted_airport))
	
	
def list_airports():
	for airport in airports:
		airport.list_airport()
