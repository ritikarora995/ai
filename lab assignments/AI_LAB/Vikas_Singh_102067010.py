
from copy import deepcopy

# declare global variables
q = []
visited = []


def compare(s, g):
    if s == g:
        return 1
    else:
        return 0


def position(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return (i, j)


def heuristic(new, g):
    d = 0
    for i in range(3):
        for j in range(3):
            if new[i][j] != g[i][j]:
                d += 1

    return d


def enqueue(new, val):
    global q
    q = q + [(val, new)]


def dequeue():
    global q
    global visited

    q.sort()
    temp = q[1:3]
    visited = visited + [q[0][1]]
    elem = q[0][1]
    q =[]
    q = temp
    return elem


def up(s, pos):
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j - 1]
        temp[i][j - 1] = 0
        return temp
    else:
        return s


def down(s, pos):
    i = pos[0]
    j = pos[1]
    if j < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i][j + 1]
        temp[i][j + 1] = 0
        return temp
    else:
        return s


def right(s, pos):
    i = pos[0]
    j = pos[1]
    if i < 2:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0
        return temp
    else:
        return s


def left(s, pos):
    i = pos[0]
    j = pos[1]
    if i > 0:
        temp = copy.deepcopy(s)
        temp[i][j] = temp[i - 1][j]
        temp[i - 1][j] = 0
        return temp
    else:
        return s


def beam_search(s, g):
    curr_state = copy.deepcopy(s)
    while 1:
        global q
        global visited
        pos = position(curr_state)

        new = up(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal state found !! \nIntermediate states are : ")
                # print(visited + [g])
                for i in visited:
                    print(i)
                print("Final goal state is: \n",g)
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = down(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal state found !! \nIntermediate states are : ")
                # print(visited + [g])
                for i in visited:
                    print(i)
                print("Final goal state is: \n",g)
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = left(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal state found !! \nIntermediate states are : ")
                # print(visited + [g])
                for i in visited:
                    print(i)
                print("Final goal state is: \n",g)
                return

            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        new = right(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal state found !! \nIntermediate states are : ")
                # print(visited + [g])
                for i in visited:
                    print(i)
                print("Final goal state is: \n",g)
                return
            else:
                if new not in visited:
                    enqueue(new, heuristic(new, g))

        if len(q) > 0:
            curr_state = dequeue()
        else:
            print("Not Found !!")
            return


# Initial state
initial_state = [[2, 4, 3], [1, 0, 8], [7, 6, 5]]
# Goal state
goal_state = [[1, 2, 3], [4, 0, 8], [7, 6, 5]]
beam_search(initial_state, goal_state)
