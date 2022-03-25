# # Python3 implementation of program to count
# # minimum number of steps required to measure
# # d litre water using jugs of m liters and n
# # liters capacity.
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# ''' fromCap -- Capacity of jug from which
# 	water is poured
#     toCap -- Capacity of jug to which
# 	water is poured
# d	-- Amount to be measured '''
#
#
# def Pour(toJugCap, fromJugCap, d):
#     # Initialize current amount of water
#     # in source and destination jugs
#     fromJug = fromJugCap
#     toJug = 0
#
#     # Initialize steps required
#     step = 1
#     while ((fromJug is not d) and (toJug is not d)):
#
#         # Find the maximum amount that can be
#         # poured
#         temp = min(fromJug, toJugCap - toJug)
#
#         # Pour 'temp' liter from 'fromJug' to 'toJug'
#         toJug = toJug + temp
#         fromJug = fromJug - temp
#
#         step = step + 1
#         if ((fromJug == d) or (toJug == d)):
#             break
#
#         # If first jug becomes empty, fill it
#         if fromJug == 0:
#             fromJug = fromJugCap
#             step = step + 1
#
#         # If second jug becomes full, empty it
#         if toJug == toJugCap:
#             toJug = 0
#             step = step + 1
#
#     return step
#
#
# # Returns count of minimum steps needed to
# # measure d liter
# def minSteps(n, m, d):
#     if m > n:
#         temp = m
#         m = n
#         n = temp
#
#     if d % (gcd(n, m)) is not 0:
#         return -1
#
#     # Return minimum two cases:
#     # a) Water of n liter jug is poured into
#     # m liter jug
#     return min(Pour(n, m, d), Pour(m, n, d))
#
#
# # Driver code
# if __name__ == '__main__':
#     n = 3
#     m = 5
#     d = 4
#
#     print('Minimum number of steps required is', minSteps(n, m, d))

print("Max capacity: Jug1 = 12, Jug2 = 8, Jug3 = 5")
print("Initial state: (12,0,0)")
print("Goal state: (6,x,y)")

jug1 = 12
jug2 = 0
jug3 = 0

i = 0
rule = [9, 11, 18, 12, 9, 11, 18]

while (jug1 != 6):
    # r=int(input("Enter rule:"))
    if (rule[i] == 1):
        jug1 = 12

    elif (rule[i] == 2):
        jug2 = 8

    elif (rule[i] == 3):
        jug3 = 5

    elif (rule[i] == 4):
        jug1 = 0

    elif (rule[i] == 5):
        jug2 = 0

    elif (rule[i] == 6):
        jug3 = 0

    elif (rule[i] == 7):
        jug2 -= 12 - jug1
        jug1 = 12

    elif (rule[i] == 8):
        jug1 += jug2
        jug2 = 0

    elif (rule[i] == 9):
        jug1 -= 8 - jug2
        jug2 = 8

    elif (rule[i] == 10):
        jug2 += jug1
        jug1 = 0

    elif (rule[i] == 11):
        jug2 -= 5 - jug3
        jug3 = 5

    elif (rule[i] == 12):
        jug3 += jug2
        jug2 = 0

    elif (rule[i] == 13):
        jug3 -= 8 - jug2
        jug2 = 8

    elif (rule[i] == 14):
        jug2 += jug3
        jug3 = 0

    elif (rule[i] == 15):
        jug1 -= 5 - jug3
        jug3 = 5

    elif (rule[i] == 16):
        jug3 += jug1
        jug1 = 0

    elif (rule[i] == 17):
        jug3 -= 12 - jug1
        jug1 = 12

    elif (rule[i] == 18):
        jug1 += jug3
        jug3 = 0

    else:
        print("Invalid choice!")

    print("Current state: ({},{},{})".format(jug1, jug2, jug3))
    i = i + 1
print("Goal state achieved")









