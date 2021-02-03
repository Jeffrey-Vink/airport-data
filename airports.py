import requests
from io import StringIO  

##Data to be retrieved
url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
res = ""
##Other variables
import_of_airports = True
unformatted_airports = ""
airports = list()


def __init__():
	print("Import airports: "+str(import_of_airports))
	
	if import_of_airports:
		res = requests.request("GET", url).text
	
	import_airports(res)
	list_airports(airports)


def import_airports(res):
	print("Importing airports...")
	unformatted_airports = res.splitlines(True)
	define_airports(unformatted_airports)


def define_airports(unformatted_airports):
	print("Defining airports...")
	for unformatted_airport in unformatted_airports:
		_airport = unformatted_airport.split(",")
		airport = dict()
		airport["id"] = _airport[0]
		airport["name"] = _airport[1]
		airport["city"] = _airport[2]
		airport["country"] = _airport[3]
		airport["iata"] = _airport[4]
		airport["icao"] = _airport[5]
		airport["latitude"] = _airport[6]
		airport["longitude"] = _airport[7]
		airport["altitude"] = _airport[8]
		airport["timezone"] = _airport[9]
		airport["dst"] = _airport[10]
		airport["tz"] = _airport[11]
		airport["type"] = _airport[12]
		airport["source"] = _airport[13]
		airports.append(airport)
	
	
def list_airports(airports):
	for airport in airports:
		print(airport["name"]+": "+airport["iata"])
		print("\tLocation: "+airport["latitude"]+", "+airport["longitude"])
		print("\tType: "+airport["type"])
		
__init__()