# Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in
# the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists (
# mammals, fishes, birds). The class should also have 2 more methods: •	add_animal(species, name) - based on the
# species, adds the name to the corresponding list •	get_info(species) - based on the species returns a string in
# the following format: "{Species} in {zoo_name}: {names} Total animals: {total_animals}" On the first line,
# you will receive the name of the zoo. On the second line, you will receive number n. On the following n lines you
# will receive animal info in the format: "{species} {name}". Add the animal to the zoo to the corresponding list.
# The species could be "mammal", "fish", or "bird". On the final line, you will receive a species. At the end,
# print the info for that species and the total count of animals in the zoo.

class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal_name):
        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)
        Zoo.__animals += 1

    def get_info(self, species):
        output = ""
        if species == "mammal":
            output = f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            output = f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            output = f"Birds in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        return output


name = input()
zoo = Zoo(name)
animal_count = int(input())

for i in range(animal_count):
    command = input().split(" ")
    animal_info = command[0]
    animal_type = command[1]
    if animal_info == "mammal":
        zoo.add_animal(animal_info, animal_type)
    elif animal_info == "fish":
        zoo.add_animal(animal_info, animal_type)
    elif animal_info == "bird":
        zoo.add_animal(animal_info, animal_type)

searched_type = input()
print(zoo.get_info(searched_type))
