import sys
from enum import Enum

print("Please chose what length  would you like to convert to. \n 1.millimeter to centimeter \n 2.centimeter to millimeter \n 3.feet to meters \n 4.meters to feet\n 5.feet to centimeter\n 6.centimeter to feet\n 7.yards to miles\n 8.miles to yards")
userInput = int(input())
print("user input", userInput)
# math for millimeter to centimeter
# m * 0.1
if (userInput == 1):
    print("please input the amount of you wish to input")
    userMillimeter = int(input())
    millimetertoCentimeter = userMillimeter * 0.1
    print("Centimeter:",round(millimetertoCentimeter,2))
    sys.exit("stop program")

#math for centimeter to millimeter
if (userInput == 2):
    print("please input the amount of you wish to input")
    userMillimeter = int(input())
    centimetertoMillimeter= userMillimeter * 10
    print("millimeter",round(centimetertoMillimeter,2))
    sys.exit("stop program")

# math for feet to meters
if(userInput == 3):
    print("please input the amount of you wish to input")
    userFeet = int(input())
    feetToMeters = userFeet * 0.3048
    print("Meters",round(feetToMeters,2))
    sys.exit("stop program")

# math for meters to feet
if(userInput == 4):
    print("please input the amount of you wish to input")
    userMeters = int(input())
    metersToFeet = userMeters * 3.28084
    print("Feet",round(metersToFeet,2))
    sys.exit("stop program")
# math for feet  to centimeter
if(userInput == 5):
    print("please input the amount of you wish to input")
    userFeet = int(input())
    feetToCentimeter = userFeet * 30.48
    print("Centimeter",round(feetToCentimeter,2))
    sys.exit("stop program")
# math for centimeter to feet
if(userInput == 6):
    print("please input the amount of you wish to input")
    userCentimeter = int(input())
    centimeterToFeet = userCentimeter / 30.48
    print("Feet",round(centimeterToFeet,2))
    sys.exit("stop program")

#math for yards to feet
yards = 5
yardsToFeet = yards * 3
print("yards to feet ",yardsToFeet)

#math for feet to yards
feet = 5
feetToYards = feet/3
print("feet to yards ",feetToYards)

#math for yards to miles
yards = 1000
yardsToMiles = yards / 1760
print("yards to miles ",yardsToMiles)

#math for miles to yards
miles = 1000
milesToYards = miles * 1760
print("miles to yards",milesToYards)