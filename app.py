 

# BMI = weight (kg) / height (m)^2

## BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

weight = input("Enter your weight in kilograms: ",)
height = input("Enter your height in meters: ")

def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        
        if height <= 0 or weight <= 0:
            return "Height and weight must be greater than zero."
        bmi = weight / (height ** 2)
        return bmi
    except ValueError:
        return "Please enter valid numbers for weight and height."

print ("Your BMI is: ", calculate_bmi(weight, height))
if calculate_bmi(weight, height) < 18.5:
    print("You are underweight.")
elif 18.5 <= calculate_bmi(weight, height) < 24.9:
    print("You have a normal weight.") 
elif 25 <= calculate_bmi(weight, height) < 29.9:
    print("You are overweight.")
elif calculate_bmi(weight, height) >= 30:
    print("You are obese.")
