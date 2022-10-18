# Connect to network
import network
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'Password')

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

# I2C address, display size, I2C object and define lcd
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Turn backlight on
lcd.backlight_on()
# Send text to lcd
lcd.putstr("Temp in EFJY:")
# Move cursor to x,y
lcd.move_to(3,1)
# Send text to that position
lcd.putstr(txt[x+7:x+11])
lcd.putstr(" C")
       
