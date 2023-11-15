import math

from control import RobotProxy

pickup_pitch = math.radians(25)
rotation_90 = math.radians(90)

x_pos_prepare = 0.16

x_pos_min = 0.24
x_pos_max = 0.4
x_pos_middle = (x_pos_min + x_pos_max) / 2

y_pos_min = -0.17
y_pos_max = 0.17

z_pos = 0.065

# setting up the robot
print("init")

proxy = RobotProxy()
proxy.connect()

# prepare to pick up a card
proxy.move(
    x=x_pos_prepare,
    y=y_pos_min,
    z=z_pos,  # replace with real value
    roll=rotation_90,
    pitch=pickup_pitch,
    yaw=rotation_90
)

# pickup card number 3
proxy.move(
    x=x_pos_max,
    y=y_pos_min,
    z=z_pos,  # replace with real value
    roll=rotation_90,
    pitch=pickup_pitch,
    yaw=rotation_90
)

proxy.grab()

proxy.moveToHomePose()
proxy.release()

# disconnecting the robot
proxy.disconnect()

