# Python3 program to print BFS traversal from a given source vertex. BFS(int, s) traverses vertices reachable from s.

from collections import defaultdict

# Make a class represents a directed graph using adjacency list
# adjacency list is a collection of unordered lists to represent a finite graph.


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):

        visited = [False] * (len(self.graph))

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# create a graph to print
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
        " (starting from vertex 2)")
g.BFS(2)

# This is code is from:
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

