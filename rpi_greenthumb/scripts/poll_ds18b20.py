"""
Simple polling of DS18B20 temperature sensor
"""

import time

import rpi_greenthumb.sensors.ds18b20 as sensor


def main():
    """
    Main function
    """
    print(sensor.read())
    time.sleep(10)


if __name__ == '__main__':
    main()
