#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender

def door_sensor_callback(channel):
	if not GPIO.input(channel):
		print('CLOSED')
		val = 1
	else:
		print('OPEN')
		val = 0
	msg = {
		'sensorId': 0,
		'sensorType': 'DOOR_SENSOR',
		'value': val,
		'date': str(datetime.now()),
		'houseId': 1,
	}
	sender.send(msg)

# Configure Sender
sender = Sender()

# DOOR SENSOR
DOOR_SENSOR_PIN = 26
GPIO.setmode(GPIO.BCM) 
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(DOOR_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(DOOR_SENSOR_PIN, door_sensor_callback)

while True:
	time.sleep(1)
