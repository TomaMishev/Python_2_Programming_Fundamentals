# You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more
# electrons left. The rules for electron distribution are as follows: •	The maximum number of electrons in a shell can
# be 2n2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the
# 3rd shield can be 2*32 = 18. •	You should start filling the shells from the first one at the first position. •	If
# the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and
# so on. In the end, print a list with the filled shells.

number = int(input())
counter = 0
shell_list = []
while number > 0:
    counter += 1
    if number - (2 * counter ** 2) >= 0:
        number -= (2 * counter ** 2)
        shell_list.append((2 * counter ** 2))
    else:
        shell_list.append(number)
        number = 0

print(shell_list)
