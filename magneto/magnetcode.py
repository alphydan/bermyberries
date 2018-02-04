import datetime, time
import math
import csv
from sense_hat import SenseHat

se = SenseHat()
timetaken = 0

'''
I'm not sure if the above needs to be imported on the main
file instead of just the current one.
I've just put it on this file for now
'''

def save_magnet_data(timestamp):
  '''
  This function saves one line of magnetic data
  and is used each time the main loop runs
  `in`: the input is the timestamp
  `out`: a line is written to file magnetic_data.csv
  '''
  with open("magnetic_data.csv","wb") as magnetdata:
    writer = csv.writer(magnetdata)
    # gets the raw magnetic data
    raw = se.get_compass_raw()

    # gets the components of the magnetic data
    x = raw["x"]
    y = raw["y"]
    z = raw["z"]
    components = "x: {x}, y: {y}, z: {z}".format(**raw)

    total = math.sqrt(x*x + y*y + z*z)
    total = round(total, 3)
  
    row = [str(x),str(y),str(z),str(total), timestamp]

    writer.writerow(row)
    return None # does not output anything

