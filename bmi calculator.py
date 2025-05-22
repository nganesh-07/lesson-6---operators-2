height = float(input("Enter your height in meters:"))
weight = float(input("Enter your weight in kilograms:"))

BMI = weight / (height**2)

print("Your BMI:", BMI)

if BMI <= 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are at a healthy weight level.")
elif BMI <= 29.9:
    print("You are slightly overweight.")
elif BMI <= 34.9:
    print("You are severely overweight.")
elif BMI <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")