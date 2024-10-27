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
    def __init__(self, graph=None, start_node=None):
        self.graph = graph
        self.start = start_node

    @abstractmethod
    def generate_spanning_tree(self, dim):
        pass
    
    @abstractmethod
    def solve(self):
        pass