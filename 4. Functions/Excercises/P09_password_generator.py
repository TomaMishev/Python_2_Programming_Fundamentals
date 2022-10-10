# Write a function that checks if a given password is valid. Password validations are:
# •	It should be 6 - 10 (inclusive) characters long
# •	It should consist only of letters and digits
# •	It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# •	"Password must be between 6 and 10 characters"
# •	"Password must consist only of letters and digits"
# •	"Password must have at least 2 digits"

def password_validator(pass_input):
    valid_password = True
    if 6 <= len(pass_input) <= 10:
        valid_password = True
    else:
        valid_password = False
        print("Password must be between 6 and 10 characters")

    digit_count = 0
    for current_char in pass_input:
        if current_char.isdigit():
            digit_count += 1
            continue
        elif current_char.isalpha():
            continue
        else:
            valid_password = False
            print("Password must consist only of letters and digits")
            break

    if digit_count < 2:
        valid_password = False
        print("Password must have at least 2 digits")

    if valid_password:
        print("Password is valid")


password = input()
password_validator(password)
