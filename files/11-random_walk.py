import random

x = 0
y = 0

steps = 25
direction = ["N", "S", "E", "W"]

for step in range(steps):
    block = random.choice(direction)
    if block == "N":
        y += 1
        print(block)
    elif block == "S":
        y -= 1
        print(block)
    elif block == "E":
        x += 1
        print(block)
    elif block == "W":
        x -= 1
        print(block)
    else:
        print("That is not a valid direction")

if x >= 0:
    final_x = "East"
else:
    final_x = "West"
if y >= 0:
    final_y = "North"
else:
    final_y = "South"

print(f"Final Coordinates: {(x,y)}")
print(f"The drunk can be found {abs(x)} block(s){final_x} and {abs(y)} block(s){final_y}")
