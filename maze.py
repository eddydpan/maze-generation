class Cell:
    def __init__(self, x, y, start=False, end=False):
        self.x = x
        self.y = y
        self.start = start
        self.end = end
        #top, right, bottom, left
        self.walls = [True, True, True, True]
        self.path = [False, False, False, False]
        self.visited = False
        self.solution = False

    def remove_wall(side):
        self.walls[side] = False

class Maze:
    def __init__(self, width, height):
        self.grid = [[Cell(j+1, i+1) for j in range(width)] for i in range(height)]
        self.width = width
        self.height = height

    def __str__(self):
        cur_string = ""
        for i in self.grid:
            for j in i:
                cur_string = cur_string + "| "
            cur_string = cur_string + "|\n"
        return cur_string

    def get_cell(self, x, y):
        return self.grid[y-1][x-1]

    def adjacency_matrix(self):
        def coordinates_to_node(x, y):
            return (y-1) * self.height + x
        adjacency_matrix = {}
        for row in self.grid:
            for cell in row:
                adjacent = []
                if cell.y != 1:
                    up_cell = self.get_cell(cell.x, cell.y-1)
                    adjacent.append(coordinates_to_node(up_cell.x, up_cell.y))
                if cell.x != self.width:
                    right_cell = self.get_cell(cell.x+1, cell.y)
                    adjacent.append(coordinates_to_node(right_cell.x, right_cell.y))
                if cell.y != self.height:
                    bottom_cell = self.get_cell(cell.x, cell.y+1)
                    adjacent.append(coordinates_to_node(bottom_cell.x, bottom_cell.y))
                if cell.x != 1:
                    left_cell = self.get_cell(cell.x-1, cell.y)
                    adjacent.append(coordinates_to_node(left_cell.x, left_cell.y))
                adjacency_matrix[str(coordinates_to_node(cell.x, cell.y))] = adjacent
        return adjacency_matrix