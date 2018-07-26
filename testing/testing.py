def bmi(mybmi):
    if float(mybmi) < 18.5:
        return("underweight.")
    elif 18.5 <= float(mybmi) < 25:
        return("normal.")
    elif 25 <= float(mybmi) < 30:
        return("overweight.")
    elif 30 <= float(mybmi) < 35:
        return("obese.")
    else:
        return("extremely obese.")
print("What is your BMI?")
print("You are considered to be "+bmi(input()))
