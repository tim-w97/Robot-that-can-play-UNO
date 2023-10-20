from pyniryo import *

class RobotProxy:
    def __init__(self):
        pass

    def connect(self):
        self.robot = NiryoRobot("10.10.10.10")
        self.robot.calibrate_auto()
        self.robot.update_tool()

        self.joints = robot.get_joints()

    def disconnect(self):
        self.robot.close_connection()

    def move(self, point1:float, point2:float, point3:float, point4:float, point5:float, point6:float):
        self.robot.move_joints(point1, point2, point3, point4, point5, point6)

