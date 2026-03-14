import random

names = input("enter everybody name: ")
names_1 = names.split()
print(names_1)
length = len(names_1)
random_person=random.randint(0,length-1)
print(names_1[random_person])