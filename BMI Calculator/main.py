print("Welcome to BMI calculator!")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight/height**2)
a = (f"Your BMI is {BMI}.")
if BMI<=18.5:
  print(a, "You are underweight.")
elif BMI<25:
  print(a, "You are normal weight.")
elif BMI<30:
  print(a, "You are slightly overweight.")
elif BMI<35:
  print(a,"You are obese.")
else:
  print(a,"You are clinically obese.")