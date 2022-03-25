# Solve the following problem using beam search algorithm, by taking
# (i) Beam width =2
# (ii) Beam width =3
# Heuristic values are given in the diagram; A is the starting node and G is the goal node

"""
    Name :- VIKAS SINGH
    Roll number :- 102067010
    Group :- 2CS3
"""


b = int(input("Enter beta : "))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G':[]
}
heuristic ={
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 2,
    'E': 2,
    'F': 3,
    'G':0
}


visited = []  # List to keep track of visited nodes.
path = []
q = []  # Initialize a queue
def enqueue(node,val):
    global q
    q = q + [(val,node)]

def dequeue():
    global q
    global visited
    global path
    global b
    q.sort()
    # print("Nodes present in queue at current level : ",q)
    # print("Nodes that are visited is : ",visited)
    temp = q[1:b]
    # print("Values in temp ",temp)
    visited = visited + [q[0][1]]
    path = path +[q[0][1]]
    elem = q[0][1]
    q = []
    q = temp
    return elem


def bfs(visited, graph, node,goal):
    # path.append(node)
    enqueue(node,heuristic[node])
    flag = 0
    while len(q):
        # print(len(q))
        s = dequeue()
        if s==goal:
            print("Goal state found ")
            print(path)
            flag = 1
            break


        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                enqueue(neighbour,heuristic[neighbour])

    if flag == 0:
        print("Goal state not reachable!!")
        print(path)
        return

# Driver Code

bfs(visited, graph, 'A','G')
