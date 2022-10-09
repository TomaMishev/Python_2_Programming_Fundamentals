# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"

def check_grade(grade_to_check):
    grade_in_string = ""
    if grade_to_check <= 2.99:
        grade_in_string = "Fail"
    elif grade_to_check <= 3.49:
        grade_in_string = "Poor"
    elif grade_to_check <= 4.49:
        grade_in_string = "Good"
    elif grade_to_check <= 5.49:
        grade_in_string = "Very Good"
    elif grade_to_check <= 6:
        grade_in_string = "Excellent"

    return grade_in_string


grade = float(input())
print(check_grade(grade))
