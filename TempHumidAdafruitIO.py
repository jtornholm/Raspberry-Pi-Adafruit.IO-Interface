# SHT-30 Temperature/Humidity Sensor
# Sending Raspberry Pi senor data to Adafruit IO netork
# Receiving digital output from Adafriut IO
# By Jake Tornholm
# Williamsburg FLL November 2019

#import adafruit libraries
from Adafruit_IO import *
#Set Adafruit username and AIO key
aio = Client('', '')
digital = aio.feeds('digital')
digital2 = aio.feeds('digital2')

import time
import threading
import board
import digitalio
import busio
import adafruit_sht31d
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

#Relay Board Set up
relay = digitalio.DigitalInOut(board.D5)#GPIO pin on Raspbery pi
relay.direction = digitalio.Direction.OUTPUT
relay2 = digitalio.DigitalInOut(board.D6)
relay2.direction = digitalio.Direction.OUTPUT

def toFahrenheit(c):
    return float((c * 1.8) + 32)

def senddata():
    while True:
        c = (sensor.temperature)
        aio.send("temp", toFahrenheit(c))
        aio.send("humid", sensor.relative_humidity)
        #print(toFahrenheit(c)) #remove comment to print values in shell
        #print(sensor.temperature)
        #print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(60)#seconds
        
def receivedata():
    while True:
        data = aio.receive(digital.key)
        if str(data.value) == 'On':
            position = 1
            #print('received <- ON\n')
        elif str(data.value) == 'Off':
            position = 0
            #print('received <- OFF\n')
        # set the LED to the feed value
        relay.value = int(position)
        time.sleep(0.5)
        
def receivedata2():
    while True:
        data = aio.receive(digital2.key)
        if str(data.value) == 'On':
            position = 1
            #print('received <- ON\n')
        elif str(data.value) == 'Off':
            position = 0
            #print('received <- OFF\n')
        # set the LED to the feed value
        relay2.value = int(position)
        time.sleep(0.5)
        
thread1 = threading.Thread(target=receivedata)
thread1.start()

thread2 = threading.Thread(target=receivedata2)
thread2.start()

thread3 = threading.Thread(target=senddata)
thread3.start()
    
    

