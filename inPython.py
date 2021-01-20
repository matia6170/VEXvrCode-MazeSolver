# ------------------------------------------
# 
# 	Project:      VEXcode VR Maze Solver
#	Author:       Hyunwoo Choi
#	Created:      January 12 2021
#	Description:  Solves a VEXcode VR maze using the right hand rule
# 
# ------------------------------------------

# Library imports
from vexcode import *

#main
def main():
    #putting down the pen to show the path of the robot
    pen.set_pen_color(BLUE)
    pen.move(DOWN)

    drivetrain.set_drive_velocity(50, PERCENT)
    drivetrain.set_turn_velocity(50, PERCENT)

    
    #start with 90 deg turned right since we are using a right hand rule to solve this maze
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    
    #run
    run()

#this method checks all three sides and returns a boolean for each side if it is blocked or not
def checkSides():
    
    rightC, frontC, leftC = True, True, True
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    if front_eye.near_object() and distance.get_distance(MM) < 3000:
        rightC = False
    drivetrain.turn_for(LEFT, 90, DEGREES)
    if front_eye.near_object() and distance.get_distance(MM) < 3000:
        frontC = False
    drivetrain.turn_for(LEFT, 90, DEGREES)
    if front_eye.near_object() and distance.get_distance(MM) < 3000:
        leftC = False
        
    drivetrain.turn_for(RIGHT, 90, DEGREES)

    return rightC, frontC, leftC

#main run function
def run():
    #program loop
    while True:

        #drive
        drivetrain.drive_for(FORWARD, 250, MM)

        #checks if the robot's surroundings are clear by using the method above
        rightClear, frontClear, leftClear = checkSides()

        #uses the 3 boolean values above to determine the which direction to turn
        if frontClear and not rightClear:
            print("")
        elif rightClear:
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        elif (not (rightClear and frontClear)) and leftClear:
            drivetrain.turn_for(LEFT, 90, DEGREES)
        elif not (rightClear and leftClear and frontClear):
            drivetrain.turn_for(RIGHT, 180, DEGREES)

        #if found an exit, stop
        if(down_eye.detect(RED)):
            break

        wait(1,MSEC)

    
    
# VR threads — Do not delete
vr_thread(main())
