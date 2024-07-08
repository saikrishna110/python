# Assignment-1: if condition
# Check if a person is eligible to vote based on their age
# Input: Age of the person
# Check if the person is eligible to vote
'''
age = int(input("enter the age:"))
if age > 18:
    print("Eligible to vote")
'''
# Assignment-2: if else condition
# WAP that checks whether a number is positive or negative
'''
num =int(input("enter the number: "))
if num >= 0:
    print(f"{num} is positive number")
else:
    print(f"{num} is a negative number")
'''
# Assignment-3: if else condition
# WAP that Checks if a given number is even or odd
'''
num1 = int(input("enter the number: "))
if num1 % 2 == 0 :
    print(f"{num1} is a even number")
else:
    print(f"{num1} is a odd number")
'''
# Assignment-4: nested if condition
# WAP to find the greatest of 3 numbers
'''
x = int(input("enter the number1: "))
y = int(input("enter the number2: "))
z = int(input("enter the number3: "))
if x > y:
    if x > z:
        print(f"{x} is greater than {y}, {z}")
    else:
        print(f"{z} is greater than {y}, {x}")
else:
    if y > z :
        print(f" {y} is greater than {x}, {z}")
    else:
        print(f"{z} is greater than {x}, {y}")
'''
# Assignment-5: nested if else condition
"""

Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices based on the age of the customer and the time of the day. The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinee show (before 5 PM) offers a 25% discount to all.
"""
age = int(input("enter the age: "))

regular_price = 10
time = int(input("enter the time in 24 day format: "))
if age <= 12 or age >= 65:
    print(f"price of the ticket is {regular_price-(regular_price*0.5)}$")
else:
    if time >= 14 and time < 17 :
        print(f"price of the ticket is {regular_price-(regular_price*0.25)}$ ")
    else:
        print(f"price of the ticket is {regular_price}$")


# Assignment-6: nested if else condition
# WAP to find the biggest country among 3 based on the population
'''country1 = int(input("enter the population : "))
country2 = int(input("enter the population : "))
country3 = int(input("enter the population : "))
if country1 > country2:
    if country3 < country1:
        print("country1 is greater than other countries")
    else:
        print("country3 is greater than other countries")
else:
    if country2 > country3 :
        print("country2 is greater than other countries")
    else:
        print("country3 is greater than other countries")
'''