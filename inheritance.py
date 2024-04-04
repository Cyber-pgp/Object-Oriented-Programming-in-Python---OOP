# Inheritance

# Imagine you have a super cool toy box at home. This toy box is special because it can make new toy boxes just like it, 
# but each new toy box can have its own extra stickers and decorations.

# In Python, inheritance is like having a special toy box 
# (we call this a "parent class") that can create new toy boxes (these are called "child classes"). 
# The new toy boxes get all the toys from the super cool toy box plus they can add their own new toys or stickers.

# So, if your first toy box has cars and dolls (these are like the attributes or methods in the parent class), 
# your new toy box will have those too. But, if you decide, you can also add robots to your new toy box (these are like new attributes or methods in the child class).

# This way, you don't need to fill the new toy box from scratch; you start with what's already in the first box and then add whatever more you like!

# Let's turn our toy box story into Python code to show how inheritance works. 

# Imagine we have a toy box that has some basic toys, 
# and then we create a new toy box that has everything the first one has, plus some extra cool toys.

# The Parent Toy Box: BasicToyBox
# First, we have our basic toy box that comes with cars and dolls. This is our "parent class."

class BasicToyBox:
  def __init__(self):
    self.toys = ['car', 'doll']

  def show_toys(self):
    print('Toys in the box:', self.toys)


# The Child Toy Box: CoolToyBox

class CoolToyBox:
  def __init__(self):
    super().__init__()



