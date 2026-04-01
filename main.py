import time
from config import *
from sensors.pm25 import PMS5003
from sensors.gps import GPS
from logging.logger import Logger

def main():
    sensor = PMS5003(SERIAL_PORT, BAUD_RATE)
    gps = GPS(GPS_PORT)
    logger = Logger(LOG_FILE)

    while True:
        pm25 = sensor.read()
        lat, lon = gps.get_position()

        if pm25 is not None and lat is not None:
            print(f"PM2.5: {pm25} | Lat: {lat} | Lon: {lon}")

            logger.log(pm25, lat, lon)

        time.sleep(SENSOR_READ_INTERVAL)


if __name__ == "__main__":
    main()
