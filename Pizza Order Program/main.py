print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L? \n")

if size=="S":
  print("Prize for small pizza is Rs.150")
elif size=="M":
  print("Prize for medium pizza is Rs.200")  
elif size=="L":
  print("Prize for large pizza is Rs.250")  

add_pepperoni = input("Do you want pepperoni? Y or N \n(Rs.20 for S,Rs. 30 for M & L) \n")
extra_cheese = input("Do you want extra cheese? Y or N \n (Rs. 10) \n")

if size=="S":
  bill=150
  if add_pepperoni=="Y":
    bill+=20
  
elif size=="M":
  bill=200
  if add_pepperoni=="Y":
    bill+=30

elif size=="L":
  bill=250
  if add_pepperoni=="Y":
    bill+=30

if extra_cheese=="Y":
  bill+=10
print("Your total bill is Rs.",bill)