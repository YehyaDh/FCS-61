# Exercise 1
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

# Exercise 2
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Exercise 3
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")