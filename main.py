from maze import *
import pygame

# Start PyGame
pygame.init()

# Set up pygame display
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 540

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create maze object
maze_width = 20
maze_height = 20
maze = Maze(maze_width, maze_height)

# create rect representation of maze object
maze_rect = []
padding = 20
pygame_maze_width = SCREEN_WIDTH - 2 * padding
pygame_maze_height = SCREEN_HEIGHT - 2 * padding
cell_width = pygame_maze_width/maze_width
cell_height = pygame_maze_height/maze_height
for x in range(maze_width):
    for y in range(maze_height):
        maze_rect.append(pygame.Rect(padding + (cell_width * x), padding + (cell_height * y), cell_width, cell_height))

# main loop for pygame
run = True
while run:
    for i in maze_rect:
        pygame.draw.rect(screen, (29, 94, 138), i, 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()