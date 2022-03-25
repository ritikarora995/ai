# Python program to print all paths from a source to destination.

from collections import defaultdict

paths =[]
# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)
        global paths
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
            paths.extend(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


# Create a graph given in the above diagram
g = Graph(12)
g.addEdge(0, 1)
g.addEdge(1, 4)
g.addEdge(4, 7)
g.addEdge(7, 9)
g.addEdge(9, 11)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(6, 8)
g.addEdge(8, 10)
g.addEdge(8, 11)
g.addEdge(3,11)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(3, 0)
g.addEdge( 11,9)
g.addEdge(9, 7)
g.addEdge(7, 4)
g.addEdge(4, 1)
g.addEdge(11, 3)
g.addEdge(10, 8)
g.addEdge(8,6)
g.addEdge(5, 2)
g.addEdge(11,8)
g.addEdge(6,2)


s = 0
d = 11
print("Following are all different paths from % d to % d :" % (s, d))
g.printAllPaths(s, d)
print(paths)
cost=0
all_path_cost=[]
for i in paths:
    if i == 11:
        all_path_cost.extend([cost])
        cost =0
    else:
        cost+=i

print(all_path_cost)
print(all_path_cost.index(min(all_path_cost)))

