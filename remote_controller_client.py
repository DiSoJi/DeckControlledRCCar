import signal
import socket
import threading
from xbox360controller import Xbox360Controller
#print(Xbox360Controller.get_available())

#May the gods of programming forgive me for putting this above function definitions and all in a single file. Convinience...
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "192.168.100.97"  # replace with the server's IP address
server_port = 8000  # replace with the server's port number
# establish connection with server
client.connect((server_ip, server_port))

axis_threshold = 0.3
#x = threading.Thread(target=receiving_frames, args=(1,))

def receiving_frames(name):
    pass

def start_stop_camera():
    pass

def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))
    
    msg = button.name + "p"+":0"
    client.send(msg.encode("utf-8")[:1024])

def on_button_released(button):
    print('Button {0} was released'.format(button.name))
    msg = button.name + "r"+":0"
    client.send(msg.encode("utf-8")[:1024])

def on_trigger_pressed(axis):
    #if axis.value >= axis_threshold:
    print('Axis {0} moved to {1}'.format(axis.name, axis.value))
    msg = axis.name + ":" +str(axis.value)
    client.send(msg.encode("utf-8")[:1024])
    
def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))
    msg = axis.name + ":" +str(axis.x)
    client.send(msg.encode("utf-8")[:1024])

def close_connection(button):
    msg = "close"
    client.send(msg.encode("utf-8")[:1024])
    client.close()
    print("Sever told to close and local connection closed")
    raise KeyboardInterrupt
    
try:
    with Xbox360Controller(0, axis_threshold) as controller:
        
        #print("Loop wo While")
        #Use button B to close socket
        controller.button_b.when_released = close_connection
        
        # Left Bumper detect
        controller.button_trigger_l.when_pressed = on_button_pressed
        controller.button_trigger_l.when_released = on_button_released
        
        # Right bumper detect
        controller.button_trigger_r.when_pressed = on_button_pressed
        controller.button_trigger_r.when_released = on_button_released
        
        # Left and right axis move event
        #controller.axis_l.when_moved = on_axis_moved
        #controller.axis_r.when_moved = on_axis_moved
        
        # Left and right Triggers
        controller.trigger_l.when_moved = on_trigger_pressed
        controller.trigger_r.when_moved = on_trigger_pressed
        
        print("Before Pause")
        #This prevents any subsequent code to be executed but akso prevents the scope from dying. Allowing the thread created by the controller to function
        signal.pause()
        
        #print("After pause")

except KeyboardInterrupt:
    pass

print("Before loop")

#while True:
#    print("While Loop")
    #time.sleep(1)

#client.close()
    