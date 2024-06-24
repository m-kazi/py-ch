order_size = "small"
extra_shot = False

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print(f"Order: {coffee}")
