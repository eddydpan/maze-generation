"""
Python module that implements a Breadth-first Search class.
"""
from search import Search
from collections import deque

class BFS(Search):
    def __init__(self, graph=None, start_node=None):
        """
        Initializes a BFS object that stores a graph and its starting node.

        Args:
            graph: A dictionary where the keys are ___ representing each of
                the nodes, and the values are a list of all adjacent nodes. 
            start_node: A ___ representing the starting node.
        """
        self.graph = graph
        self.start = start_node
        

    def generate_spanning_tree(self, dim):
        """
        Generates a spanning tree using BFS.

        Args:
            dim: a tuple of integers (n,h) where n is the max number of
                 children a vertex can have, and h is the height of the tree.
        """
        pass

    def solve(self, target):
        """
        Finds the shortest path of the tree that represents the maze using BFS.
        
        Args:
            target: A Node representing the target for the BFS search and
                shortest path.
        """
        visited = {} # key is the visited node, val is the node it came from

        visited[self.start] = None
        queue = deque([self.start])

        # If there are elements in the queue...
        while queue:
            node = queue.popleft() # visit a node, therefore pop it out

            # Target located:
            if node == target:
                path = []
                while node:
                    path.append(node)
                    node = visited[node]  # Walk back
                return path[::-1]  # Reverse it
            
            # We didn't find the target, so find neighbors and add to queue.
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited[neighbor] = node
                    queue.append(neighbor)
            