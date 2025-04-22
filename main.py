# Katelyn Curtiss
# April 22 2025
# Snake Game! 

import pygame 
import sys 
import random
from pygame.locals import *

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "SNAKE GAME! ^.^ "

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)


CELL_SIZE = 10 
direction = 1 # 1 is up, 2 is right, 3 is down, 4 is left
update_snake = 0 
score = 0 

snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]
snake_pos.append = ([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE])
snake_pos.append = ([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 2])
snake_pos.append = ([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 3]) 

#colors / wallpaper
BG = ("kwallpaper.webp")
BANANAYELLOW = (255, 255, 102)
Black = (0,0,0)
TOMATO = (255, 99, 71)
BODY_INNER = (167, 107, 207)
BODY_OUTER = (204, 204, 255)

# Define apple position

apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE] 

# Font for score
font = pygame.font.SysFont(None, 35)

# Load and play background music
pygame.mixer.music.load("Joe Hisaishi Merry Go Round of Life from Howl’s Moving Castle.mp3")

pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)

def draw_screen():
    screen.fill(BG)

def draw_apple():
    pygame.draw.rect(screen, TOMATO, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score():
    score_text = font.render(f"score: {score}", True, Black)
    screen.blit(score_text, [10,10])

running = True
while running:
    draw_screen()
    draw_apple()
    draw_score()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            elif event.key == pygame.K_RIGHT and direction != 4:  

