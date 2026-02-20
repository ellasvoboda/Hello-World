# Ella Svoboda
# 2/4/26
# homework 1


# 1 sales tax calculator

sales_tax = 0.075

item_price = float(input("enter the price of the item: "))
quantity = int(input("enter the quantity: "))

subtotal = item_price * quantity
tax = subtotal * sales_tax
total = subtotal + tax

subtotal = round(subtotal,2)
tax = round(tax,2)
total = round(total,2)

print("subtotal: ", subtotal)
print("tax: ", tax)
print("total: ", total)


# 2 BMI calculator

pounds_to_kg = 2.20
feet_to_meters = 3.28

weight_pounds = float(input("enter your weight in pounds: "))
height_feet = float(input("enter your height in feet: "))

weight_kg = weight_pounds / pounds_to_kg
height_meters = height_feet / feet_to_meters
bmi = weight_kg / (height_meters ** 2)

weight_kg = round(weight_kg, 2)
height_meters = round(height_meters, 2)
bmi = round(bmi, 2)

print("weight in kg: ", weight_kg)
print("height in meters: ", height_meters)
print("BMI: ", bmi)


# 3 monthly mortgage payment calculator

principal = float(input("enter the proncipal loan amount: "))
annual_rate = float(input("enter the annual interest rate as a percent: "))
years = int(input("enter the number of years for the loan: "))

monthly_rate = annual_rate / (12 * 100)
number_of_payments = 12 * years

monthly_payment = ((principal * annual_rate) / (12*100)) * (1 / (1-(1+(annual_rate/(12*100)))**(-12*years)))


monthly_payment = round(monthly_payment, 2)

print("monthly mortgage payment: $",monthly_payment)


# 4 student grade categorizer

numeric_grade = float(input("Enter your numeric grade between 0 and 100: "))

if numeric_grade >= 90:
    letter_grade = "A"
    
elif numeric_grade >= 80:
    letter_grade = "B"
    
elif numeric_grade >= 70:
    letter_grade = "C"
    
elif numeric_grade >= 60:
    letter_grade = "D"
    
else:
    letter_grade = "F"
    
print("numeric grade: ", numeric_grade)
print("letter grade: ", letter_grade)


# 5 bonus eligibility checker

required_hours = 35
required_score = 85
bonus = 100

hours_worked = float(input("enter hours worked: "))
performance_score = float(input("enter performance score: "))

if hours_worked > required_hours and performance_score > required_score:
    print("congratulations you get a bonus!")
    print("bonus amount: $", bonus)
    
else:
    print("you do not get a bonus.")
    
    if hours_worked <= required_hours:
        hours_needed = required_hours - hours_worked + 1
        print("additional hours needed: ", hours_needed)
        
    if performance_score <= required_score:
        score_needed = required_score - performance_score + 1
        print("additional performance points needed: ", score_needed)
        

