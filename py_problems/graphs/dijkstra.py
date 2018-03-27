import sys
from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(set)
        self.distances = {}

    def add_vertex(self, node):
        self.vertices.add(node)

    def add_connection(self, from_node, to_node, weight):
        self.edges[from_node].add(to_node)
        self.distances[(from_node, to_node)] = weight

    def findMinimumDist(self, dist, shortest_path):
        _min = sys.maxsize
        for index, distance in enumerate(dist):
            if distance < _min and index not in shortest_path:
                _min = distance
                min_index = index
        return min_index

    def dijkstra(self, source_node):
        infinity = sys.maxsize
        n_vertices = len(self.vertices)
        dist = [infinity]*n_vertices
        dist[source_node] = 0
        shortest_path = []
        while len(shortest_path) < n_vertices:
            index = self.findMinimumDist(dist, shortest_path)
            shortest_path.append(index)
            for adj_node in self.edges[index]:
                d = self.distances[(index, adj_node)]
                if dist[adj_node] > d + dist[index]:
                    dist[adj_node] = d + dist[index]
        return dist


g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)
g.add_vertex(8)
g.add_connection()
