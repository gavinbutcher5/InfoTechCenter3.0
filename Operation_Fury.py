#Welcome screen
#Developer: Gavin.Butcher
#version:1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading
"""

#Import Libraries Here
from time import sleep #imported sleep function from the time library

print("\033[1;31m welcome fury Infotech Center \n")

sleep(2)
print("\033[1;32m Operation Fury Operation system booting up  \n")

for i in range(2):
    print("OS Booting up.")
    sleep(1)