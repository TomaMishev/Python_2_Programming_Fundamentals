# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that
# order. Your task is to re-arrange the elements in a list so that the animal looks normal again: •	On the first
# position is the head; •	On the second position is the body; •	On the last one is the tail.

first_srt = input()
second_str = input()
third_str = input()

meerkat = [first_srt, second_str, third_str]
meerkat[0], meerkat[-1] = meerkat[-1], meerkat[0]

print(meerkat)