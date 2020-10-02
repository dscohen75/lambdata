import pandas as pd
import random

names = ["Roger", "Stuart", "Buddy", "Johnson", "Tommy"]
colors = ["Red", "Green", "Yellow", "Gray", "Blue"]
species_names = ["Wooly Mammoth", "Birds", "Reptiles", "Fish", "Rodents"]

class ExoticAnimals:
    def __init__(self, name, height=1, weight=1, color='brown',
                 legs=4, species=None, mammal=True):
        self.name = str(name)
        self.height = int(height)
        self.weight = int(weight)
        self.color = color
        self.legs = legs
        self.species = species
        self.mammal = mammal

    def move(self, distance, direction):
        return f"{self.name} travels {distance} meters in {direction} direction!"

    def eat(self, food):
        return f"Yum, yum! I love {food}!"

class Anaconda(ExoticAnimals):
    def __init__(self, name, height, weight, color, constrictor, legs=0, species="snake", mammal=False):
        super().__init__(name, height, weight, color, legs, species, mammal)
        self.constrictor = bool(constrictor)

    def move(self, distance, direction):
        return f"{self.name} slithers {distance} meters in {direction} direction!"


def create_animal():
    print("Welcome to the program! Please provide the following info:")
    n = input("What is your animal's name? ")
    h = input("What is your animal's height? ")
    w = input("What is your animal's weight? ")
    c = input("What is your animal's color? ")
    l = input("What is your animal's number of legs? ")
    s = input("What is your animal's species? ")
    m = input("Is your animal a mammal? True or False ")
    dist = input("How far will your animal travel? ")
    dirc = input("Which direction will your animal go? ")
    user_animal = ExoticAnimals(name=n, height=h, weight=w, color=c, legs=l, species=s, mammal=m)
    print(user_animal.move(dist, dirc))

def lots_of_animals(n):
    animals = []
    while n > 0:
        a_name = random.choice(names)
        a_height = random.randint(5, 501)
        a_weight = random.randint(2, 2001)
        a_color = random.choice(colors)
        a_legs = random.randint(0, 5)
        a_species = random.choice(species_names)
        if a_species == "Rodents" or a_species == "Wooly Mammoth":
            a_mammal = True
        else:
            a_mammal = False

        a_animal = ExoticAnimals(a_name, a_height, a_weight, a_color, a_legs, a_species, a_mammal)
        animals.append(a_animal)

        n = n-1
        
    return animals
