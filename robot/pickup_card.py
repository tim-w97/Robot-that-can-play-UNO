import math

from control import RobotProxy

print("init")

proxy = RobotProxy()
proxy.connect()

proxy.move(z=0.1)

proxy.grab()

proxy.move(x=0, y=0.4)

proxy.release()

proxy.disconnect()

