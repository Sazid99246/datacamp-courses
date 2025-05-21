class Calculator:
    def __init__(self, num_one, num_two):
        self.num_one = num_one
        self.num_two = num_two

    def addition(self):
        return self.num_one + self.num_two

    def subtraction(self):
        return self.num_one - self.num_two

    def multiplication(self):
        return self.num_one * self.num_two
