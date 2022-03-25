import math
initial_state = [[2,0,3], [1,8,4], [7,6,5]]
goal_state = [[1,2,3], [8,0,4], [7,6,5]]
a=[]
b=[]
c=[]
s1=0
s2=0
s3=0
for i in range(3):
  for k in range(3):
    a=(initial_state[i][k]-goal_state[i][k])**2
    s1=s1+a
print("Value of Heuristic function using Euclidian distance is ",math.sqrt(s1))
for i in range(3):
  for k in range(3):
    b=(initial_state[i][k]-goal_state[i][k])
    s2=s2+abs(b)
print("Value of Heuristic function using Manhattan distance is ",s2)
p=float(input("Enter the value of p: "))
for i in range(3):
  for k in range(3):
    c=(initial_state[i][k]-goal_state[i][k])**(p)
    s3=s3+abs(c)
print("Value of Heuristic function using Minkowski distance is ",s3**(1/p))