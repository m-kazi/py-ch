fruit = "orange"
banana_color = "green"


if fruit == "banana":
    if banana_color == "green":
        banana_type = "unripe"
    elif banana_color == "yellow":
        banana_type = "ripe"
    elif banana_color == "brown":
        banana_type = "overripe"

else:
    print("No info about this fruit yet!")
    exit()


print(f"Banana is: {banana_type}")
