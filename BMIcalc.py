print("Welcome to the BMI calculator!! \n")

# Asking user for input

height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))

print("Your BMI is: ")

# Calculating the BMI and printing it
print(int(weight / (height ** 2)))