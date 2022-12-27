import numpy as np
import sys 
import random
import math

def lire_instance(filename):
    with open(filename, 'r') as f:
        first_line = f.read()
        tokens = first_line.split()
        n = int(tokens[0])
        XY = np.zeros((n,2))
        for i in range(n):
            for j in range(2):
                XY[i,j] = int(tokens[i * 3 + j + 2])
    return XY, n

#2.1
def init_solution(n):
    solution_init = random.sample(range(1,n+1), n)
    return solution_init

#2.2
def euclidean_distance(point1, point2):
    # Calcule la distance euclidienne entre les points point1 et point2
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def calcule_solution(XY, s, n):
    valeur = euclidean_distance([0,0], XY[s[0]-1])
    for i in range(n-1):
        valeur+= euclidean_distance(XY[s[i]-1], XY[s[i+1]-1])
    valeur += euclidean_distance(XY[s[n-1]-1], [0,0])
    return valeur

#2.3




if len(sys.argv) != 2:
    print("Needed Instance Name, MAX_DEPL, MAX_ESSAIE")
    sys.exit(1)

XY, n = lire_instance(sys.argv[1])
s = init_solution(n)
print(s, calcule_solution(XY, s, n))
