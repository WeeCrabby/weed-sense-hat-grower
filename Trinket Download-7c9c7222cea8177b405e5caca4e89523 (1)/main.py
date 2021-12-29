from sense_hat import SenseHat
import time
import math

"""

cannabis
flowering temp - 18-29C
hum - 40% - 50%
vegetative temp - 20-25C
hum -40%- 60%
"""

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
plant = 0
state = 0

def settings():
  print("What are you growing?")
  print("1. cannabis")
  print("2. other")
  plant = input()
  global start_temp
  global end_temp
  global start_hum
  global end_hum
  
  if(plant == "1"):
    
    print("Is your cannabis in a vegetative state, or flowering state?")
    print("1. vegetative")
    print("2. flowering")
    state = input()
    print(state)
    if(state == 1):
      start_temp = 20
      end_temp = 25
      start_hum = 40
      end_hum = 60
    else:
      start_temp = 18
      end_temp = 29
      start_hum = 40
      end_hum = 50
  
  else:
    print("type in the lowest temperature for your plant")
    start_temp = int(input())
    print("type in the highest temperature for your plant")
    end_temp = int(input())
    print("type in the lowest humidity for your plant (%)")
    start_hum = int(input())
    print("type in the highest humidity for your plant (%)")
    end_hum = int(input())
    
  
 
def measure_temperature(start_temp, end_temp, start_hum, end_hum):
  temp = math.floor(sense.get_temperature())
  if(temp >start_temp and temp < end_temp):
    sense.show_message(str(temp) + "C", text_colour = green)
  else:
    sense.show_message(str(temp) + "C", text_colour = red)
    
  hum = math.floor(sense.get_humidity())
  if(hum > start_hum and hum < end_hum):
    sense.show_message(str(hum) + "%", text_colour = green)
  else:
    sense.show_message(str(hum) + "%", text_colour = red)
   
settings()
measure_temperature(start_temp, end_temp, start_hum, end_hum)

