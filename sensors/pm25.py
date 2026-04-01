
import serial

class PMS5003:
    def __init__(self, port, baud):
        self.ser = serial.Serial(port, baudrate=baud, timeout=2)

    def read(self):
        data = self.ser.read(32)

        if len(data) != 32:
            return None

        pm25 = data[12] * 256 + data[13]

        # basic validation
        if pm25 < 0 or pm25 > 1000:
            return None

        return pm25
