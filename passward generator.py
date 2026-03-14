import random
alphabet = ["a", "b", "c", "d", "e", "f", "g","i","j","k"]
symbols=["@","#","$","%","^","&","*"]
numbers=["1","2","3","4","5","6","7","8","9"]
print("welcome to password generator")
print("how many lettors do you want to insert")
n=int(input())
n1=int(input())
n2=int(input())

password = []
for i in range(1,n+1):
    random_lettor = random.choice(alphabet)
    password += random_lettor
print(password)
for i in range(1,n1+1):
    random_symbol=random.choice(symbols)
    password += random_symbol
print(password)
for i in range(1,n2+1):
    random_number=random.choice(numbers)
    password += random_number
print(password)
random.shuffle(password)
print(password)
result="".join(password)
print(result)

letters = ["a", "b", "c"]

s = ""

for i in letters:
    s += i

print(s)