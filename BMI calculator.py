# simple BMI calculator based on categories defined by the WHO
# and Centres for Disease Control and Prevention

weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

BMI = round(weight / pow(height, 2),2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}. Category = Underweight.")
elif 18.5 <= BMI <= 24.9:
    print(f"Your BMI is {BMI}. Category = Healthy weight.")
elif 25.0 <= BMI <= 29.9:
    print(f"Your BMI is {BMI}. Category = Overweight.")
elif 30.0 <= BMI <= 34.9:
    print(f"Your BMI is {BMI}. Category = Obese (Class 1).")
elif 35.0 <= BMI <= 39.9:
    print(f"Your BMI is {BMI}. Category = Obese (Class 2).")
elif BMI >= 40.0:
    print(f"Your BMI is {BMI}. Severe Obesity (Class 3).")




