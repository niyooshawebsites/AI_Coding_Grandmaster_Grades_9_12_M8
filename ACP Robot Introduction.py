# Creating a Robot class
class Robot:
    
    # Constructor to initialize robot name
    def __init__(self, name):
        self.name = name
    
    # Method to introduce the robot
    def introduce(self):
        print("Hello! My name is", self.name)

# Creating objects (robots)
robot1 = Robot("Tom")
robot2 = Robot("Jerry")

# Calling introduce method
robot1.introduce()
robot2.introduce()