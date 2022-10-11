#Gasoline
#programmer: Gavin Butcher
#version1.0

"""
Define a Function to check our gas gauge and determine how far
we have untill we need gasoline based on an if, elif, else
condition
"""

#import library here
import random
from time import sleep
#Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","low tank","Quarter Tank" ,"Half Tank" , "Three Quarter Tank" ,"Full tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#variable calling the gasLevelGauge function to store value once
gasLevelIndicator = gasLevelGauge()

def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("***Warning you are on EMPTY***")
        sleep(.9)
        print("Calling Emergency Contact")
gasLevelAlert()