import requests
from io import StringIO  

url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"

res = requests.request("GET", url).text

airports = res.splitlines(True)

for __airport in airports:
	_airport = __airport.split(",")
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
	print(airport["name"]+": "+airport["iata"])
