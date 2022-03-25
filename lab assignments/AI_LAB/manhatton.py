

def find_pos(g,val):
    for i in range(3):
        for j in range(3):
            if g[i][j] == val:
                return ([i, j])

def manhatton_value(s,g):
    heuristic =0
    for i in range(3):
        for j in range(3):
            if s[i][j] !=0:
                pos = find_pos(g,s[i][j])
                m,n = pos
                heuristic = heuristic + abs(i-m)+abs(j-n)
    return heuristic

def euclidean_value(s,g):
    heuristic =0
    for i in range(3):
        for j in range(3):
            if s[i][j] !=0:
                pos = find_pos(g,s[i][j])
                m,n = pos
                heuristic =heuristic + (abs(i-m)**2+abs(j-n)**2)**(1/2)
    return heuristic

def minkowski_value(s,g,p):
    heuristic =0
    for i in range(3):
        for j in range(3):
            if s[i][j] !=0:
                pos = find_pos(g,s[i][j])
                m,n = pos
                heuristic =heuristic + (abs(i-m)**p+abs(j-n)**p)**(1/p)
    return heuristic

if __name__ == "__main__":
    s = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    g = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    print("Manhatton distance is : ",manhatton_value(s,g))
    print("Euclidean distance is : ", euclidean_value(s, g))
    p = int(input("Enter value of p : "))
    print("Minkowaski distance is : ", minkowski_value(s, g,p))
