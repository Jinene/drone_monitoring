
from pymavlink import mavutil

class Telemetry:
    def __init__(self, connection_string):
        self.master = mavutil.mavlink_connection(connection_string)
        self.master.wait_heartbeat()

    def get_drone_position(self):
        msg = self.master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        return msg.lat / 1e7, msg.lon / 1e7
