from bfs import BFS
from maze import *

maze = Maze(4, 4)
bfs_object = BFS(maze.adjacency_matrix())

solution = bfs_object.generate_spanning_tree()
print(solution)