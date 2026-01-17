import random


# Inputs / Normalizations
name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: ").strip())
movie_type = input("Enter your favourite movietype: ").strip().upper()  # (Regular / 3D / IMAX)

# Constants
REGULAR_TICKET_BASE_PRICE = 5 # USD
THREE_D_TICKET_BASE_PRICE = 10 # USD
IMAX_TICKET_BASE_PRICE = 15 # USD

CHILD_DISCOUNT_RATE = 30 
SENIOR_DISCOUNT_RATE = 75
MOVIE_TYPE_LIST = ("REGULAR", "3D", "IMAX")

# Validation-1
if not (1 <= age <= 120):
    exit("Not valid age.")

# Validations-2
if movie_type not in MOVIE_TYPE_LIST:
    exit("Not valid movie type.")

# Business logic
discount_rate = 0
if age <= 15:
    discount_rate = CHILD_DISCOUNT_RATE
elif age >=65:
    discount_rate = SENIOR_DISCOUNT_RATE

if movie_type == "REGULAR":
    movie_ticket_price = REGULAR_TICKET_BASE_PRICE    
elif movie_type == "3D":
    movie_ticket_price = THREE_D_TICKET_BASE_PRICE
elif movie_type == "IMAX":
    movie_ticket_price =  IMAX_TICKET_BASE_PRICE

final_price = movie_ticket_price * (100-discount_rate) / 100

# Output
print(f"Starting price for ticket is {movie_ticket_price}$")
print(f"Applying discount of {discount_rate}%")
print(f"Final price for your ticket is {final_price}$")

def greet():
    print("Hello World")

greet()

import random


num = random.randint(20, 50)
print(num)
