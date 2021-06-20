from datetime import *
import pytz
print(">>Welcome to Python program to get Current Time")

print(">>Please select your desired country")

list=["Europe/Berlin","Asia/Kolkata","America/Los_Angeles", "America/New_York","Europe/London","Hongkong","Europe/Minsk","Australia/Sydney"]
serial = 1
for item in list:
  print(serial , " : " , item)
  serial = serial + 1
selection = int(input("Please enter country ID : "))
tz_Germany = pytz.timezone(list[selection-1])
datetime_Germany = datetime.now(tz_Germany)
print(list[selection-1] , " time:", datetime_Germany.strftime("%H:%M:%S"))