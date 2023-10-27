from pyniryo import *

cardPose = [0.2, -0.2, 0.2, 0.003, 0.994, .0]

class RobotProxy:
    def __init__(self):
        pass

    def connect(self):
        self.robot = NiryoRobot("10.10.10.10")
        self.robot.calibrate_auto()
        self.robot.update_tool()

        self.robot.move_to_home_pose()

    def disconnect(self):
        self.robot.close_connection()

    def moveJoints(self, j0, j1, j2, j3, j4, j5):
        self.robot.move_joints(j0, j1, j2, j3, j4, j5)

    def move(self, x, y, z, roll, pitch, yaw):
        self.robot.move_pose(x, y, z, roll, pitch, yaw)

    def moveToHomePose(self):
        self.robot.move_to_home_pose()


# further logic can be placed in here