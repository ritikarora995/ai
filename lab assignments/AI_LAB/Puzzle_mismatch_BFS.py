# If the initial and final states are as below and H(n): number of misplaced tiles in the current state
# n as compared to the goal node need to be considered as the heuristic function. You need to use
# Hill Climbing algorithm.

"""
    Name :- VIKAS SINGH
    Roll number :- 102067010
    Group :- 2CS3
"""

import sys
import copy

# Create a two empty list which is global q and visited
q = []
visited = []


# Create a Compare function takes two arguments s and g
# if s and g is equal it will return 1 else it will return 0

def compare(s, g):
    if s == g:
        return 1
    else:
        return 0

# find_pos function return the position of 0

def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return [i, j]

#  Move the 0 in upward direction if i>0 else do nothing simply return s which is pass in the function
def up(s, pos):
    i = pos[0]
    j = pos[1]
    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i - 1][j]
        temp[i - 1][j] = 0
        return temp
    else:
        return s

#  Move the 0 in downward direction if i<2 else do nothing simply return s which is pass in the function
def down(s, pos):
    i = pos[0]
    j = pos[1]
    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0
        return temp
    else:
        return (s)

#  Move the 0 in rightward direction if j<2 else do nothing simply return s which is pass in the function
def right(s, pos):
    i = pos[0]
    j = pos[1]
    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j + 1]
        temp[i][j + 1] = 0
        return temp
    else:
        return s

# Move the 0 in leftward direction if j>0 else do nothing simply return s which is pass in the function
def left(s, pos):
    i = pos[0]
    j = pos[1]
    if j >0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j - 1]
        temp[i][j - 1] = 0
        return temp
    else:
        return s

# enqueue function insert the s and val in q
def enqueue(s, val):
    global q
    q = q + [(val, s)]

# calculte the heuristic value
def heuristic(s, g):
    d = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] != g[i][j]:
                d += 1
    # print(d)
    return d

# deqeue function first sort the q and then insert the first element list in visited list
# after inserting delete the first element from the q

def dequeue():
    global q
    global visited
    q.sort()
    visited = visited + [q[0][1]]
    elem = q[0][1]
    del q[0]
    return elem


def search(s, g):
    # create a curr_state variable and assign the deepcopy of s
    curr_state = copy.deepcopy(s)
    if s == g:
        return
    global visited
    while (1):
        # find the postition of 0 in the current state
        pos = find_pos(curr_state)

        new = up(curr_state, pos)  # move 0 upward if possible
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are: ")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = down(curr_state, pos)  # move 0 downward if possible
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are: ")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = right(curr_state, pos)  # move 0 rightward if possible
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are: ")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = left(curr_state, pos)   # move 0 leftward if possible
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are: ")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        if len(q) > 0:
            curr_state = dequeue()
        else:
            print("not found")
            return


def main():
    # Initial state is vikas_singh_102067010
    vikas_singh_102067010 = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    global q
    global visited
    q = q
    visited = visited + [vikas_singh_102067010]

    search(vikas_singh_102067010, g)


if __name__ == "__main__":
    main()
