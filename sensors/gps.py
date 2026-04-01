import serial
import pynmea2

class GPS:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, timeout=1)

    def get_position(self):
        try:
            line = self.ser.readline().decode("ascii", errors="ignore")

            if "GGA" in line:
                msg = pynmea2.parse(line)
                return msg.latitude, msg.longitude

        except Exception:
            return None, None

        return None, None
