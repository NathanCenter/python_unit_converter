import sys
from enum import Enum

print("Please chose what unit of weight measurement would you like to convert to. \n 1.milligram to gram \n 2.gram to milligram \n 3.kilogram to ounce \n 4.ounce to kilogram \n 5.pounds to grams \n 6.grams to pounds ")
userInput = int(input())
print("user input", userInput)
# math of converting milligram to gram
if userInput == 1:
    print("please input the amount of you wish to input")
    userMilligram = int(input())
    milligramToGram = userMilligram * 0.001 
    print("Milligram to gram", milligramToGram)
    sys.exit("stop program")

# math of converting gram to milligram
if userInput == 2:
    print("please input the amount of you wish to input")
    userGram = int(input())
    gramsToMilligram = userGram * 1000
    print("Grams to Milligrams", gramsToMilligram)
    sys.exit("stop program")
# math of kilogram to ounce
if userInput == 3:
    print("please input the amount of you wish to input")
    userKilogram = int(input())
    kilogramToOunces = userKilogram * 35.274
    print("Kilogram to Ounces",kilogramToOunces)
    sys.exit("stop program")
# math of ounce to kilogram
if userInput == 4:
    print("please input the amount of you wish to input")
    userOunces = int(input())
    ouncesToKilogram = userOunces * 0.0283495231
    print("Ounces to Kilogram ",ouncesToKilogram)
    sys.exit("stop program")
# math of pounds to Grams
if userInput == 5:
    print("please input the amount of you wish to input")
    userPounds = int(input())
    poundsToGrams =userPounds * 453.59237
    print("Pounds to Grams ",poundsToGrams)
    sys.exit("stop program")
# math of Grams to pounds
if userInput == 6:
    print("please input the amount of you wish to input")
    userGrams = int(input())
    GramsToPounds = userGrams / 453.59290944
    print("Grams to pounds",round(GramsToPounds,2))
    sys.exit("stop program")
