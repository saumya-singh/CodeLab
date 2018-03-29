import pprint


class Graph:

    def __init__(self, grid):
        self.grid = grid
        self.edges = {}
        self.cost = {}
        self.neighbors()
        self.weight()

    def neighbors(self):
        rows = len(self.grid)
        columns = len(self.grid[0])
        for x in range(rows):
            for y in range(columns):
                if self.grid[x][y] == 0:
                    connections = []
                    if x-1 >= 0 and self.grid[x-1][y] == 0:
                        connections.append((x-1, y))
                    if x+1 < rows and self.grid[x+1][y] == 0:
                        connections.append((x+1, y))
                    if y-1 >= 0 and self.grid[x][y-1] == 0:
                        connections.append((x, y-1))
                    if y+1 < columns and self.grid[x][y+1] == 0:
                        connections.append((x, y+1))
                    if x-1 >= 0 and y-1 >= 0 and self.grid[x-1][y-1] == 0:
                        connections.append((x-1, y-1))
                    if x+1 < rows and y+1 < columns and self.grid[x+1][y+1] == 0:
                        connections.append((x+1, y+1))
                    if x+1 < rows and y-1 >= 0 and self.grid[x+1][y-1] == 0:
                        connections.append((x+1, y-1))
                    if x-1 >= 0 and y+1 < columns and self.grid[x-1][y+1] == 0:
                        connections.append((x-1, y+1))
                    self.edges[(x, y)] = connections

    def weight(self):
        for edge, connections in self.edges.items():
            for connection in connections:
                cost = input("Enter the cost of edge {} and {}: "
                             .format(edge, connection))
                self.cost[edge, connection] = int(cost)

    def astar_search(self, start, end):
        pass


class MakeGrid:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.init_grid = [[0 for column in range(y)] for row in range(x)]

    def add_blocked_cells(self, blocked_coordinates):
        for cell in blocked_coordinates:
            x, y = cell
            self.init_grid[x][y] = 1
        return self.init_grid


if __name__ == "__main__":
    x, y = map(int, input("Enter the grid size(rows, columns): ").split())
    grid = MakeGrid(x, y)
    blocked_coordinates = []
    blocked_coords = list(input("Enter the blocked co-ordinate: ").split())
    for blocked_coord in blocked_coords:
        one_blocked_cell = tuple(map(int, blocked_coord.split(",")))
        blocked_coordinates.append(one_blocked_cell)
    final_grid = grid.add_blocked_cells(blocked_coordinates)
    for row in final_grid:
        for cell in row:
            print(cell, end=" ")
        print(end="\n")
    print("\n\n")
    graph = Graph(final_grid)
    print("\n\n")
    start = tuple(map(int, input("Enter the start co-ordinate: ").split(",")))
    end = tuple(map(int, input("Enter the start co-ordinate: ").split(",")))
    path = graph.astar_search(start, end)
    print("="*25)
    print(path)
