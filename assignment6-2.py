class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def special_ability(self):
        print(f"{self.name} has a hunting skill level of {self.hunting_skill}.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def bul_strength(self):
        print(f"{self.name} has a strength level of {self.strength}.")

dog1 = Dog("Puppy",2,"white")
dog2 = JackRussellTerrier("Blacky", 5, "White and black","9/10")
dog3 = Bulldog("Bully", 3, "Brindle","10/10")
print("\nDog",dog1.name)
dog1.description()
dog1.get_info()
print("\nDog",dog2.name)
dog2.description()
dog2.get_info()
print("\nDog",dog3.name)
dog3.description()
dog3.get_info()
print("\nDog's Strength & Skill\n")
dog2.special_ability()
dog3.bul_strength()

# output:

# Dog Puppy
# Puppy is 2 years old.
# Puppy's coat color is white.

# Dog Blacky
# Blacky is 5 years old.
# Blacky's coat color is White and black.

# Dog Bully
# Bully is 3 years old.
# Bully's coat color is Brindle.

# Dog's Strength & Skill

# Blacky has a hunting skill level of 9/10.
# Bully has a strength level of 10/10.