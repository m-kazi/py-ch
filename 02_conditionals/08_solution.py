password = "kn1hb"
password_length = len(password)


if password_length < 6:
    strength = "weak"
elif password_length <= 10:
    strength = "medium"
else:
    strength = "strong"

print(f"password strenth is: {strength}")
