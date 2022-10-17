# Connect to network
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'password')

# Make GET request
# Get Metar from aviationweather.gov for EFJY
import urequests
r = urequests.get("https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&mostRecent=true&stationString=efjy")
#Convert to str
txt = r.content.decode('utf-8')
r.close()

#Find temp from XML file, store the first occurrence of the specified value to x
x = txt.index("temp")
#Print temp, slicing string in positon x+7 and x+11 and show the slice
print("Temperature in EFJY: " + txt[x+7:x+11] + "\u00B0")

       
