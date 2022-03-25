# Solve the following blocks world problem using Simple Hill Climbing Algorithm.
# Take the following heuristic function:
# +n for block which is resting on the current support structure and n is equal to number
# of blocks below it.
#  -n for block which is resting on the incurrent support structure and n is equal to
# number of blocks below it.

"""
    Name :- VIKAS SINGH
    Roll number :- 102067010
    Group :- 2CS3
"""

import copy

visited_states = []

def prev(goal_,ch):
    for i in range(len(goal_)):
        if goal_[i]==ch:
            if i==0:
                return -1
            else:
                return goal_[i-1]
# heuristic fn - number of misplaced blocks as compared to goal state
def heuristic(curr_state, goal_state):
    goal_ = goal_state[3]
    val = 0
    for i in range(len(curr_state)):
        check_val = curr_state[i]
        if len(check_val) > 0:
            for j in range(len(check_val)):

                if check_val[j] != goal_[j]:
                    # val-=1
                    val -= j
                else:
                    # val+=1
                    val += j

    return val


# generate next possible solution for the current state
def generate_next(curr_state, prev_heu, goal_state):
    global visited_states
    state = copy.deepcopy(curr_state)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    if (temp1 not in visited_states):
                        curr_heu = heuristic(temp1, goal_state)
                        # if a better state than previous state of found
                        if curr_heu > prev_heu:
                            child = copy.deepcopy(temp1)
                            return child

    # no better soln than current state is possible
    return 0


def solution_(init_state, goal_state):
    global visited_states

    # checking if initial state is already the final state
    if (init_state == goal_state):
        print(goal_state)
        print("solution found!")
        return

    current_state = copy.deepcopy(init_state)

    # loop while goal is found or no better optimal solution is possible
    while (True):

        # add current state to visited to avoid repetition
        visited_states.append(copy.deepcopy(current_state))

        print(current_state)
        prev_heu = heuristic(current_state, goal_state)

        # generate possible better child from current state
        child = generate_next(current_state, prev_heu, goal_state)

        # No more better states are possible
        if child == 0:
            print("Final state - ", current_state)
            return

        # change current state to child
        current_state = copy.deepcopy(child)


def main():
    # maintaining a global visited to save all visited and avoid repetition & infinite loop condition
    global visited_states
    # inputs
    # Initial state is vikas_singh_102067010
    vikas_singh_102067010 = [[], [], [], ['B', 'C', 'D', 'A']]
    goal_state = [[], [], [], ['A', 'B', 'C', 'D']]
    # goal_state = [[],[],[],['A','D','C','B']]
    print(goal_state[3])
    solution_(vikas_singh_102067010, goal_state)


if __name__=="__main__":
    main()