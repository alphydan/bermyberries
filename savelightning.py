from picamera import PiCamera
from time import sleep
import datetime as dt

x= 4
y= 7

lightning = True

if lightning = True:
  #save pic
  camera = PiCamera()
  #str_time = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
  
  camera.capture('lightning.jpg')
  
  with open("lightning_data.csv","w") as lightningdata:
    writer = csv.writer(lightningdata)
    #save (x, y) of lightning + ts
    components = "x: {x}, y: {y}".format(**raw)

    time.sleep(2)
    timestamp = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    row = [str(x),str(y), timestamp]

    writer.writerow(row)
        
print("i'm done!! :)")