import csv
from datetime import datetime

class Logger:
    def __init__(self, file):
        self.file = file

    def log(self, pm25, lat, lon):
        with open(self.file, "a", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                datetime.utcnow().isoformat(),
                pm25,
                lat,
                lon
            ])
