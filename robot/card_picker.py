import math

from control import RobotProxy

pickup_pitch = math.radians(25)
rotation_90 = math.radians(90)

x_pos_min = 0.19
x_pos_max = 0.35
x_pos_middle = (x_pos_min + x_pos_max) / 2

y_pos_min = -0.17
y_pos_max = 0.17

z_pos = 0.065

# setting up the robot
print("init")

proxy = RobotProxy()
proxy.connect()

# disconnecting the robot
proxy.disconnect()

