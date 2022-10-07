# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events.
# Each event is separated with '|' (vertical bar): "event1|event2| … eventN" Each event contains an event name or an
# ingredient and a number, separated by a dash ("{event/ingredient}-{number}") •	If the event is "rest": o	You
# gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100). Print: "You
# gained {gained_energy} energy.". o	After that, print your current energy: "Current energy: {current_energy}.".
# •	If the event is "order": o	You've earned some coins (the number in the second part). o	Each time you get an
# order, your energy decreases by 30 points. 	If you have the energy to complete the order, print: "You earned {
# earned} coins.". 	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!". •	In any other
# case, you have an ingredient you should buy. The second part of the event contains the coins you should spend. o	If
# you have enough money, you should buy the ingredient and print: "You bought {ingredient}." o	Otherwise,
# print "Closed! Cannot afford {ingredient}." and your bakery rush is over. If you managed to handle all events
# throughout the day, print on the following 3 lines: "Day completed!" "Coins: {coins}" "Energy: {energy}" Input /
# Constraints You will receive a string representing the working day events, separated with '|' (vertical bar) in the
# format: "event1|event2| … eventN". Each event contains an event name or an ingredient and a number, separated by a
# dash in the format: "{event/ingredient}-{number}" Output Print the corresponding messages described above.

initial_energy = 100
initial_coins = 100
event_list = input().split("|")
condition = False
for i in event_list:
    command_line_list = i.split("-")
    current_command = command_line_list[0]
    if current_command == "rest":
        gained_energy = int(command_line_list[1])
        if initial_energy >= 100:
            initial_energy = 100
            print(f"You gained 0 energy.")
            print(f"Current energy: {initial_energy}.")
        elif initial_energy + gained_energy > 100:
            print(f"You gained {initial_energy + gained_energy - 100} energy.")
            print(f"Current energy: {initial_energy}.")
            initial_energy = 100
        else:
            initial_energy += gained_energy
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {initial_energy}.")
    elif current_command == "order":
        earned_coins = int(command_line_list[1])
        if initial_energy >= 30:
            print(f"You earned {earned_coins} coins.")
            initial_energy -= 30
            initial_coins += earned_coins
        else:
            initial_energy += 50
            print(f"You had to rest!")
    else:
        coins_to_spend = int(command_line_list[1])
        if initial_coins - coins_to_spend >= 0:
            initial_coins -= coins_to_spend
            print(f"You bought {command_line_list[0]}.")
        else:
            print(f"Closed! Cannot afford {command_line_list[0]}.")
            condition = True
            break
if not condition:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
