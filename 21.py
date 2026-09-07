age = int(input("Enter your age: "))

if age < 5:
    price = 0
elif age < 18:
    price = 50
else:
    price = 100

print("Ticket price =", price)