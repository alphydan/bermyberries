import math
import csv
from sense_hat import SenseHat

se = SenseHat()

'''
Mia: I'm not sure if the above needs to be imported on the main
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

  # note the use "a" for append
  # (so we write a new line each time)
  with open("magneto/magnetic_data.csv","a") as magnetdata:
    writer = csv.writer(magnetdata)
    # gets the raw magnetic data
    raw = se.get_compass_raw()

    # gets the components of the magnetic data
    x = round(raw["x"],5) 
    y = round(raw["y"],5)
    z = round(raw["z"],5)
    # normal fluctuations on the sensor indicate there is no 
    # sense in saving more than 5 significant figures
    components = "x: {x}, y: {y}, z: {z}".format(**raw)

    total = math.sqrt(x*x + y*y + z*z)
    total = round(total, 6)
  
    row = [str(x),str(y),str(z),str(total), timestamp]
    writer.writerow(row)
  return None # does not output anything

