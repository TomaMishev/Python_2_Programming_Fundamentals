# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half. Then the
# cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom and
# the original top card is still on top. For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five',
# 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six'] Write a program that receives a single string (
# cards separated by space) and on the second line receives a count of faro shuffles that should be made. Print the
# state of the deck after the shuffle. Note: The length of the deck of cards will always be an even number.

initial_list = input().split(" ")
count = int(input())

length = len(initial_list)
half_length = length // 2
original_half_length = half_length

new_list = []
new_list2 = []

for i in range(count):
    if i == 0:
        copy_ini_list = initial_list.copy()
    if i > 0:
        if i > 1:
            new_list2.clear()
        for k in range(len(new_list)):
            new_list2.append(new_list[k])
        new_list.clear()
        initial_list = new_list2
        copy_ini_list.clear()
        for b in range(len(new_list2)):
            copy_ini_list.append(new_list2[b])

    half_length = original_half_length
    new_list.append(initial_list[0])
    for j in range(len(initial_list)):
        if j == 0:
            continue
        initial_list[j] = initial_list[half_length]
        new_list.append(initial_list[j])
        if j == original_half_length:
            break
        new_list.append(copy_ini_list[j])
        half_length += 1
print(new_list)