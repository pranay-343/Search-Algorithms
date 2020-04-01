import time
import math


class Graph:

    def __init__(self, adjacency_list, vert_coord):
        self.adjacency_list = adjacency_list
        self.vert_coord = vert_coord

    def get_nextneighbour(self, v):
        return self.adjacency_list[v]

    # heuristic function for h value
    def h(self, n, target_ver):
        a = vert_coord[n]
        b = self.vert_coord[target_ver]
        dx = abs(a[0] - b[0]) ** 2
        dy = abs(a[1] - b[1]) ** 2
        h = (math.sqrt(dx + dy)) * 10
        return h

    def astar(self, start_ver, target_ver):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_ver])
        closed_list = set([])

        # g contains current distances from start_ver to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_ver] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_ver] = start_ver

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if (n == None or g[v] + self.h(v, target_ver) < g[n] + self.h(n, target_ver)):
                    n = v

            if (n == None):
                print('Path does not exist!')
                return None

            # if the current node is the target_ver
            # then we begin reconstructin the path from it to the start_ver
            if (n == target_ver):
                final_path = []

                while parents[n] != n:
                    final_path.append(n)
                    n = parents[n]

                final_path.append(start_ver)

                final_path.reverse()

                print('Path found: {}'.format(final_path))
                return final_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_nextneighbour(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if (g[m] > g[n] + weight):
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)


            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


if __name__ == '__main__':

    adjacent = {}
    vert_coord = {}

    def add_edge(frm_ver, to_ver, cost=0):
        if frm_ver not in adjacent:
            adjacent[frm_ver] = []
        if to_ver not in adjacent:
            adjacent[to_ver] = []
        adjacent[frm_ver].append((to_ver, cost))
        adjacent[to_ver].append((frm_ver, cost))

    file = open("v.txt", "r")

    # Repeat for each song in the text file
    for line in file:
        # Let's split the line into an array called "fields" using the ";" as a separator:
        if line.startswith("#"):
            continue
        else:
            fields = line.split(",")

            # and let's extract the data:
            vertex = fields[0]
            x = int(int(fields[1]) / 10)
            y = int(fields[1]) % 10
            vert_coord[vertex] = []
            vert_coord[vertex].append(x)
            vert_coord[vertex].append(y)
    file.close()
    file2 = open("e.txt", "r")

    for line2 in file2:
        # Let's split the line into an array called "fields" using the "," as a separator:
        if line2.startswith("#"):
            continue
        else:
            fields = line2.split(",")
            vertex = fields[0]
            vertex1 = fields[1]
            distance = int(fields[2])
            add_edge(vertex, vertex1, distance)
    file2.close()

    graph1 = Graph(adjacent, vert_coord)
    start_time = time.time()  # execution time calculation starts from here
    #Enter your start vertex and goal vertex here:
    graph1.astar('4', '41')
    end_time = time.time()
    print("---------")
    print((end_time - start_time))
