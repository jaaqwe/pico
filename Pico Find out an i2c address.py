import machine

# I2C bus connection, SDA the data, SDL the clock
# Raspbery Pi Pico documents blue pins are I2C bus
sda=machine.Pin(0)
scl=machine.Pin(1)

# Define bus for I2C
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

# Print out address for I2C
print('I2C address:')
print(i2c.scan(),' (decimal)')
print(hex(i2c.scan()[0]), ' (hex)')
