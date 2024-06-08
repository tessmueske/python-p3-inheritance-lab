#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)     
        self.knowledge = []   

    def learn(self, string):
        self.knowledge.append(string)


# We've given you a barebones Student class. Change the class definition so that it inherits from the User class. Run the test suite and notice that you are passing some tests for the Student class, even without writing any code inside that class. That is because it will inherit the first_name and last_name attributes from the User class you told it to inherit from.

# Individual students should initialize with an attribute, self.knowledge, that points to an empty list.

# Expand the learn() method in the Student class so that in takes in a string and adds that string to the student's self.knowledge list.

