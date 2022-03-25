import copy
#RITIK ARORA
#102053036
class MyBlockProblem:
    def __init__(self_RITIK, start, goal):
        self_RITIK.currentState=start
        self_RITIK.goalState=goal
        self_RITIK.prevState=None

    def isGoalReached(self_RITIK):
        #print("In isGoalReached()")
        for i in range(0, 4):
            #print("Printing self_RITIK.currentState[i]")
            #print(self_RITIK.currentState[i])
            if self_RITIK.currentState[i]==goal:
                return True
        
        return False

    def displayState(self_RITIK):
        for i in range(0, 4):
            if self_RITIK.currentState[i]!=[]:
                print(f"Stack {i}:")
                print(self_RITIK.currentState[i])
                print("------------------")
        print("******************************************")

    def _eq_(self_RITIK, other):
        return self_RITIK.currentState==other.currentState

    def movefromStackXtoStackY(self_RITIK, x, y):
        if self_RITIK.currentState[x]!=[] and len(self_RITIK.currentState[y])!=4:
            self_RITIK.prevState=copy.deepcopy(self_RITIK)
            block=self_RITIK.currentState[x].pop()
            self_RITIK.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self_RITIK):
        #print("Over here")
        stateList=[]
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state=copy.deepcopy(self_RITIK)
                if i!=j and copy_state.movefromStackXtoStackY(i, j):
                    #copy_state.displayState()
                    stateList.append(copy_state)
                    #print("Appending to stateList ")
                    
        return stateList

    def heuristic(self_RITIK):
        value=0

        for i in range(0, 4):
            if self_RITIK.currentState[i]!=[]:
                if self_RITIK.currentState[i][0]==self_RITIK.goalState[0]:
                    value+=1
                    #print("First block +1")
                else:
                    #print("First block -1")
                    value-=1

        
        for i in range(0, 4):
            goalBlock=self_RITIK.goalState[i]
            goalBlockIndex=i
            for j in range(0, 4):
                flag=0
                for k in range(0, len(self_RITIK.currentState[j])):
                    if self_RITIK.currentState[j]!=[]: 
                        if self_RITIK.currentState[j][k]==goalBlock:
                            currentBlockIndexX=j
                            currentBlockIndexY=k
                            flag=1
                            break
                if flag==1:
                    flag=0
                    break
            
            if self_RITIK.currentState[currentBlockIndexX][currentBlockIndexY-1]==self_RITIK.goalState[goalBlockIndex-1] and currentBlockIndexY!=0 and goalBlockIndex!=0:
                #print(f"{self_RITIK.currentState[currentBlockIndexX][currentBlockIndexY]} rests on {self_RITIK.goalState[goalBlockIndex-1]}")
                value+=1
            else:
                if currentBlockIndexY!=0:
                    #print(f"{self_RITIK.currentState[currentBlockIndexX][currentBlockIndexY]} shouldn't rest on {self_RITIK.currentState[currentBlockIndexX][currentBlockIndexY-1]}") 
                    value-=1
                
        return value

def constructPath(goalState):
    print("Displaying path from start to goal")
    while goalState:
        goalState.displayState()
        goalState=goalState.prevState
    
    return 1

def HillClimbing(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)


    #Step 2
    returnVal=0
    while open:

        #
        thisState=open.pop(0)
        #print("Printing thisState")
        thisState.displayState()

        #Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            returnVal=constructPath(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                #If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)
    
    if returnVal!=1:
        print("Error: Local Maxima")

                
start=[[2, 3, 4, 1], [], [], []]
goal=[1, 2, 3, 4]
problem=MyBlockProblem(start, goal)
#print(problem.heuristic())
HillClimbing(problem)