#from gpiozero import LED
from gpiozero import OutputDevice
from time import sleep


"""
led = LED(18)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    break
"""

output_18 = OutputDevice(18)
output_23 = OutputDevice(23)
output_24 = OutputDevice(24)
output_25 = OutputDevice(25)

while True:
    output_18.on()
    sleep(1)
    output_18.off()
    
    output_23.on()
    sleep(1)
    output_23.off()
 
    output_24.on()
    sleep(1)
    output_24.off()
    
    output_25.on()
    sleep(1)
    output_25.off()
    break
    