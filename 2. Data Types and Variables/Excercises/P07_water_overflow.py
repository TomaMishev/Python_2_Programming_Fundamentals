# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow. On the following n lines,
# you will receive liters of water (integers), which you should pour into your tank. If the capacity is not enough,
# print "Insufficient capacity!" and continue reading the next line. On the last line, print the liters in the tank.

iterations_count = int(input())
capacity = 255
total_filled = 0
for current_iteration in range(iterations_count):
    current_liters = int(input())
    if current_liters <= capacity:
        capacity -= current_liters
        total_filled += current_liters
    else:
        print("Insufficient capacity!")
print(total_filled)
