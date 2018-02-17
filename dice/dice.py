from random_walk import randint

class DD():
    def __init__(self,numbers=6):
        self.numbers = numbers

    def roll(self):
        return randint(1,self.numbers)