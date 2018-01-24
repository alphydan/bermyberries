import datetime, time
import math
import csv
from sense_hat import SenseHat

se = SenseHat()

timetaken = 0

# while timetaken < 10:
with open("magnetic_data.csv","w") as magnetdata:
    writer = csv.writer(magnetdata)
    # 1450 steps with 0.1 waits takes 7min 11s
    for x in range(1,1250):

        # gets the raw magnetic data
        raw = se.get_compass_raw()

        # gets the components of the magnetic data
        x = raw["x"]
        y = raw["y"]
        z = raw["z"]
        components = "x: {x}, y: {y}, z: {z}".format(**raw)

        total = math.sqrt(x*x + y*y + z*z)
        total = round(total, 3)

        #print(components, '-->', total)
        time.sleep(0.002)
        timestamp = datetime.datetime.now()
        row = [str(x),str(y),str(z),str(total), timestamp]

        writer.writerow(row)
       
print("i'm done!! :)")

