"""
Python module that implements a Breadth-first Search class.
"""
from search import Search
from collections import deque
from maze import Maze
import random

class BFS(Search):
    def __init__(self, graph=None, start_node='1'):
        """
        Initializes a BFS object that stores a graph and its starting node.

        Args:
            graph: A dictionary where the keys are ___ representing each of
                the nodes, and the values are a list of all adjacent nodes. 
            start_node: A ___ representing the starting node.
        """
        self.graph = graph
        self.start = start_node
        
    def generate_spanning_tree(self):
        """
        Generates a spanning tree using BFS starting at the top left corner and
        ending at the bottom right corner.

        Args:
            dim: a tuple of integers (w, h) where w is the width of the
                graph, and h is the height.
        """
        # Retrieve the adjacency matrix from the Maze class
        adj_matrix = self.graph
        
        # Initialize graph with all vertices but no edges
        adj_graph = {node: [] for node in adj_matrix}
        solution = {}
        
        visited = set() # Dictionary to keep track of the parent to each visited node
        # visited[self.start] = None # The source does not have a parent
        queue = deque([(self.start, None)])
        # next_node = None

        while queue:
            queue_nodes = []
            node, parent = queue.popleft()  # Visit a node
            if node not in visited and parent is not None:
                solution[str(node)] = int(parent)
                adj_graph[parent].append(node)
                adj_graph[node].append(parent)
            visited.add(node)
            
            
            # breakpoint()

            neighbor_list = adj_matrix[node]
            random.shuffle(neighbor_list)
            
            for i in range(len(queue)):
                queue_nodes.append(queue[i][0])
            # Iterate over shuffled neighbors
            for neighbor in neighbor_list:
                neighbor = str(neighbor)
                if neighbor not in visited and neighbor not in queue_nodes:
                    # Add edge to the spanning tree
                    # adj_graph[node].append(neighbor)
                    # adj_graph[neighbor].append(node)  # Undirected edge
                    queue.append((neighbor, node))  # Add unvisited neighbor to queue with node as its parent
                    # visited.add(neighbor)
                    # next_node = neighbor
                    # visited[neighbor] = node
        print(solution)
        return solution
            



    # def generate_spanning_tree(self, dim):
    #     """
    #     Generates a spanning tree using BFS starting at the top left corner and
    #     ending at the bottom right corner.

    #     Args:
    #         dim: a tuple of integers (w, h) where w is the width of the
    #             graph, and h is the height.
    #     """
    #     # key is the visited node and the values are the edges
        
    #     neighbors = Maze(dim[0], dim[1]).adjacency_matrix()
    #     # Initialize graph with all vertices but no edges
    #     adj_graph = {}
    #     for node in neighbors.keys():
    #         adj_graph[node] = []

    #     # node_idx = 1
    #     # # Initialize graph matrix.
    #     # for w in range(dim[0]):
    #     #     for h in range(dim[1]):
    #     #         # Set each node to be a key with an empty list as its value
    #     #         adj_graph['{node_idx}'] = [] 
    #     #         node_idx += 1


    #     # Start at the top left node, reference as Node '1'
    #     visited = set()
    #     queue = deque([self.start])
    #     last_node = None
    #     # If there are elements in the queue...
    #     while queue:
    #         if last_node is not None:
    #             adj_graph[node].append(last_node)
    #         node = queue.popleft() # visit a node, therefore pop it out            
    #         visited.add(node)
    #         # Find neighbors and add to queue.
    #         for neighbor_list in neighbors[node]:
    #             # Shuffle the list of neihgbors to add randomness
    #             random.shuffle(neighbor_list)
    #             for neighbor in neighbor_list:
    #                 if neighbor not in visited: 
    #                     queue.append(neighbor)
           
    #         last_node = node

            

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
            