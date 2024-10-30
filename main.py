from maze import *
import pygame
import dfs
import bfs
import time

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
search = bfs.BFS(maze.adjacency_matrix())
solution = search.generate_spanning_tree()

# create rect representation of maze object
maze_rect = []
padding = 20
line_width = 3
pygame_maze_width = SCREEN_WIDTH - 2 * padding
pygame_maze_height = SCREEN_HEIGHT - 2 * padding
cell_width = pygame_maze_width/maze_width
cell_height = pygame_maze_height/maze_height

def display_maze(recent_coord=None):
    """
    Firstly, fill screen with black
    Then, loop through each cell, draw the walls if they exist.
    """
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (30, 123, 186), pygame.Rect(padding + cell_width * (recent_coord[0]-1), padding + cell_height * (recent_coord[1] - 1),cell_width, cell_height))
    for row in range(maze_width):
        for col in range(maze_height):
            cell = maze.get_cell(col+1, row+1)
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

for i in solution.keys():
    xy = maze.draw_graph({i: int(solution[i])})
    display_maze(xy)
    pygame.display.update()
    time.sleep(0.1)

# main loop for pygame
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()