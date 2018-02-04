import datetime, time
import math
import csv
from sense_hat import SenseHat

se = SenseHat()
timetaken = 0

#I'm not sure if the above needs to be imported on the main file instead of just the current one.
#I've just put it on this file for now

def save_magnet_data():
  with open("magnetic_data.csv","w") as magnetdata:
    writer = csv.writer(magnetdata)
    #1450 steps with 0.1 waits takes 7min 11s
    #set as 10 so testing program is faster
    for x in range(1,10):

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

print("done")