# Solve this given problem using Uniform Cost search. A is the initial state and G is the goal state

"""
    Name :- VIKAS SINGH
    Roll number :- 102067010
    Group :- 2CS3
"""

from queue import PriorityQueue

class Graph:
    def __init__(self, V, E):
        self.V = V
        self._graph = {}

        for u, v, z in E:
            # 'A','B',10 ==>   A--10--B   && B--10--A into graph
            if u not in self._graph:
                self._graph[u] = set()
                self._graph[u].add((v, z))
            else:
                self._graph[u].add((v, z))

            if v not in self._graph:
                self._graph[v] = set()
                self._graph[v].add((u, z))
            else:
                self._graph[v].add((u, z))

        print(self._graph)

    def Solve(self, initial, goal):
        queue = PriorityQueue()  # used priorityqueue
        visited = set()

        queue.put((0, initial, [initial]))  # add root node into queue with priority 0 (priority,node,path)

        while queue:
            f, curr, path = queue.get()  # returns f --> pri , curr --> node , path --> path till node
            visited.add(curr)

            if curr == goal:  # if curr is goal then print the path and exit
                print(path)
                return

            for nbrs in self._graph[curr]:  # else explore the nbrs
                if nbrs not in visited:
                    queue.put((f + nbrs[1], nbrs[0],
                               path + [nbrs[0]]))  # ( (relative edge wt as prority) , (child_node) , (path-->child) )


if __name__ == '__main__':
    vikas_singh_102067010 = Graph({'A', 'B', 'C', 'S', 'G'}, {('A', 'S', 1), ('A', 'G', 10),
                                          ('S', 'B', 5), ('B', 'G', 5), ('G', 'C', 5), ('S', 'C', 15)})
    # print(vikas_singh_102067010)
    vikas_singh_102067010.Solve('A', 'C')
