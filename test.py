#import gpiozero
import time, libcamera
from picamera2 import Picamera2, Preview
from PIL import Image
import matplotlib.pyplot as plt
#picam = Picamera2()
import pylab as pl
#config = picam.create_preview_configuration()

#config = picam.create_preview_configuration(main={"size": (800, 600)},colour_space=libcamera.ColorSpace.Srgb(),queue=False)
#config["transform"] = libcamera.Transform(hflip=1, vflip=1)

#config = picam.create_preview_configuration(main={"size": (1600, 1200)})
#config["transform"] = libcamera.Transform(hflip=1, vflip=1)
#picam.configure(config)

#picam.start_preview(Preview.QTGL)

#picam.start()
#time.sleep(10)
#picam.capture_file("test-python.jpg")

#picam.close()
"""
with Picamera2() as picam:
    config = picam.create_preview_configuration(main={"size": (800, 600)},colour_space=libcamera.ColorSpace.Srgb(),queue=False)
    config["transform"] = libcamera.Transform(hflip=1, vflip=1)
    picam.configure(config)
    picam.start()
    count = 0
    
    fig, ax = plt.subplots()
    img = None
    while count < 100:
        image=picam.capture_image("main")
        if img is None:
            img = ax.imshow(image)
            ax.axis('off')
        else:
            img.set_data(image)
        plt.pause(0.5)
        plt.draw()
        
        count+=1
        print(count)

        
    #image.save("/home/disoji/Pictures/image_cam.jpeg")
    
    #im = Image.fromarray(array)
    #im.save("/home/disoji/Pictures/image_array.png")
    
    #print(array.tostring())
#from picamera2.outputs import FileOutput
#output = FileOutput('/home/disoji/Pictures/test.jpg')
"""
"""
from picamera2 import Picamera2
import time

import cv2
picam2 = Picamera2()
capture_config = picam2.create_still_configuration()
picam2.start(show_preview=False)
time.sleep(1)
array = picam2.switch_mode_and_capture_array(capture_config, "main")
cv2.imshow("Frame",array)"""
"""
_var = 0.1

def test_funct_button():
    print("Button")

def test_funct_button_arg(val):
    print("This is val:")
    print(val)
    
def test_funct_axis_variable():
    print("Var val:")
    print(_var)
    
text = "button_lr:0.72"
action,val=text.split(":")
print(action)
print(float(val))

text = "button_lp:0.35"
action2,val2=text.split(":")
print(action2)
print(float(val2))
_var = float(val2)

test_dict={"button_lr":test_funct_button,"button_lp":test_funct_axis_variable}


test_dict[action]()

test_dict[action2]()
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Libraries
import time    #https://docs.python.org/fr/3/library/time.html
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
#from Adafruit_PCA9685 import PCA9685
"""
pwm = PCA9685()
pwm.set_pwm_freq(60)


channel = 0
min_pulse = 150  # Min pulse length out of 4096
max_pulse = 600  # Max pulse length out of 4096

while True:
    pwm.set_pwm(channel, 0, min_pulse)
    sleep(1)
    pwm.set_pwm(channel, 0, max_pulse)
    sleep(1)



"""

#Constants
nbPCAServo=16 


#Objects
pca = ServoKit(channels=16)
pca.frequency = 50
pca.reference_clock_speed = 27000000
# function init 
def init():
    for i in [0,4,8,12]:
        
        pca.continuous_servo[i].set_pulse_width_range(50 , 3100) #0.6 Maximum forward servo speed, 0.5 maximum backwards speed
        #pca.continuous_servo[i].set_pulse_width_range(0, 65535)
# function main 
def main():

    pcaScenario();


# function pcaScenario 
def pcaScenario(): #0.6 Maximum servo speed
    #pca.frequency = 60
    #for i in [0,4,8,12]:
     for i in [0]:   
        #print("Starting Servo Forward: " + str(i))
        #pca.continuous_servo[i].throttle = 1
        #time.sleep(1)
        #print("Starting Servo Backwards: " + str(i))
        #pca.continuous_servo[i].throttle = -1
        #time.sleep(1)
        
        #print("Starting Servo Forward Half: " + str(i))
        print(1)
        pca.continuous_servo[i].throttle = -1
        time.sleep(1)
        #print("Starting Servo Forward Half: " + str(i))
        print(0.9)
        pca.continuous_servo[i].throttle = -0.9
        time.sleep(1)
        #print("Starting Servo Forward Half: " + str(i))
        print(0.8)
        pca.continuous_servo[i].throttle = -0.8
        time.sleep(1)
        print(0.7)
        pca.continuous_servo[i].throttle = -0.7
        time.sleep(1)
        print(0.6)
        pca.continuous_servo[i].throttle = -0.6
        time.sleep(1)
        print(0.5)
        pca.continuous_servo[i].throttle = -0.5
        time.sleep(1)
        print(0.4)
        pca.continuous_servo[i].throttle = -0.4
        time.sleep(1)
        print(0.3)
        pca.continuous_servo[i].throttle = -0.3
        time.sleep(1)
        print(0.2)
        pca.continuous_servo[i].throttle = -0.2
        time.sleep(1)
        print(0.1)
        pca.continuous_servo[i].throttle = -0.1
        time.sleep(1)
        #print("Starting Servo Backwards Half: " + str(i))
        #pca.continuous_servo[i].throttle = -0.6
        #time.sleep(1)
        
        print("Stopping Servo: " + str(i))
        pca.continuous_servo[i].throttle = 0.0
        
        
        print("Servo Throttle: " + str(i))
        print(pca.continuous_servo[i].throttle)
        




if __name__ == '__main__':
    init()
    main()
