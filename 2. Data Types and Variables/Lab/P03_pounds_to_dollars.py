# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.

pounds = int(input())
dollars = pounds * 1.31
print(f"{dollars:.3f}")
