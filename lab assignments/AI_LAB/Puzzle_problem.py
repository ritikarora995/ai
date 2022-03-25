import sys
import copy


def find_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return ([i, j])


def right(a, pos):
    i, j = pos

    if j < 2:
        t = copy.deepcopy(a)
        t[i][j] = t[i][j + 1]
        t[i][j + 1] = 0
        return (t)
    else:
        return (a)


def left(a, pos):
    i, j = pos

    if j > 0:
        t = copy.deepcopy(a)
        t[i][j] = t[i][j - 1]
        t[i][j - 1] = 0
        return (t)
    else:
        return (a)


def up(a, pos):
    i, j = pos

    if i > 0:
        t = copy.deepcopy(a)
        t[i][j] = t[i-1][j]
        t[i-1][j] = 0
        return (t)
    else:
        return (a)


def down(a, pos):
    i, j = pos

    if i < 2:
        t = copy.deepcopy(a)
        t[i][j] = t[i + 1][j]
        t[i + 1][j] = 0
        return (t)
    else:
        return (a)

 # current_state, cost, cost = number of misplaced tiles/ Manhattan distance
def enqueue(a):
    global q
    q = q + [a]


def dequeue(g):
    global q
    global visited
    q.sort()
    visited = visited + q[0]
    elem = q[0]
    del q[0]
    return (elem)


def search(s, g):
    curr_state = copy.deepcopy(s)
    if s == g:
        return

    global visited
    while (1):
        pos = find_pos(curr_state)

        new = down(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State Reached!!")
                print("The intermediate states are:")
                visited = visited + [g]
                for i in visited:
                    for j in i:
                        print(j)
                    print(" ")
                print("\n")
                return
            else:
                if new not in visited:
                    enqueue(new)

        new = up(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State Reached!!")
                print("The intermediate states are:")
                visited = visited + [g]

                for i in visited:
                    for j in i:
                        print(j)
                    print(" ")
                print("\n")
                return
            else:
                if new not in visited:
                    enqueue(new)

        new = left(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State Reached!!")
                print("The intermediate states are:")
                visited = visited + [g]
                for i in visited:
                    for j in i:
                        print(j)
                    print(" ")
                print("\n")
                return
            else:
                if new not in visited:
                    enqueue(new)

        new = right(curr_state, pos)
        if new != curr_state:
            if new == g:
                print("Goal State Reached!!")
                print("The intermediate states are:")
                visited = visited + [g]
                for i in visited:
                    for j in i:
                        print(j,end=" ")
                    print("")
                return
            else:
                if new not in visited:
                    enqueue(new)

        if len(q) > 0:
            curr_state = dequeue(q)
        else:
            print("not found")
            return

if __name__ == "__main__":
    s = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    q = []
    visited = []

    q = q
    visited = visited + [s]

    search(s, g)