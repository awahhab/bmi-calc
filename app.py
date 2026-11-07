 

# BMI = weight (kg) / height (m)^2

# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
    except (TypeError, ValueError):
        return "Please enter valid numbers for weight and height."

    if height <= 0 or weight <= 0:
        return "Height and weight must be greater than zero."

    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5:
        return "You are underweight."
    if 18.5 <= bmi < 24.9:
        return "You have a normal weight."
    if 25 <= bmi < 29.9:
        return "You are overweight."
    return "You are obese."


def main():
    weight = input("Enter your weight in kilograms: ")
    height = input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    if isinstance(bmi, str):
        print(bmi)
        return

    print(f"Your BMI is: {bmi:.2f}")
    print(bmi_category(bmi))


if __name__ == "__main__":
    main()
