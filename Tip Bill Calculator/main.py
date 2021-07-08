print("Welcome to the tip calculator.")
bill=float(input("What is the total bill? ₹"))
tip=float(input("What percentage tip would you like to give? (Write any number)"))
total_bill= bill+ tip/100*bill
people=int(input("How many people to split the bill?"))
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
final_amount="{:.2f}".format(final_amount)
print("Each person should pay ₹",final_amount)
