import sys
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
print("please chose what temperature would you like to convert to. \n 1.  Celsius to Fahrenheit \n 2.  Fahrenheit to Celsius")
userConvert = input()
print("You picked ", userConvert)
print("Please input the amount you want to convert")

userAmountTemp = input()
if(int(userConvert) == 1):
    print("You want to convert ", userAmountTemp)
    c = int(userAmountTemp)
    amount = c * 1.8
    convertCToF = amount + 32
    print("Converted Celsius to ",c,"Fahrenheit:",round(convertCToF,2))
    sys.exit("stop program")
#convert f to c

f = 60
math = f - 32
convertFToC = math / 1.8
print("Celsius:",round(convertFToC,2))

# convert f to k
subSum = f - 32
multiblySum = subSum * 5
dividSum = multiblySum / 9
finalKelvinTotal = dividSum + 273.15
print("Fahrenheit to Kelvin:",round(finalKelvinTotal,2))

# convert c to k
finalCelsiusToKelvin = c + 273.15
print("Celsius to Kelvin:", round(finalCelsiusToKelvin,2))