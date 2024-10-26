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

class Maze:
    def __init__(self, width, height):
        self.cur_row = [[Cell(j, i) for j in range(width)] for i in range(height)]
        self.width = width
        self.height = height

    def __str__(self):
        cur_string = ""
        for i in self.cur_row:
            for j in i:
                cur_string = cur_string + "| "
            cur_string = cur_string + "|\n"
        return cur_string