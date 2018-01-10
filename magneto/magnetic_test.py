import time
import math
import csv
from sense_hat import SenseHat

se = SenseHat()

timetaken = 0
while timetaken < 5:
    while True:
        # gets the raw magnetic data
        raw = se.get_compass_raw()
        # gets the components of the magnetic data
        x = raw["x"]
        y = raw["y"]
        z = raw["z"]
        components = "x: {x}, y: {y}, z: {z}".format(**raw)
        total = math.sqrt(x*x + y*y + z*z)
        print(components, '-->', total)
        time.sleep(0.1)


        with open('magnetic_data.csv', 'rb') as f:
          data = list(csv.reader(f))

        import collections
        counter = collections.defaultdict(int)
        for row in data:
            counter[row[0]] += 1


        writer = csv.writer(open("magnetic_data.csv", 'w'))
        for row in data:
            if counter[row[0]] >= 4:
                writer.writerow(row)
        time.sleep(0.1)
        timetaken = timetaken + 1
