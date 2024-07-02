# file management - method 1

file = open("youtube.txt", "w")

try:
    file.write("kazzcode")
finally:
    file.close()


# file management - method 2

with open("youtube.txt", "w") as file:
    file.write("python")
