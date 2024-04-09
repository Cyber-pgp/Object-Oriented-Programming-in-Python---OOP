# Task: 

# Develop a Simulation System for a Zoo

# Background:
# You are tasked with developing an object-oriented system to simulate a zoo. The system should manage different types of animals and their interactions within the park. The goal is to create a dynamic environment where animals can eat, sleep, and interact with each other and the park's visitors.

# Specifications:

# 1. Basic Objects:

#   Animal: 
#       The base class for all types of animals. Common attributes may include name, age, and energy level. Basic methods might be to eat, sleep, and make sounds. 

#   Herbivores and Carnivores: 
#       Subclasses that inherit from Animal, with specific characteristics and behaviors.

#   Visitors: 
#       A class to represent the visitors in the park, with attributes like name and age.

# 2. Features:
#       Create specific animal species such as lions, elephants, and giraffes, with unique characteristics and behaviors.
#       Implement interactions between animals, like hunting or playing.
#       Allow visitors to "feed" certain animal species, affecting their energy levels.
#       Simulate a day in the zoo, where animals follow their natural routines and interact with visitors.

# 3. Challenges:
#       Managing the energy levels of animals and ensuring they eat and rest regularly.
#       Modeling predator-prey relationships in a way that is balanced and doesn't lead to any species quickly being "eradicated" from the simulation.
#       Creating an engaging and interactive experience for the visitor through the interface.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Adding
# Random Visitor Interactions: Sometimes visitors might feed one animal, other times three, or even more, and the visitors should have randomly generated names.

# Hunting Mechanism Inside the Zoo: 
#         Animals can hunt others, which involves managing the predator-prey dynamics to ensure that no species becomes extinct.

# Life Cycle of Animals: 
#         If an animal "dies" (is hunted), it's removed from the zoo, but to prevent extinction, a new animal of the same species is introduced.

# Energy Management: 
#        The act of hunting increases an animal's energy level by 5. Meanwhile, playing decreases an animal's energy by 5 to simulate exhaustion.

# Dynamic Animal Names: 
#        Animals should have randomly generated names to add variety.

# Visitor Name Input: 
#       When a visitor comes to the zoo, they should input their name to personalize the interaction.


#  requirements aim to simulate a more realistic and engaging zoo environment where events happen spontaneously, mirroring the unpredictability of real life within the controlled confines of a simulation.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# First we have to import random method
import random

# creating a list for animals and visitors so it can chooses randomly from here

animal_names = [
    "Dog", "Cow", "Horse",
    "Donkey", "Tiger", "Panther",
    "Leopard", "Cheetah", "Elephant",
    "Polar bear", "Turtle", "Crocodile",
    "Rabbit", "Porcupine", "Hen"
]


visitor_names = [
    "Alice", "Bob", "Charlie",
    "David", "Eve", "Frank",
    "Grace", "Hannah", "Ivan",
    "Jack"
]

# create a function
def get_random_name(name_list):
  return random.choice(name_list)

# here We'll adjust our Animal class to account for the new dynamics, including energy changes due to hunting and playing.

class Animal:
    def __init__(self, name):
        self.name = get_random_name(animals_name)
        self.energy = 10 # our starting energy would be 10 because they had a goodnight sleep


# the animals are eating and getting 5 more energy so they can play.
    def eat(self):
        print(f'{self.name} ate and feels strong')
        self.energy += 5


# the animals are sleeping and getting 5 more energy so they can play.
    def sleep(self):
        print(f'{self.name} is sleeping')
        self.energy += 5

# animals are making sounds
    def make_sound(self):
        print(f'{self.name} is making sound')

# animals r getting -5 energy when they play
def play(self):
  self.energy = -= 5
  print(f'{self.name} played and lost some energy')

# animals are hunting aenergy level changes when they r hunting or get hunted
def hunt(self, prey):
  if prey.energy > 0
      self.energy += 5
      prey.energy = 0
      print{f'{self.sname} hunted {prey.name} and gained energy.')
  else:
      print(f'{prey.name} is already out of energy.')
          
    
# now we will create herbivores and carnivores class. 
# Herbivores like plants, and carnivores prefer other kinds of food.

class Herbivore(Animal):
    def eat(self):
        super().eat()
        print(f'{self.name} loves those green leaves!')


class Carnivore(Animal):
    def eat(self):
            super().eat()
            print(f'{self.name} enjoys bloody red meat!')


# Creating special animals in our zoo

class Lion(Carnivore):
    def make_sound(self):
        print(f'{self.name} roars loudly, i am the king og the zoo!')


class Elephant(Herbivore):
    def make_sound(self):
        print(f'{self.name} trumpets with joy, i am the happiest animal in the zoo!')


class Giraffe(Herbivore):
    def make_sound(self):
        print(f'{self.name} hums a gentle tune, Nice to see you up here!')


# Creating visitors, the love to feed the animals

class Visitor:
    def feed_animal(self, animal):
        print(f"The visitor feeds {animal.name}.")
        animal.eat()

# bringing zoo to life, creating animals and visitors

leo = Lion('Leo')
ellie = Elephant('Ellie')
gerry = Giraffe('Gerry')

dean = Visitor()

# Morning in the zoo

leo.make_sound()
ellie.make_sound()
gerry.make_sound()

# visitor feeding the animals
dean.feed_animal(leo)
dean.feed_animal(ellie)
dean.feed_animal(gerry)

# animals going to sleeping

leo.sleep()
ellie.sleep()
gerry.sleep()




              
