# Get user input
name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        height_input = input("Enter your height (in cm): ")
        height = float(height_input)
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        weight = float(input("Enter your weight (in kg): "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate BMI
bmi = weight / (height / 100) ** 2

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Print the results
print(name + " is " + category)
print("BMI: ", bmi)
