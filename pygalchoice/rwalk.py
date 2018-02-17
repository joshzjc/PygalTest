from random import choice

class Randoms():
    def __init__(self,nums=10):
        self.nums = nums
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1,1])
        mobilevalue = choice([1,2,3,4,5])
        return direction * mobilevalue

    def fill_work(self):
        while len(self.x_values) < self.nums:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)