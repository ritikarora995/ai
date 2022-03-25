# graph = {
#     'A': ['C', 'B'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F', 'G'],
#     'F': [],
#     'G': []
# }
#
# visited = []  # List to keep track of visited nodes.
# stack = []  # Initialize a stack
#
#
# def bfs(visited, graph, node):
#     visited.append(node)
#     stack.append(node)
#
#     while stack:
#         s = stack.pop()
#         print(s, end=" ")
#
#         for neighbour in graph[s]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 stack.append(neighbour)
#
#
# # Driver Code
#
# bfs(visited, graph, 'A')
#


graph = {
    '0': ['1', '2','3'],
    '1': ['4'],
    '4': ['7'],
    '7': ['9'],
    '9': ['11'],
    '11': [],
    '2': ['5','6'],
    '3': ['11'],
    '6': ['8'],
    '8': ['11','10'],
    '5': [],
    '10': [],
    '1': ['4']

}

visited = []  # List to keep track of visited nodes.
stack = []  # Initialize a stack


def dfs(visited, graph, node):
    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


# Driver Code

dfs(visited, graph, '0')
