age = 17
day = "Friday"

# if age is greater than or equal to 18 then the price is 8 otherwise 12
price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print(f"Ticket price for you is: ${price}")
