
#***********************************************************************************************************************
#Import Libraries Here
from time import sleep #imported sleep function from the time library
#***********************************************************************************************************************

#Welcome screen
#Developer: Gavin.Butcher
#version:1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading
"""
print("\033[1;31m welcome fury Infotech Center \n")
sleep(2)
print("\033[1;32m Operation Fury Operation system booting up  \n")

for i in range(2):
    print("OS Booting up.")
    sleep(1)

#weather
#Developer:Gavin Butcher
#version 1.0

"""
Create a function for our current weather using the random. choice function to determine what the weather is
picking from a list - using If, Elif and else statements to check the condition and print a specific print line
"""

#Import Libraries here
import random

#Weather condition list using the random.choice library
#to randomly choose a condition and storing it in its brain
def weather():
    weather_forcast = [" Rain","Snow", "Sunny", "Cloudy", "Foggy", "Storming", "Icy"]
    weather_condition = random.choice(weather_forcast)
    return weather_condition


weatherAlert = weather()
def vehicleResponseSystem():
    if weatherAlert == "Icy":
        print("\nVRS changed your alarm 30 minutes earlier based on the NWS forcast of" ,weatherAlert)
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snow":
        print("\nVRS changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Rain":
        print("\nVRS changed your alarm 5 minutes earlier based on the NWS forcast of" , weatherAlert)
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Cloudy":
        print("\nVRS changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 40MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS changed your alarm 10 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 55MPH")
    elif weatherAlert == "Storming":
        print("\nVRS changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50MPH")
    else:
        print("\nThe weather today is",weatherAlert, "lets go!")
        print("VRS will only allow your car to go 95MPH")


vehicleResponseSystem()




