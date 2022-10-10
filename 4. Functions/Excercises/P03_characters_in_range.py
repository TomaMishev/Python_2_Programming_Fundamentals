# Write a function that receives two characters and returns a single string with all the characters in between them (
# according to the ASCII code), separated by a single space. Print the result on the console.

def chars_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end=" ")


chars_in_range(ch1=input(), ch2=input())
