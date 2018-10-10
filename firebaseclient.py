import serial
import time
import requests
import json
from random import *
firebase_url = 'https://tvhealth-ifce.firebaseio.com/'
# Connect to Serial Port for communication
ser = serial.Serial('COM5', 9600, timeout=0)
# Setup a loop to send Temperature values at fixed intervals
# in seconds
fixed_interval = 1

while 1:
    try:
        # temperature value obtained from Arduino + LM35 Temp Sensor
        temperature_c = str(ser.readline()).split("'")[1].split("\\")[0]

        # current time and date
        time_hhmmss = time.strftime('%H:%M:%S')
        date_mmddyyyy = time.strftime('%d/%m/%Y')
        padrao = "%.2f" % uniform(0, 30)
        outro = randrange(1000, 2000)
        # current location name
        temperature_location = 'Brasil'
        print(temperature_c + ',' + time_hhmmss + ',' +
              date_mmddyyyy + ',' + temperature_location)

        # insert record
        data = {'temperatura': temperature_c,
                'frequencia': padrao,
                'bpm': outro, }
        result = requests.post(
            firebase_url + '/' + temperature_location + '/temperature.json', data=json.dumps(data))

        print('Record inserted. Result Code = ' +
              str(result.status_code) + ',' + result.text)
        time.sleep(fixed_interval)
    except IOError:
        print('Error! Something went wrong.')
    time.sleep(fixed_interval)
