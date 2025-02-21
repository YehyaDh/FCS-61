age = int(input("Enter your age: "))

if age < 3:
    price = "free"
elif 3 <= age <= 12:
    price = 5
elif 13 <= age <= 18:
    price = 10
else:
    price = 15

print(f"The ticket price is ${price}.")
