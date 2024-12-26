import pygame


class Label:
    ''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''
    def __init__(self, screen, text, x, y, fontname="Arial" ,size=20, color="white"):
        self.font = pygame.font.SysFont(f"{fontname}",size)
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text
    def change_text(self, newtext, color="white"):
        self.image = self.font.render(newtext, 1, color)
    def change_font(self, font, size, color="white"):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)
    def draw(self):
        self.screen.blit(self.image, (self.rect))

def give_coordinates(x, y):
    return (x * 25 + 25, y * 25 + 25)


def draw_snake_part(surface, posx, posy):
    pygame.draw.rect(surface, 'green', pygame.Rect(give_coordinates(posx, posy), (25, 25)))


def draw_food(surface, posx, posy):
    pygame.draw.rect(surface, 'red', pygame.Rect(give_coordinates(posx, posy), (25, 25)))

def draw_defeat(surface):
    pygame.draw.rect(surface, 'orange', pygame.Rect(give_coordinates(7,7),(6*25,3*25)))
def draw_pause(surface):
    pygame.draw.rect(surface, 'yellow', pygame.Rect(give_coordinates(7,7),(6*25,3*25)))
def draw_start(surface):
    pygame.draw.rect(surface, 'green', pygame.Rect(give_coordinates(7,7),(6*25,3*25)))

# ------------------------------------------------------------------------------------- #
"""
import pygame

class Label:
    def __init__(self, screen, text, x, y, fontname="Arial", size=20, color="white"):
        self.font = pygame.font.SysFont(fontname, size)
        self.image = self.font.render(text, True, pygame.Color(color))
        self.rect = self.image.get_rect(center=(x, y))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)

def give_coordinates(x, y):
    return (x * 25 + 25, y * 25 + 25)

def draw_snake_part(surface, posx, posy):
    pygame.draw.rect(surface, pygame.Color('green'), pygame.Rect(give_coordinates(posx, posy), (25, 25)))

def draw_food(surface, posx, posy):
    pygame.draw.rect(surface, pygame.Color('red'), pygame.Rect(give_coordinates(posx, posy), (25, 25)))

def draw_defeat(surface):
    pygame.draw.rect(surface, pygame.Color('orange'), pygame.Rect(give_coordinates(7, 7), (6*25, 3*25)))

def draw_pause(surface):
    pygame.draw.rect(surface, pygame.Color('yellow'), pygame.Rect(give_coordinates(7, 7), (6*25, 3*25)))

def draw_start(surface):
    pygame.draw.rect(surface, pygame.Color('green'), pygame.Rect(give_coordinates(7, 7), (6*25, 3*25)))
"""