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
#Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","low tank","Quarter Tank" ,"Half Tank" , "Three Quarter Tank" ,"Full tank"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)

gasLevelGauge()