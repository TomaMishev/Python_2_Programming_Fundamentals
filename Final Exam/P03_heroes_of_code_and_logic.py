# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose
# for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points
# separated by a single space in the following format: "{hero name} {HP} {MP}" -	HP stands for hit points and MP
# for mana points -	a hero can have a maximum of 100 HP and 200 MP After you have successfully picked your heroes,
# you can start playing the game. You will be receiving different commands, each on a new line, separated by " – ",
# until the "End" command is given. There are several actions that the heroes can perform: "CastSpell – {hero name} –
# {MP needed} – {spell name}" •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this
# message: o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!" •	If the hero is
# unable to cast the spell print: o	"{hero name} does not have enough MP to cast {spell name}!" "TakeDamage – {hero
# name} – {damage} – {attacker}" •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP
# is greater than 0) print: o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print: o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}" •	The hero increases his MP. If it brings the MP of the hero above the maximum
# value (200), MP is increased to 200. (the MP can't go over the maximum value). •	 Print the following message: o	"{
# hero name} recharged for {amount recovered} MP!" "Heal – {hero name} – {amount}" •	The hero increases his HP. If
# a command is given that would bring the HP of the hero above the maximum value (100), HP is increased to 100 (the HP
# can't go over the maximum value). •	 Print the following message: o	"{hero name} healed for {amount recovered}
# HP!" Input •	On the first line of the standard input, you will receive an integer n •	On the following n lines,
# the heroes themselves will follow with their hit points and mana points separated by a space in the following format
# •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
# Output •	Print all members of your party who are still alive, in the following format (their HP/MP need to be
# indented 2 spaces): "{hero name} HP: {current HP} MP: {current MP}" Constraints •	The starting HP/MP of the heroes
# will be valid, 32-bit integers will never be negative or exceed the respective limits. •	The HP/MP amounts in the
# commands will never be negative. •	The hero names in the commands will always be valid members of your party. No
# need to check that explicitly. #


heroes_count = int(input())
party_dict = {}

for i in range(heroes_count):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hero_hp = int(current_hero[1])
    hero_mp = int(current_hero[2])
    party_dict[hero_name] = [hero_hp, hero_mp]

command = input()
while command != "End":

    input_line = command.split(" - ")
    command_type = input_line[0]

    if command_type == "CastSpell":
        hero_name = input_line[1]
        mp_needed = int(input_line[2])
        spell_name = input_line[3]
        if party_dict[hero_name][1] >= mp_needed:
            print(
                f"{hero_name} has successfully cast {spell_name} and now has {party_dict[hero_name][1] - mp_needed} MP!")
            party_dict[hero_name][1] -= mp_needed
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command_type == "TakeDamage":
        hero_name = input_line[1]
        damage = int(input_line[2])
        attacker = input_line[3]
        if party_dict[hero_name][0] - damage > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {party_dict[hero_name][0] - damage} HP left!")
            party_dict[hero_name][0] -= damage
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            party_dict.pop(hero_name)
    elif command_type == "Recharge":
        hero_name = input_line[1]
        recharge_amount = int(input_line[2])
        if party_dict[hero_name][1] + recharge_amount > 200:
            print(f"{hero_name} recharged for {200 - party_dict[hero_name][1]} MP!")
            party_dict[hero_name][1] = 200
        else:
            print(f"{hero_name} recharged for {recharge_amount} MP!")
            party_dict[hero_name][1] += recharge_amount
    elif command_type == "Heal":
        hero_name = input_line[1]
        amount_recovered = int(input_line[2])
        if party_dict[hero_name][0] + amount_recovered > 100:
            print(f"{hero_name} healed for {100 - party_dict[hero_name][0]} HP!")
            party_dict[hero_name][0] = 100
        else:
            print(f"{hero_name} healed for {amount_recovered} HP!")
            party_dict[hero_name][0] += amount_recovered
    command = input()

for key, value in party_dict.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
