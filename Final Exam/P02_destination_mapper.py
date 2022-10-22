# Now that you have planned out your tour, you are ready to go! Your next task is to mark all the points on the map
# that you are going to visit. You will be given a string representing some places on the map. You have to filter only
# the valid ones. A valid location is: •	Surrounded by "=" or "/" on both sides (the first and the last symbols
# must match) •	After the first "=" or "/" there should be only letters (the first must be upper-case, other letters
# could be upper or lower-case) •	The letters must be at least 3 Example: In the string
# "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid. After you have
# matched all the valid locations, you have to calculate travel points. They are calculated by summing the lengths of
# all the valid destinations that you have found on the map. In the end, on the first line, print: "Destinations: {
# destinations joined by ', '}". On the second line, print "Travel Points: {travel_points}". Input / Constraints •
# You will receive a string representing the locations on the map •	JavaScript: you will receive a single parameter:
# string Output •	Print the messages described above

import re

location = input()
regex = r"=[A-Z][a-zA-Z]{3,}=|\/[A-Z][a-zA-Z]{3,}\/"
matches = re.findall(regex, location)
end_destinations = []
for match in matches:
    output = ""
    for i in match:
        if i != "=" and i != "/":
            output += i
    end_destinations.append(output)
total_points = 0
for i in end_destinations:
    total_points += len(i)
print(f"Destinations: {', '.join(end_destinations)}")
print(f"Travel Points: {total_points}")



