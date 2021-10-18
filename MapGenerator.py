import random
import array
import numpy.matlib as np
import matplotlib.pyplot as plt
import math

"""
" MapGenerator
"
" A file that creates a visual map generated from random values, containing
" geographical features for a fantasy setting.
"
" @Author Neil Cronin neilc5867@gmail.com
"""


"""
class Terrain.

Prototype version is a blank grid with a preset amount (20% of size) of 'filled'
Spaces, containing number which corresponds to a location.

size : length of the map in cells - must be more than 10,less than 100 for now.
Functions - __init__, populate, show, show_graphic.
"""
class Terrain:
    def __init__(self, size : int, name : str):
        try:
            if(size < 10 or size > 100):
                raise ValueError("Size must be greater / equal to 10, less / equal to 100.")
            else:
                self.size=size
        except ValueError as ve:
            print(ve)
        self.name=name
        self.matrix=[]
        self.locations=[]
        rows=self.size
        cols=self.size
        for r in range(0,rows):
            self.matrix.append(['#' for c in range(0, cols)])

    """
    populate

    Generate stuff in the map.
    """
    def populate(self):
        print("populate function called.")
        # initialize the locations dict id => string. .
        locations={1:"Bandit Camp", 2:"Village", 3:"Shrine", 4:"Creature nest"}

        # roll a d6 for each location. Num of locations is 20% of total grid size.
        numLocations= math.floor(self.size * .2)
        print("Adding " + str(numLocations) + " locations.")
        # origin is at top left
        for n in range(0, numLocations):
            xVal=random.randint(0,self.size-1)
            yVal=random.randint(0,self.size-1)
            feature=locations.get(random.randint(1,len(locations)))
            print("Placing " + str(feature) + " at " + str(xVal) + "," + str(yVal) + ".")
            self.matrix[yVal][xVal]="@"
            locationCoord=(xVal, yVal)
            self.locations.append(locationCoord)
        # call functions to make geographical features here later.
        return

    """
    show

    Display the map visually for the user.
    """
    def show(self):
        print("show function called. ")
        for r in self.matrix:
            for c in r:
                print(" " + str(c) + " ", end ='')
            print()
        # print list of locations + grid ref after. Need key at top & size.
        # do key before each loop
        return

    """
    show_graphic

    Display the map using matplotlib grapics.

    Make use of basemap.scatter
    """
    def show_graphic(self):
        print("Show graphic function called.")

if __name__ == "__main__":
    print("Main.")
    bonkonia=Terrain(15,"Bonkonia")
    bonkonia.populate()
    bonkonia.show()
    bonkonia.show_graphic()

    print("End Main.")
