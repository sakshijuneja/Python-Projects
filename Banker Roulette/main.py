# import random
# names_string = input("Give me everybody's names, separated by a comma.\n")
# names = names_string.split(", ")
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay, "will pay the bill.")


# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
number_of_persons= len(names)
# print(names)
random_choice=random.randint(0,number_of_persons-1)
person_who_will_pay=names[random_choice]
print(person_who_will_pay, "will pay the bill.")