import pygame
import drawings


class Snake:
    def __init__(self, posx, posy, velocity, direction, size):
        self.posx = posx
        self.posy = posy
        self.velocity = velocity
        self.direction = direction
        self.size = size
        self.snake_list = [[self.posx, self.posy, self.direction], ]

    def change_direction(self, keypressed):
        if (keypressed == pygame.K_s or keypressed == pygame.K_DOWN) and self.direction != 'UP':
            self.direction = 'DOWN'
        elif (keypressed == pygame.K_d or keypressed == pygame.K_RIGHT) and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        elif (keypressed == pygame.K_z or keypressed == pygame.K_UP) and self.direction != 'DOWN':
            self.direction = 'UP'
        elif (keypressed == pygame.K_q or keypressed == pygame.K_LEFT) and self.direction != 'RIGHT':
            self.direction = 'LEFT'

    def move(self):
        if self.direction == 'UP':
            self.posy -= 1
        elif self.direction == 'DOWN':
            self.posy += 1
        elif self.direction == 'RIGHT':
            self.posx += 1
        else:
            self.posx -= 1

    def update(self, surface):

        if len(self.snake_list) > 1:
            i = len(self.snake_list) - 1
            while i > 0:
                self.snake_list[i] = self.snake_list[i - 1]
                i -= 1
        self.snake_list = [[self.posx, self.posy, self.direction]] + self.snake_list[1:]

        for i in range(len(self.snake_list)):
            if (1 <= self.snake_list[i][0] <= 20) and (1 <= self.snake_list[i][1] <= 20):
                drawings.draw_snake_part(surface, self.snake_list[i][0], self.snake_list[i][1])

    def eat_food(self):
        self.velocity += 0.1
        self.size += 1
        if self.snake_list[-1][2] == 'LEFT':
            self.snake_list.append([self.snake_list[-1][0] + 1, self.snake_list[-1][1], self.snake_list[-1][2]])
        elif self.snake_list[-1][2] == 'RIGHT':
            self.snake_list.append([self.snake_list[-1][0] - 1, self.snake_list[-1][1], self.snake_list[-1][2]])
        elif self.snake_list[-1][2] == 'UP':
            self.snake_list.append([self.snake_list[-1][0], self.snake_list[-1][1] + 1, self.snake_list[-1][2]])
        else:
            self.snake_list.append([self.snake_list[-1][0], self.snake_list[-1][1] - 1, self.snake_list[-1][2]])

    def isdead(self):
        if self.posx > 20 or self.posx < 1 or self.posy > 20 or self.posy < 1:
            return True

# ---------------------------------------------------------------- #
"""
import pygame
import drawings

class Snake:
    def __init__(self, posx, posy, velocity, direction, size):
        self.posx = posx
        self.posy = posy
        self.velocity = velocity
        self.direction = direction
        self.size = size
        self.snake_list = [[self.posx, self.posy, self.direction]]

    def change_direction(self, keypressed):
        direction_map = {
            pygame.K_s: 'DOWN',
            pygame.K_DOWN: 'DOWN',
            pygame.K_d: 'RIGHT',
            pygame.K_RIGHT: 'RIGHT',
            pygame.K_z: 'UP',
            pygame.K_UP: 'UP',
            pygame.K_q: 'LEFT',
            pygame.K_LEFT: 'LEFT'
        }
        new_direction = direction_map.get(keypressed)
        if new_direction and new_direction != self.opposite_direction(self.direction):
            self.direction = new_direction

    def opposite_direction(self, direction):
        opposite_map = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        return opposite_map.get(direction)

    def move(self):
        direction_deltas = {
            'UP': (0, -1),
            'DOWN': (0, 1),
            'RIGHT': (1, 0),
            'LEFT': (-1, 0)
        }
        dx, dy = direction_deltas[self.direction]
        self.posx += dx
        self.posy += dy

    def update(self, surface):
        self.snake_list = [[self.posx, self.posy, self.direction]] + self.snake_list[:-1]
        for x, y, _ in self.snake_list:
            if 1 <= x <= 20 and 1 <= y <= 20:
                drawings.draw_snake_part(surface, x, y)

    def eat_food(self):
        self.velocity += 0.1
        self.size += 1
        tail_x, tail_y, tail_dir = self.snake_list[-1]
        if tail_dir == 'LEFT':
            self.snake_list.append([tail_x + 1, tail_y, tail_dir])
        elif tail_dir == 'RIGHT':
            self.snake_list.append([tail_x - 1, tail_y, tail_dir])
        elif tail_dir == 'UP':
            self.snake_list.append([tail_x, tail_y + 1, tail_dir])
        else:
            self.snake_list.append([tail_x, tail_y - 1, tail_dir])

    def isdead(self):
        return self.posx > 20 or self.posx < 1 or self.posy > 20 or self.posy < 1
"""