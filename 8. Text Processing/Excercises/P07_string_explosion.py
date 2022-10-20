# Write a program that reads a string from the console that contains: •	Explosions marked with '>' •	Immediately
# after the mark, there will be an integer x, which signifies the strength of the explosion •	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion mark
# ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete the
# explosion character – '>'. When all characters are processed, print the final string. Constraints •	You will
# always receive strength for the explosions •	The path will consist only of letters from the Latin alphabet,
# integers, and the char '>' •	The strength of the punches will be in the interval [0…9]

text = input()
result = ""
i = 0
count = 0

while i < len(text):
    if text[i] != ">":
        result += text[i]
        i += 1
    else:
        result += ">"
        i += 1
        count += int(text[i])
        while count > 0 and text[i] != ">":
            i += 1
            count -= 1
            if i >= len(text):
                break

print(result)


