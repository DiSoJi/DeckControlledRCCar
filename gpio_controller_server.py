import socket
from gpiozero import OutputDevice
from time import sleep
import libcamera
#from picamera2 import Picamera2, Preview
from PIL import Image
from adafruit_servokit import ServoKit



#output_18 = OutputDevice(18)
#output_23 = OutputDevice(23)
#output_24 = OutputDevice(24)
#output_25 = OutputDevice(25)

#Constants
nbPCAServo=16 
ACTIONS = {"button_trigger_lp":switch_light_status,"button_trigger_rp":output_23.on,"button_trigger_rr":output_23.off}
MAX_SERVO_THROTTLE = 0.6

#Objects
pca = ServoKit(channels=16)
pca.frequency = 50
pca.reference_clock_speed = 27000000

#Global vars
_press_intensity = 0
_light_status = 0
_light_status = 0

#actions = {"button_trigger_lp":output_18.on,"button_trigger_lr":output_18.off,"button_trigger_rp":output_23.on,"button_trigger_rr":output_23.off}

print(ACTIONS)

#pycam = Picamera2()
#config = picam.create_preview_configuration(main={"size": (800, 600)},colour_space=libcamera.ColorSpace.Srgb(),queue=False)
#config["transform"] = libcamera.Transform(hflip=1, vflip=1)
#picam.configure(config)
#picam.start()

def init_servos():
    for i in [0,4,8,12]:
        pca.continuous_servo[i].set_pulse_width_range(50 , 3100) #0.6 Maximum forward servo speed, 0.5 maximum backwards speed
        #pca.continuous_servo[i].set_pulse_width_range(0, 65535)
        
def switch_horn_status():
    match _horn_status:
        case 0:
            print("Horn Switched ON")
        case 1:
            print("Horn Switched OFF")
            
def switch_light_status():
    match _light_status:
        case 0:
            print("Lights Switched ON")
        case 1:
            print("Lights Switched OFF")
            
            
def set_throttle(servo_port)::
    pca.continuous_servo[servo_port].throttle = _press_intensity * MAX_SERVO_THROTTLE
    
def move():
    move = map(set_throttle, [0,4,8,12])
    list(map)

def turn_right():
    turn = map(set_throttle,[4,8])
    list(map)
    
def turn_right():
    turn = map(set_throttle,[0,12])
    list(map)
    
def run_server():
    init_servos()
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.100.97"
    port = 8000

    # bind the socket to a specific address and port
    server.bind((server_ip, port))
    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # receive data from the client
    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8") # convert bytes to string
        print(request)
        # if we receive "close" from the client, then we break
        # out of the loop and close the conneciton
        try:
            action, val = request.split(":")
            _press_intensity = float(val)
        
            actions[action]()
        except:
            print("Dirty Message Received")
        #print(f"Received: {request}")

        response = "accepted".encode("utf-8") # convert string to bytes
        # convert and send accept response to the client
        client_socket.send(response)

    # close connection socket with the client
    client_socket.close()
    print("Connection to client closed")
    # close server socket
    server.close()


run_server()
