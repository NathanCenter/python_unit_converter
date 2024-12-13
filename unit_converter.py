import sys
from enum import Enum
# need to do as a command  line then do
# user inputs the amount thy want to convert
#the user choose the convert from and to
# have the user pick the type either length: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
# weight:milligram, gram, kilogram, ounce, pound , temperature:  Celsius, Fahrenheit, Kelvin
# lets do temperature first

# convert c to f

# now how do we get the user to pick what they want to convert and how much they want to convert it too.
# lets use user input
# have it so that the user wants to convert Celsius to Fahrenheit
# CREATE pairs this may not work the way I want it to go
class userPick(Enum):
    Celsius_to_Fahrenheit = 1
    Fahrenheit_to_Celsius = 2
    Fahrenheit_to_Kelvin = 3
    Celsius_to_Kelvin = 4

print("Please chose what temperature would you like to convert to. \n 1.Celsius to Fahrenheit \n 2.Fahrenheit to Celsius \n 3.Fahrenheit to Kelvin \n 4.Celsius to Kelvin")
userConvert = input()
userChoice = int(userConvert)
print("You picked ", str(userPick(userChoice)).replace('userPick.',''))
print("Please input the amount you want to convert")

userAmountTemp = input()
if(int(userConvert) == 1):
    c = int(userAmountTemp)
    amount = c * 1.8
    convertCToF = amount + 32
    print("Converted Celsius",c, "to","Fahrenheit:",round(convertCToF,2))
    sys.exit("stop program")
#convert f to c
if(int(userConvert) == 2):
    print("You want to convert ", userAmountTemp)
    f = int(userAmountTemp)
    math = f - 32
    convertFToC = math / 1.8
    print("Converted Fahrenheit",f, "to","Celsius:",round(convertFToC,2))
    sys.exit("stop program")

if(int(userConvert) == 3):
# convert f to k
    f = int(userAmountTemp)
    subSum = f - 32
    multiblySum = subSum * 5
    dividSum = multiblySum / 9
    finalKelvinTotal = dividSum + 273.15
    print("Converted Fahrenheit",f, "to","Kelvin:",round(finalKelvinTotal,2))
    sys.exit("stop program")

if(int(userConvert) == 4):
# convert c to k
    c = int(userAmountTemp)
    finalCelsiusToKelvin = c + 273.15
    print("Converted Celsius",c, "to","Kelvin:",round(finalCelsiusToKelvin,2))
    sys.exit("stop program")