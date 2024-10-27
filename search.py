"""
A Python module for the abstract Search class that the BFS and DFS classes will
inherit from.
"""
from abc import ABC, abstractmethod

class Search(ABC):
    """
    An abstract class that BFS and DFS inherit from.
    """
    @abstractmethod
    def __init__(self, graph=None, start_node='1'):
        self.graph = graph
        self.start = start_node

    @abstractmethod
    def generate_spanning_tree(self, dim):
        """
        Generates a spanning tree.

        Args:
            dim: a tuple of integers (w, h) where w is the width of the
                graph, and h is the height.
        """
        pass
    
    @abstractmethod
    def solve(self, target):
        """
        Finds the shortest path of the tree that represents the maze using BFS.
        
        Args:
            target: A String of an int representing the target node to find the
                shortest path to.
        """
        pass