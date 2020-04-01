import sys
import heapq
import time

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacentnode = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def addnext_neighbor(self, neighbor, cost=0):
        self.adjacentnode[neighbor] = cost

    def get_connections(self):
        return self.adjacentnode.keys()

    def get_verid(self):
        return self.id

    def get_cost(self, neighbor):
        return self.adjacentnode[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacentnode: ' + str([x.id for x in self.adjacentnode])

    def __lt__(self, other):
        return self.distance < other.distance

class Graph:
    def __init__(self):
        self.vertexdict = {}
        self.verticesnum = 0

    def __iter__(self):
        return iter(self.vertexdict.values())

    def add_vertex(self, node):
        self.verticesnum = self.verticesnum + 1
        new_vertex = Vertex(node)
        self.vertexdict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertexdict:
            return self.vertexdict[n]
        else:
            return None

    def add_edge(self, frm_ver, to_ver, cost=0):
        if frm_ver not in self.vertexdict:
            self.add_vertex(frm_ver)
        if to_ver not in self.vertexdict:
            self.add_vertex(to)

        self.vertexdict[frm_ver].addnext_neighbor(self.vertexdict[to_ver], cost)
        self.vertexdict[to_ver].addnext_neighbor(self.vertexdict[frm_ver], cost)

    def get_vertices(self):
        return self.vertexdict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortestpath(ver, path):
    ''' make shortest path from v.previous'''
    if ver.previous:
        path.append(ver.previous.get_verid())
        shortestpath(ver.previous, path)
    return

def dijkstra(verGraph, startnode):

    startnode.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_nodes = [(ver.get_distance(), ver) for ver in verGraph]
    heapq.heapify(unvisited_nodes)

    while len(unvisited_nodes):
        # Pops a vertex with the smallest distance
        uv = heapq.heappop(unvisited_nodes)
        current = uv[1]
        current.set_visited()

        for next in current.adjacentnode:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + int(current.get_cost(next))
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # 1. Pop  item
        while len(unvisited_nodes):
            heapq.heappop(unvisited_nodes)
        # 2. Put all vertices not visited into the queue
        unvisited_nodes = [(v.get_distance(), v) for v in verGraph if not v.visited]
        heapq.heapify(unvisited_nodes)


if __name__ == '__main__':

    a = Graph()

    file = open("v.txt", "r")

    # Repeat for each song in the text file
    for line in file:
        # Let's split the line into an array called "fields" using the "," as a separator:
        if line.startswith("#"):
            continue
        else:
            fields = line.split(",")

            # and let's extract the data:
            vertex = fields[0]
            a.add_vertex(vertex)
    file.close()
    file2 = open("e.txt", "r")

    # Repeat for each song in the text file
    for line2 in file2:
        # Let's split the line into an array called "fields" using the ";" as a separator:
        if line2.startswith("#"):
            continue
        else:
            fields = line2.split(",")

            # and let's extract the data:
            vertex = fields[0]
            vertex1 = fields[1]
            distance = fields[2]
            a.add_edge(vertex, vertex1, distance)
    file2.close()
    start_time = time.time()
    #Enter your start vertex here:
    dijkstra(a, a.get_vertex('4'))
    end_time = time.time()
    #Enter your goal vertex here:
    target = a.get_vertex('41')
    finalpath = [target.get_verid()]
    shortestpath(target, finalpath)
    print(finalpath[::-1])
    print("---------")
    print((end_time - start_time))
