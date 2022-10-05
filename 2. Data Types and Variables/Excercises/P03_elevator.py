# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

number_of_people = int(input())
elevator_capacity = int(input())


courses_count = 0
if number_of_people < elevator_capacity:
    courses_count = 1
elif number_of_people % elevator_capacity == 0:
    courses_count = number_of_people // elevator_capacity
else:
    courses_count = number_of_people // elevator_capacity + 1

print(courses_count)

