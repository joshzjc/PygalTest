from random_walk import randint

class Matp_die():
    def __init__(self,num_size=6):
        self.num_size = num_size

    def matroll(self):
        return randint(1,self.num_size)