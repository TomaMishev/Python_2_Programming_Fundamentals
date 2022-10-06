# Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes the best
# snowballs. They have decided to involve you in their fray by writing a program that calculates snowball data and
# outputs the best snowball value. You will receive N – an integer, the number of snowballs being made by Tony and
# Andi. On the following lines, you will receive 3 inputs for each snowball: •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer). •	The quality of the snowball (integer). For
# each snowball, you must calculate its value by the following formula: (snowball_weight / snowball_time) **
# snowball_quality In the end, you must print the highest calculated value of a snowball. Input •	On the first input
# line, you will receive N – the number of snowballs. •	On the next N*3 input lines, you will be receiving data about
# each snowball. Output •	You need to print the highest calculated snowball's value in the format: "{
# snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
import sys

snowballs_count = int(input())

current_highest_value = -sys.maxsize

current_highest_weight = 0
current_highest_time = 0
current_highest_quality = 0

for current_ball in range(snowballs_count):
    snowball_weight = int(input())
    time_to_target = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight // time_to_target) ** snowball_quality

    if snowball_value > current_highest_value:
        current_highest_value = snowball_value
        current_highest_weight = snowball_weight
        current_highest_time = time_to_target
        current_highest_quality = snowball_quality

print(f"{current_highest_weight} : {current_highest_time} = {current_highest_value} ({current_highest_quality})")
