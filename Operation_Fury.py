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


vehicleResponseSystem()
