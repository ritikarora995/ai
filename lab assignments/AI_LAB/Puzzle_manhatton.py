# If the initial and final states are as below and H(n): Manhattan distance as the heuristic function.
# You need to use Best First Search algorithm.

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
        return (1)
    else:
        return (0)

# find_pos function return the position of 0

def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return ([i, j])

# find_pos function return the position of val
def find_pos_val(g, val):
    for i in range(3):
        for j in range(3):
            if g[i][j] == val:
                return [i, j]

# manhattan_value function calculate the manhattan value

def manhatton_value(s, g):
    heuristic_value = 0
    for i in range(3):
        for j in range(3):
            pos = find_pos_val(g, s[i][j])
            m, n = pos
            heuristic_value = heuristic_value + abs(i - m) + abs(j - n)
    # print(heuristic_value)
    return heuristic_value


def up(s, pos):
    i = pos[0]
    j = pos[1]
    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i - 1][j]
        temp[i - 1][j] = 0
        return (temp)
    else:
        return (s)


def down(s, pos):
    i = pos[0]
    j = pos[1]
    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0
        return
        (temp)
    else:
        return (s)


def right(s, pos):
    i = pos[0]
    j = pos[1]
    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j + 1]
        temp[i][j + 1] = 0
        return (temp)
    else:
        return (s)


def left(s, pos):
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j - 1]
        temp[i][j - 1] = 0
        return (temp)
    else:
        return (s)


def enqueue(s, val):
    global q
    q = q + [[val, s]]


def heuristic(s, g):
    d = manhatton_value(s, g)
    return d

# deqeue function first sort the q and compare heuristiv with  current heuristic
# if current heuristic value is less than the previous
# then insert the first element list in visited list
# after inserting delete the first element from the q

def dequeue(prev_heuristic,current_state):
    global q
    global visited

    q.sort()
    if q[0][0]<prev_heuristic:
        visited = visited + [q[0][1]]
        elem = q[0][1]
        del q[0]
        return (elem)
    else:
        return  current_state



def search(s, g):

    curr_state = copy.deepcopy(s)
    prev_heuristic = heuristic(curr_state,g)
    if s == g:
        return
    global visited
    while (1):
        pos = find_pos(curr_state)
        new = left(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are:")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = up(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are: ")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = down(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are: ")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = right(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("found!! The intermediate states are: ")
                print(visited + [g])
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))
        print(q)

        if len(q) > 0:

            curr_state = dequeue(prev_heuristic,curr_state)
            print(curr_state)
            print(visited)
            if curr_state == s:
                print("not found")
                return
        else:
            print("not found")
            return


def main():
    # Initial state is vikas_singh_102067010
    vikas_singh_102067010 = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]
    g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    global q
    global visited
    q = q
    visited = visited + [vikas_singh_102067010]
    # print(manhatton_value(s,g))
    search(vikas_singh_102067010, g)


if __name__ == "__main__":
    main()
