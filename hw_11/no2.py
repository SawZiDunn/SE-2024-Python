import math
import turtle

def RobotiBattle():
    robotList = list()

    while True:
        turtle.clear()

        for robot in robotList:
            robot.draw()

        print(f"\n==== Robots ====")
        i = 0
        for robot in robotList:
            print(f"{i} : ")
            robot.displayStatus()
            i += 1
        print("=============\n")

        choice = input("Enter which robot to order (0, 1, ...),  'c' to create a new robot, or 'q' to quit: ")
        if choice == "q":
            break

        elif choice == "c":
            print(f"Enter which type of robot to create: ")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList += [newRobot]
        
        else:
            n = int(choice)
            robotList[n].command(robotList)

        # Delete robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100

    def move(self, newX, newY):
        if self.energy > 0:
            self.x, self.y = newX, newY
            self.energy -= 10

    def draw(self):
      
        # draw robot picture
        turtle.penup()
        turtle.goto(self.x, self.y - 10)
        turtle.write(f"x: {self.x}, y: {self.y}")
        turtle.pendown()
        turtle.circle(25)

    def displayStatus(self):
        print(f"x={self.x}, y={self.y}, health={self.health}, energy={self.energy}")

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):
        # formula to find the distance between two points is used!
        if self.energy >= 20 and math.sqrt(pow(r.x - self.x, 2) + pow(r.y - self.y, 2)) <= 30:
            self.energy -= 20
            r.health += 10
        else:
            print("Not withing enough distance!")


    def command(self, robotList):
        x = input("'m' to move the robot or 'h' to heal other robots: ")
        if x == "m":
            super().command(robotList)
        elif x == "h":
            robot_to_heal = int(input("Which robot in the robot list you want to heal?: "))
            for robot_no in range(len(robotList)):
                if robot_no == robot_to_heal:
                    self.heal(robotList[robot_no])


class StrikerBot(Robot):
    def __init__(self, missile=5):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        # formula to find the distance between two points is used!
        if self.energy >= 20 and self.missile > 0 and math.sqrt(pow(r.x - self.x, 2) + pow(r.y - self.y, 2)) <= 30:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50
        else:
            print("Not within enough distance!")
                
    def command(self, robotList):
        x = input("'m' to move the robot or 's' to strike other robots: ")
        if x == "m":
            super().command(robotList)
        elif x == "s":
            robot_to_strike = int(input("Enter the Robot ID you want to strike?: "))
            for robot_no in range(len(robotList)):
                if robot_no == robot_to_strike:
                    self.strike(robotList[robot_no])

    def displayStatus(self):
        super().displayStatus()
        print(f"Health={self.health}, Missile={self.missile}")

RobotiBattle()