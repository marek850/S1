import random
import sys


class Generator:
    def __init__(self, seed=None):
        self.__seed = seed if seed is not None else random.randint(1, 10000000)
    def generate_unique_id(self):
        self.__seed = random.randint(1, 10000000)
        random.seed(self.__seed)
        return random.randint(0, sys.maxsize)
    def generate_number(self, min, max):
        return random.randint(min, max)