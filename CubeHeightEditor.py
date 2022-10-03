#imports
import maya.standalone
import argparse
import maya.cmds

maya.standalone.initialize()

#deals with the arg parse and user input

parser = argparse.ArgumentParser(description = "This script creates stairs of cubes going up to the specified height")
parser.add_argument('cube_height', type=int, help='Cube Height')
args = parser.parse_args()

print("Creating Stairs".format(args.cube_height))

#loop to make cube next to each other with the next one taller to make stairs
for i in range(args.cube_height):
    print("Making stair #{}".format(i))
    maya.cmds.polyCube( sx = 5, sy = 5, sz = 5, h = format(i) )
    cmds.move(5, 0, 0)

print("Made stairs in maya according to your desired stair height")