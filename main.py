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
print(maze.adjacency_matrix())

# create rect representation of maze object
maze_rect = []
padding = 20
line_width = 3
pygame_maze_width = SCREEN_WIDTH - 2 * padding
pygame_maze_height = SCREEN_HEIGHT - 2 * padding
cell_width = pygame_maze_width/maze_width
cell_height = pygame_maze_height/maze_height

def display_maze():
    for row in range(maze_width):
        for col in range(maze_height):
            cell = maze.grid[row][col]
            cur_cell_x = padding + cell_width*col
            cur_cell_y = padding + cell_height*row
            if cell.walls[0]:
                pygame.draw.line(screen, (29, 94, 138), (cur_cell_x, cur_cell_y), (cur_cell_x + cell_width, cur_cell_y), line_width)
            if cell.walls[1]:
                pygame.draw.line(screen, (29, 94, 138), (cur_cell_x + cell_width, cur_cell_y), (cur_cell_x + cell_width, cur_cell_y + cell_height), line_width)
            if cell.walls[2]:
                pygame.draw.line(screen, (29, 94, 138), (cur_cell_x, cur_cell_y + cell_height), (cur_cell_x + cell_width, cur_cell_y + cell_height), line_width)
            if cell.walls[3]:
                pygame.draw.line(screen, (29, 94, 138), (cur_cell_x, cur_cell_y), (cur_cell_x, cur_cell_y + cell_height), line_width)

# main loop for pygame
run = True
while run:
    display_maze()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()