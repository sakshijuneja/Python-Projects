year = int(input("Which year do you want to check? "))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("YES, it is a leap year.")
    else:
      print("NO, it is not a leap year.")

  else:
     print("YES, it is a leap year.")

else:
  print("NO, it is not a leap year.")