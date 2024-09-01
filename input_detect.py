import signal
from xbox360controller import Xbox360Controller
#print(Xbox360Controller.get_available())

def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))


def on_button_released(button):
    print('Button {0} was released'.format(button.name))


def on_axis_moved(axis):
    if axis.name == "trigger_l" or axis.name == "trigger_r":
        print('Axis {0} moved to {1}'.format(axis.name, axis.value))
    else:
        print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

try:
    with Xbox360Controller(0, axis_threshold=0.3) as controller:
        
        # Left Bumper detect
        controller.button_trigger_l.when_pressed = on_button_pressed
        controller.button_trigger_l.when_released = on_button_released
        
        # Right bumper detect
        controller.button_trigger_r.when_pressed = on_button_pressed
        controller.button_trigger_r.when_released = on_button_released
        
        # Left and right axis move event
        controller.axis_l.when_moved = on_axis_moved
        controller.axis_r.when_moved = on_axis_moved
        
        # Left and right Triggers
        controller.trigger_l.when_moved = on_axis_moved
        controller.trigger_r.when_moved = on_axis_moved

        signal.pause()
except KeyboardInterrupt:
    pass
