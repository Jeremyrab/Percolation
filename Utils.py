import random


class Utils:
    @staticmethod
    def generate_rgb():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return r, g, b
