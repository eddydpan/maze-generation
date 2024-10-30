from bfs import BFS

bfs_object = BFS()

bfs_object.generate_spanning_tree((4,4))
print(bfs_object.graph)

###############################################################################
# from maze import *
# from main import display_maze
# import pygame

# # Start PyGame
# pygame.init()

# # Set up pygame display
# SCREEN_WIDTH = 720
# SCREEN_HEIGHT = 540

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # create maze object
# maze_width = 20
# maze_height = 20
# maze = Maze(maze_width, maze_height)
# print(maze.adjacency_matrix())

# # create rect representation of maze object
# maze_rect = []
# padding = 20
# line_width = 3
# pygame_maze_width = SCREEN_WIDTH - 2 * padding
# pygame_maze_height = SCREEN_HEIGHT - 2 * padding
# cell_width = pygame_maze_width/maze_width
# cell_height = pygame_maze_height/maze_height

# # main loop for pygame
# run = True
# while run:
#     display_maze()
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     pygame.display.update()

# pygame.quit()