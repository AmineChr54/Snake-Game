# Example file showing a circle moving on screen
import pygame
import drawings
import snake
import food

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0
game_speed_delay = 100

# Initiating variables and Objects
STATES = {IN_GAME := "IN_GAME", PAUSED := "PAUSED", DEFEAT := "DEFEAT", STARTING := "STARTING"}
GAME_STATE = STARTING
Labels = [pause_label := drawings.Label(screen, "Game paused.", 7 * 25, 7 * 25, ),
          start_label := drawings.Label(screen, "Press any key to start.", 7 * 25, 7 * 25),
          defeat_label := drawings.Label(screen, "You lost! Press any key to start again.", 7 * 25, 7 * 25),
          ]


def start_game():
    global myFood, mySnake
    myFood = food.Food()
    mySnake = snake.Snake(3, 3, 1, 'RIGHT', 1)


start_game()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    pygame.time.delay(game_speed_delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and GAME_STATE == IN_GAME:
            if event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_q or event.key == pygame.K_z or event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                mySnake.change_direction(event.key)
            elif event.key == pygame.K_p:
                GAME_STATE = PAUSED
        elif event.type == pygame.KEYDOWN and (GAME_STATE == DEFEAT or GAME_STATE == STARTING):
            start_game()
            GAME_STATE = IN_GAME
        elif event.type == pygame.KEYDOWN and GAME_STATE == PAUSED:
            if event.key == pygame.K_p:
                GAME_STATE = IN_GAME

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Write code here ---------------------------------------------------------------
    if GAME_STATE == IN_GAME:
        background_rectangle = pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 500, 500))
        if mySnake.isdead():
            GAME_STATE = DEFEAT
        else:
            mySnake.update(screen)
            mySnake.move()
            myFood.update(screen)
            if mySnake.posx == myFood.posx and mySnake.posy == myFood.posy:
                myFood.generate(screen)
                mySnake.eat_food()
                mySnake.update(screen)
                game_speed_delay -= 1
            i=1
            while i < len(mySnake.snake_list):
                if mySnake.posx == mySnake.snake_list[i][0] and mySnake.posy == mySnake.snake_list[i][1]:
                    GAME_STATE = DEFEAT
                i+=1
    # Other States
    elif GAME_STATE == PAUSED:
        background_rectangle = pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 500, 500))
        mySnake.update(screen)
        myFood.update(screen)
        drawings.draw_pause(screen)
        pause_label.draw()
    elif GAME_STATE == DEFEAT:
        background_rectangle = pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 500, 500))
        mySnake.update(screen)
        myFood.update(screen)
        drawings.draw_defeat(screen)
        defeat_label.draw()
    elif GAME_STATE == STARTING:
        background_rectangle = pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 500, 500))
        mySnake.update(screen)
        myFood.update(screen)
        drawings.draw_start(screen)
        start_label.draw()

    # --------------------------------------------------------------------------------
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
# ---------------------------------------------------------------------------------------------------- #
"""
import pygame
import drawings
import snake
import food
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GAME_SPEED_DELAY = 200

# Game states
STATES = {IN_GAME := "IN_GAME", PAUSED := "PAUSED", DEFEAT := "DEFEAT", STARTING := "STARTING"}

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
game_speed_delay = GAME_SPEED_DELAY

# Global variables
GAME_STATE = STARTING
myFood = None
mySnake = None

# Labels
Labels = [
    drawings.Label(screen, "Game paused.", 7 * 25, 7 * 25),
    drawings.Label(screen, "Press any key to start.", 7 * 25, 7 * 25),
    drawings.Label(screen, "You lost! Press any key to start again.", 7 * 25, 7 * 25)
]


def start_game():
    global myFood, mySnake
    myFood = food.Food()
    mySnake = snake.Snake(3, 3, 1, 'RIGHT', 1)


start_game()

while running:
    pygame.time.delay(game_speed_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if GAME_STATE == IN_GAME:
                if event.key in {pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT}:
                    mySnake.change_direction(event.key)
                elif event.key == pygame.K_p:
                    GAME_STATE = PAUSED
            elif GAME_STATE in {DEFEAT, STARTING}:
                start_game()
                GAME_STATE = IN_GAME
            elif GAME_STATE == PAUSED and event.key == pygame.K_p:
                GAME_STATE = IN_GAME

    screen.fill("purple")
    pygame.draw.rect(screen, "black", pygame.Rect(50, 50, 500, 500))

    if GAME_STATE == IN_GAME:
        if mySnake.isdead():
            GAME_STATE = DEFEAT
        else:
            mySnake.update(screen)
            mySnake.move()
            myFood.update(screen)
            if mySnake.posx == myFood.posx and mySnake.posy == myFood.posy:
                myFood.generate(screen)
                mySnake.eat_food()
                mySnake.update(screen)
                game_speed_delay -= 1
            for i in range(1, len(mySnake.snake_list)):
                if mySnake.posx == mySnake.snake_list[i][0] and mySnake.posy == mySnake.snake_list[i][1]:
                    GAME_STATE = DEFEAT
    elif GAME_STATE == PAUSED:
        mySnake.update(screen)
        myFood.update(screen)
        drawings.draw_pause(screen)
        Labels[0].draw()
    elif GAME_STATE == DEFEAT:
        mySnake.update(screen)
        myFood.update(screen)
        drawings.draw_defeat(screen)
        Labels[2].draw()
    elif GAME_STATE == STARTING:
        mySnake.update(screen)
        myFood.update(screen)
        drawings.draw_start(screen)
        Labels[1].draw()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
"""