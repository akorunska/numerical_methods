import math


def ctg(x):
    return math.cos(x) / math.sin(x)


class Integral:
    def __init__(self, a=0.5, b=1):
        self.a = a
        self.b = b

    @staticmethod
    def f(x):
        return (1 + math.sqrt(ctg(x)))/math.pow(math.sin(x), 2)

    def sum_of_border_values(self):
        return self.f(self.a) + self.f(self.b)