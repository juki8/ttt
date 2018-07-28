# 6.00.2x Problem Set 2: Simulating robots

import math
import random
random.seed(0)

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """     
        self.width = width
        self.height = height
        self.tilesClean = []
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = math.floor(Position.getX(pos))
        y = math.floor(Position.getY(pos))     
        if (x, y) not in self.tilesClean:
            self.tilesClean.append((x, y))
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        
        if (math.floor(m), math.floor(n)) in self.tilesClean:
            return True
        else: 
            return False      
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.height * self.width
        
    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.tilesClean)
        
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.uniform(0, self.width), 
                        random.uniform(0, self.height))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return Position.getX(pos) >= 0 and \
                Position.getX(pos) < self.width and \
                Position.getY(pos) < self.height and \
                Position.getY(pos) >= 0 

    def __str__(self):
        return "RectangularRoom with size: " + str(self.width) + \
                " | " + str(self.height) + ". Cleaned tiles: " + \
                str(self.tilesClean)

# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        pos = room.getRandomPosition()
        self.position = pos
        self.angle = random.randint(0, 360)        
        # Clean tile at current position
        self.room.cleanTileAtPosition(pos)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.angle

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.angle = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        oldPos = self.getRobotPosition()
        oldDir = self.getRobotDirection()
        # get new position
        posNew = oldPos.getNewPosition(oldDir, self.speed)
        
        # check if pos2 is in room
        if self.room.isPositionInRoom(posNew):
        # Update position
            self.setRobotPosition(posNew)
        # Mark tile as cleaned
            self.room.cleanTileAtPosition(posNew)
        # if not in room, change to random direction and try again
        else: 
            self.angle = random.randint(0, 360)
            
# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)

# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    # initiate room
    room = RectangularRoom(width, height)
    
    # initiate robots as list of robot objects
    robots = []
    for i in range(num_robots):
        robots.append(robot_type(room, speed))
    
    # Start trial:
    timeCounters = [] 
    for trial in range(num_trials):
        anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        timeCounter = 0
        while (room.getNumCleanedTiles() / room.getNumTiles()) < min_coverage:
            timeCounter += 1
            anim.update(room, robots)
            for robot in robots:
#                room.cleanTileAtPosition(robot.getRobotPosition())
                robot.updatePositionAndClean()
            if (room.getNumCleanedTiles() / room.getNumTiles()) >= min_coverage:
                timeCounters.append(timeCounter)
            else:
                continue
        anim.done()
        room.tilesClean = []
    
    return sum(timeCounters)/len(timeCounters)

##Test case
#
speedT = 2
widthT = 10
heightT = 12
min_coverageT = 0.96
num_trialsT = 1
numRobotsT = 3
#robot_type1 = StandardRobot
robot_type2 = RandomWalkRobot
#
##print('Single Simulation:  ' + str(runSingleSimulation(speedT, widthT, heightT, min_coverageT)))
##print(str(num_trialsT) + ' Simulations with 1 robot:  ' + str(runSingleSimulationTrials(speedT, widthT, heightT, min_coverageT, num_trialsT)))
##print(str(num_trialsT) + ' Simulations with ' + str(numRobotsT) + ' robots:  ' + str(runSimulationStandard(numRobotsT, speedT, widthT, heightT, min_coverageT, num_trialsT)))
print(str(num_trialsT) + ' Simulations with ' + str(numRobotsT) + ' robots of type StandardRobot:  ' + str(runSimulation(numRobotsT, speedT, widthT, heightT, min_coverageT, num_trialsT, StandardRobot)))
print(str(num_trialsT) + ' Simulations with ' + str(numRobotsT) + ' robots of type RandomWalkRobot:  ' + str(runSimulation(numRobotsT, speedT, widthT, heightT, min_coverageT, num_trialsT, RandomWalkRobot)))



# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(1, 1.0, 5, 5, 1, 50, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        oldPos = self.getRobotPosition()
        oldDir = self.getRobotDirection()
        # get new position
        posNew = oldPos.getNewPosition(oldDir, self.speed)
        
        # check if pos2 is in room
        if self.room.isPositionInRoom(posNew):
        # Update position
            self.setRobotPosition(posNew)
        # Mark tile as cleaned
            self.room.cleanTileAtPosition(posNew)
        self.angle = random.randint(0, 360)
        

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
