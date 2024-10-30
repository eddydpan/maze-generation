from search import Search
from maze import *
import random

class DFS(Search):
    def __init__(self, graph=None, start_node="1"):
        """
        Initializes a DFS object that stores a graph and its starting node.

        Args:
            graph: A dictionary where the keys are ___ representing each of
                the nodes, and the values are a list of all adjacent nodes. 
            start_node: A ___ representing the starting node.
        """
        self.graph = graph
        self.start = start_node
        

    def generate_spanning_tree(self):
        """
        Generates a spanning tree using BFS.

        Args:
            dim: a tuple of integers (n,h) where n is the max number of
                 children a vertex can have, and h is the height of the tree.
        """
        visited = {}
        
        def dfs(visited, graph, node, prev_node):

            if str(node) not in visited.keys():
                visited[str(node)] = prev_node
                for neighbor in random.sample(graph[str(node)], len(graph[str(node)])):
                    dfs(visited, graph, neighbor, node)

        dfs(visited, self.graph, self.start, 0)

        return visited

    def solve(self):
        """
        Finds the shortest path of the tree that represents the maze using BFS.
        
        Args:
            target: A Node representing the target for the BFS search and
                shortest path.
        """