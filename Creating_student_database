# Let's dive into creating our student database, just like setting up a school in our Python playroom. Our school needs a list of students, so we need to make a special blueprint (class) for what a student looks like and what they can do.

# Step 1: The Student Blueprint
# Think of a class as a way to describe what a student is. 
# Our students will have a name, an age, and what grade they're in, just like kids in a real school.

class Student:
    def __init__(self, name, age, grade): # defining what student is. student will have name, age, and grade.
        self.name = name # the students name
        self.age = age # the students age
        self.grade = grade # the students grade
    
    def get_info(self): # getting information
        print(f'My name is {self.name}. I am {self.age} years old and in grade {self.grade}')

    
    def promote(self): # this method is like moving up to the next grade at the end of the school year.
        self.grade += 1
        print(f'{self.name} has been promoted to grade {self.grade}.')

# creating a student
anna = Student('Anna', 15, 9)

anna.get_info() # anna introduce her self for first time
anna.promote() # anna got promoted to the grade 10
anna.get_info() # anna introduce her self second time but with higher grade
