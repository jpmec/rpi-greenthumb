"""
Sensor module for the DS18B20 temperature sensor.

Borrowed heavily from:
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/software
"""

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

BASE_DIR = '/sys/bus/w1/devices/'
DEVICE_DIR = glob.glob(BASE_DIR + '28*')[0]
DEVICE_FILE = DEVICE_DIR + '/w1_slave'


def _read():
    """
    Read raw file contents
    """
    with open(DEVICE_FILE, 'r') as open_file:
        lines = open_file.readlines()

    return lines


def read(units='C', timeout=2, sleeptime=0.2):
    """
    Read the temperature

    WARNING: THIS IS A BLOCKING CALL
    """
    lines = _read()

    tries = 0
    while lines[0].strip()[-3:] != 'YES':
        tries += sleeptime

        if tries > timeout:
            return None

        time.sleep(sleeptime)
        lines = _read()

    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0

        if units == 'F':
            return (temp_c * 9.0 / 5.0 + 32.0, 'F')
        else:
            return (temp_c, 'C')
