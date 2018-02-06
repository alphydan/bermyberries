#  This is the astropi entry for the Bermyberries
We are a team of students from Bermuda investigating lighting on the International Space Station.

## Dependencies

You will need to install the following libraries to run this code:


    sudo pip3 install opencv-python -i https://www.piwheels.hostedpi.com/simple
    sudo pip3 install scikit-image -i https://www.piwheels.hostedpi.com/simple 
    sudo pip3 install numpy
    

![ESA lightning](https://github.com/alphydan/bermyberries/blob/master/cam/city_3_HC.jpg)
Detection of lightning from a camera on the ISS

> We are interested in the Physics of the atmosphere. We have decided
to investigate two fascinating phenomena: Lightning and the
magnetosphere. When lightning strikes, some of the energy travels to
the top of the atmosphere, and some free electrons can be sent into
the magnetosphere and the Van Allen belt (arxiv.0906.0429). We want
to detect lightning and see if the electromagnetic waves it produces
affect our magnetometer. Approximately a flash/km^2/month hits the
earth. When observed with a visible (or near IR) camera the results
are beautiful. Our objective is to do image processing to detect
lightning in almost real time. We want to count lightning strikes and
see if magnetic fields change in a window of a couple of seconds
around it. We estimate that in 3h the camera will be able to see
around 24 million km^2. On average, this corresponds to 100,000
lightning strikes. However, lighting and path of flight may divide
the numbers by 10 or 100. In addition, we saw in previous astropi
pictures that the field of view of the camera is sometimes obstructed,
so the area may be smaller too. Overall, we hope to record the
location and effect of hundreds of lightning strikes.

