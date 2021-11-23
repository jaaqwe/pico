from machine import Pin
import utime

# Objects for pins trigger and echo in HC-SR04
pin_trigger = Pin(1, Pin.OUT)
pin_echo = Pin(0, Pin.IN)

# Red led for too close and Green led for not too close
led_red = Pin(2, Pin.OUT)
led_green = Pin(3, Pin.OUT)

# Define object for motor output, Setting pins to output
motor_tr = machine.Pin(16, machine.Pin.OUT)

# Define object for button, Setting pins to input
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

import time
timer1_start = time.time()

while True:

    # If input, turn motor on/off
    if button.value() == 1:
        motor_tr.value(1)
        print ("motor")
        utime.sleep(0.22)
        print ("motor off")
        motor_tr.value(0)



    if time.time() - timer1_start > 1:
        timer1_start = time.time()

        # Pull the trigger low and pause
        pin_trigger.low()
        utime.sleep_us(2)

        # Pull the trigger high for 5 us
        pin_trigger.high()
        utime.sleep_us(5)

        # Pull the trigger low
        pin_trigger.low()

        # Wait when echo is low and add timestamp for it
        while pin_echo.value() == 0:
            signal_off = utime.ticks_us()

        # Wait when echo is high and add timestamp for it
        while pin_echo.value() == 1:
            signal_on = utime.ticks_us()

        # Calculate time between on and of signal
        timepassed = signal_on - signal_off

        # Multiply the jorney time by the speed of sound 0.0343 cm per microsecond
        object_distance = (timepassed * 0.0343) / 2

        print("The distance from object is ",object_distance,"cm")

        # if object is too close ligth up the Red Led
        if object_distance > 10:
            led_red.value(1)
            led_green.value(0)

        # if object is too close ligth up the Green Led
        if object_distance < 10:
            led_red.value(0)
            led_green.value(1)

    # Sleep one second
    #utime.sleep(1)
