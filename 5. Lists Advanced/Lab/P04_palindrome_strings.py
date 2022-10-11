# On the first line, you will receive words separated by a single space. On the second line, you will receive a
# palindrome. First, you should print a list containing all the found palindromes in the sequence. Then, you should
# print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".

words_list = input().split(" ")
palindrome_word = input()
palindrome_list = [word for word in words_list if word == word[::-1]]
print(palindrome_list)
palindrome_count = words_list.count(palindrome_word)
print(f"Found palindrome {palindrome_count} times")