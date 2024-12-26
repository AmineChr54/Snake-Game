import random
import drawings


class Food:
    def __init__(self):
        self.posx = random.randint(1, 20)
        self.posy = random.randint(1, 20)

    def generate(self, surface):
        self.posx = random.randint(1, 20)
        self.posy = random.randint(1, 20)
        drawings.draw_food(surface, self.posx, self.posy)

    def update(self, surface):
        drawings.draw_food(surface, self.posx, self.posy)

# ------------------------------------------------------------------------------------------- #
"""
import random
import pygame
import drawings

class Food:
    def __init__(self):
        self.posx = random.randint(1, 20)
        self.posy = random.randint(1, 20)

    def generate(self, surface):
        self.posx = random.randint(1, 20)
        self.posy = random.randint(1, 20)
        drawings.draw_food(surface, self.posx, self.posy)

    def update(self, surface):
        drawings.draw_food(surface, self.posx, self.posy)
"""