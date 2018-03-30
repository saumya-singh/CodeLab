import sys
import math
from queue import PriorityQueue


class Graph:

    def __init__(self, grid):
        self.grid = grid
        self.nonblock_vertices = []
        self.edges = {}
        self.cost = {}
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.non_block_vertices()
        self.neighbors()
        self.weight()

    def non_block_vertices(self):
        for x in range(self.rows):
            for y in range(self.columns):
                if self.grid[x][y] == 0:
                    self.nonblock_vertices.append((x, y))

    def neighbors(self):
        for x in range(self.rows):
            for y in range(self.columns):
                if self.grid[x][y] == 0:
                    connections = []
                    if x-1 >= 0 and self.grid[x-1][y] == 0:
                        connections.append((x-1, y))
                    if x+1 < self.rows and self.grid[x+1][y] == 0:
                        connections.append((x+1, y))
                    if y-1 >= 0 and self.grid[x][y-1] == 0:
                        connections.append((x, y-1))
                    if y+1 < self.columns and self.grid[x][y+1] == 0:
                        connections.append((x, y+1))
                    if x-1 >= 0 and y-1 >= 0 and self.grid[x-1][y-1] == 0:
                        connections.append((x-1, y-1))
                    if x+1 < self.rows and y+1 < self.columns and \
                            self.grid[x+1][y+1] == 0:
                        connections.append((x+1, y+1))
                    if x+1 < self.rows and y-1 >= 0 and \
                            self.grid[x+1][y-1] == 0:
                        connections.append((x+1, y-1))
                    if x-1 >= 0 and y+1 < self.columns and \
                            self.grid[x-1][y+1] == 0:
                        connections.append((x-1, y+1))
                    self.edges[(x, y)] = connections

    def weight(self):
        for edge, connections in self.edges.items():
            for connection in connections:
                cost = input("Enter the cost of edge {} and {}: "
                             .format(edge, connection))
                self.cost[edge, connection] = int(cost)

    def path(self, start, end, came_from):
        if end not in came_from:
            print("NO ROUTE FROM START TO END CO-ORDINATES")
            sys.exit()
        path = []
        path.append(end)
        backtrack = came_from[end]
        while backtrack is not start:
            path.append(backtrack)
            backtrack = came_from[backtrack]
        path.append(start)
        path.reverse()
        return path

    def euclidean_distance(self, node1, node2):
        heuristic = math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)
        return int(heuristic)

    def astar_search(self, start, end):
        if start not in self.nonblock_vertices:
            print("START NODE SHOULD NOT BE BLOCKED")
            sys.exit()
        if end not in self.nonblock_vertices:
            print("END NODE SHOULD NOT BE BLOCKED")
            sys.exit()
        cost = {}
        came_from = {}
        vertices_covered = []
        queue_to_be_eval = PriorityQueue()
        cost[start] = 0
        came_from[start] = None
        queue_to_be_eval.put((0, start))
        while not queue_to_be_eval.empty():
            current_node = queue_to_be_eval.get()[1]
            if current_node == end:
                break
            for connection in self.edges[current_node]:
                if connection not in vertices_covered:
                    new_cost = cost[current_node] + self.cost[(current_node,
                                                               connection)]
                    if connection not in cost or \
                            new_cost < cost[connection]:
                        cost[connection] = new_cost
                        came_from[connection] = current_node
                        priority = cost[connection] + \
                            self.euclidean_distance(connection, end)
                        queue_to_be_eval.put((priority, connection))
            vertices_covered.append(current_node)
        return self.path(start, end, came_from)


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


def show_path(grid, path, start, end):
    for x, y in path:
        grid[x][y] = "*"
    grid[start[0]][start[1]] = "S"
    grid[end[0]][end[1]] = "E"
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print(end="\n")


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
    print("\n")
    graph = Graph(final_grid)
    print("\n")
    start = tuple(map(int, input("Enter the start co-ordinate: ").split(",")))
    end = tuple(map(int, input("Enter the end co-ordinate: ").split(",")))
    path = graph.astar_search(start, end)
    print("\n" + "="*25)
    show_path(final_grid, path, start, end)
