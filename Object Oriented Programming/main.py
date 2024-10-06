
# Class - Plan/Blueprint with Functions/Properties
# Object - an Instance created using a Class

# Creating a Class

class Student():
    # A Class has a lot of Properties + Functions
    # Using Constructor Function to set the Properties
    def __init__(self):
        print("This function will initialize basic features of our object!")
        self.name = ""
        self.age = 11
        self.grade = 6
        self.schoolname = "Pine Middle School"
    def displayDetails(self):
        print(f"My name is {self.name}!")
        print(f"I am {self.age} years old!")
        print(f"I am in {self.grade}th grade!")
        print(f"I go to {self.schoolname}!")

# Creating an Object using the Student Class

s1 = Student()
s2 = Student()

# Accessing the Properties of Object s1

print(s1.age)
s1.name = "Bob"
print(s1.name)
s2.name = "Sarah"
print(s2.name)

# Calling a Function created in a Class

s1.displayDetails()
s2.displayDetails()