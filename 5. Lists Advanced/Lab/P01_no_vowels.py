# Using comprehension, write a program that receives a text and removes all its vowels, case-insensitive. Print the
# new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

vowels_list =['a', 'o', 'u', 'e', 'i']
str_input = input()
no_vowels_list = [ch for ch in str_input if ch not in vowels_list]
print("".join(no_vowels_list))