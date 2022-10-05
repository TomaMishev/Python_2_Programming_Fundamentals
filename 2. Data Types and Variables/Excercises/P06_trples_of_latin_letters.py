# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically

num = int(input())
for i in range(0, num):
    for j in range(0, num):
        for k in range(0, num):
            print(f"{chr(97 + i)}{chr(97 + j)}{(chr(97 + k))}")
