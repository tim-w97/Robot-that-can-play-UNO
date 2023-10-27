from pyniryo import *

cardPose = PoseObject(
    x=0.2, y=-0.2, z=0.2,
    roll=0.003, pitch=0.994, yaw=0.0
)

'''
How to use the Proxy:
1. create instance
2. connect()
3. use move() to control the movement
4. disconnect()
'''
class RobotProxy:
    def __init__(self):
        self.connected = False

    def connect(self):
        try:
            self.robot = NiryoRobot("10.10.10.10")
            self.robot.calibrate_auto()
            self.robot.update_tool()

            self.robot.move_to_home_pose()
            self.pose = self.robot.get_pose()

            self.connected = True
            print("The robot is ready to use.")
        except:
            self.robot = None
            print("There is an error with the connection. Make sure to be connected to the Niryo Wifi.")

    def checkConnection(self):
        if not self.connected: raise Exception("There is no robot connected")

    def disconnect(self):
        self.checkConnection()

        self.robot.move_to_home_pose()
        self.robot.close_connection()
        
    # simple movement
    '''
    Do not use this function for simple movement. Instead use move. This function only exists for turning cards.
    '''
    def moveJoints(self, j0, j1, j2, j3, j4, j5):
        self.checkConnection()
        self.robot.move_joints(j0, j1, j2, j3, j4, j5)
        self.pose = self.robot.get_pose()

    '''
    This method calculates
    '''
    def updatePose(self, x, y, z, roll, pitch, yaw):
        if not x: x = self.pose.x
        if not y: y = self.pose.y
        if not z: z = self.pose.z
        if not roll: roll = self.pose.roll
        if not pitch: pitch = self.pose.pitch
        if not yaw: yaw = self.pose.yaw
        return PoseObject(x=x, y=y, z=z, roll=roll, pitch=pitch, yaw=yaw)

    '''
    This is the convenient method to control the robot.
    move(self, x=self.pose.x) is not working. If you find a similiar version to get a default value from the self-pose, let me know.
    '''
    def move(self, x=False, y=False, z=False, roll=False, pitch=False, yaw=False):
        self.checkConnection()

        new_pose = self.updatePose(x, y, z, roll, pitch, yaw)
        self.robot.move_pose(new_pose)
        self.pose = new_pose

    def moveToHomePose(self):
        self.checkConnection()
        self.robot.move_to_home_pose()
        self.pose = self.robot.get_pose()

    # Grabber
    def grab(self):
        self.checkConnection()
        self.robot.close_gripper()

    def release(self):
        self.checkConnection()
        self.robot.open_gripper()

    # functions for fun
    def killAllHuman(self):
        for i in range(10):
            self.moveJoints(2.99, .0, .0, .0, .0, .0)
            self.grab()
            self.moveJoints(-2.99, .0, .0, .0, .0, .0)
            self.release()

            
