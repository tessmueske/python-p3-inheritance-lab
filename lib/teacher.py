#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)        
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        random_index = random.randint(0, 8)
        return self.knowledge[random_index]
        

# Expand the teach() method in the Teacher class so that it returns a random element from self.knowledge. We have imported Python's random library to assist you. You will want to use the random.randint() method to choose a random index in self.knowledge. This method takes two arguments, a minimum number and a maximum number, and returns a random element in the range.