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

    def remove_wall(self, side):
        self.walls[side] = False

class Maze:
    def __init__(self, width, height):
        self.grid = [[Cell(j+1, i+1) for j in range(width)] for i in range(height)]
        self.width = width
        self.height = height
        self.grid[0][0].walls[3] = False
        self.grid[width-1][height-1].walls[1] = False

    def __str__(self):
        cur_string = ""
        for i in self.grid:
            for j in i:
                cur_string = cur_string + "| "
            cur_string = cur_string + "|\n"
        return cur_string

    def get_cell(self, x, y):
        return self.grid[y-1][x-1]

    def draw_graph(self, steps_matrix):

        def node_to_coordinates(node):
            node = int(node)
            x = node % self.height
            if x == 0:
               x = self.width
            y = (node - x)/self.height + 1
            return (int(x),int(y))
        
        for node in steps_matrix.keys():
            xy_coords = node_to_coordinates(node)
            cell = steps_matrix[node]
            if cell == 0:
                continue
            xy_coords_cell = node_to_coordinates(cell)
            diff_x = xy_coords[0] - xy_coords_cell[0]
            diff_y = xy_coords[1] - xy_coords_cell[1]
            if diff_x == 1:
                self.get_cell(xy_coords[0], xy_coords[1]).remove_wall(3)
                self.get_cell(xy_coords[0]-1, xy_coords[1]).remove_wall(1)
            if diff_x == -1:
                self.get_cell(xy_coords[0], xy_coords[1]).remove_wall(1)
                self.get_cell(xy_coords[0]+1, xy_coords[1]).remove_wall(3)
            if diff_y == 1:
                self.get_cell(xy_coords[0], xy_coords[1]).remove_wall(0)
                self.get_cell(xy_coords[0], xy_coords[1]-1).remove_wall(2)
            if diff_y == -1:
                self.get_cell(xy_coords[0], xy_coords[1]).remove_wall(2)
                self.get_cell(xy_coords[0], xy_coords[1]+1).remove_wall(0)
        return xy_coords

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