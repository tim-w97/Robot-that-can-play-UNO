from control import RobotProxy

print("init")

proxy = RobotProxy()
proxy.connect()


# move the arm to the position where the robot should pick up the uno card
def move_to_pick_up_pos():
    proxy.move(
        x=-0.002,
        y=0.269,
        z=0.094,
        roll=-1.648,
        pitch=0.155,
        yaw=1.701
    )


# move the arm to the position where robot should release the uno card
def move_to_release_pos():
    proxy.move(
        x=0.251,
        y=-0.041,
        z=0.073,
        roll=1.517,
        pitch=0.544,
        yaw=-0.006
    )


for i in range(3):
    move_to_pick_up_pos()
    proxy.grab()
    move_to_release_pos()
    proxy.release()

proxy.disconnect()

