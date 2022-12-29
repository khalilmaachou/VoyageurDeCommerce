import numpy as np
import sys 
import random
import math
import copy

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
    # Calcule la distance euclidienne entre deux points
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def calculer_solution(XY, s, n):
    valeur = euclidean_distance([0,0], XY[s[0]-1])
    
    for i in range(n-1):
        valeur+= euclidean_distance(XY[s[i]-1], XY[s[i+1]-1])
    
    valeur += euclidean_distance(XY[s[n-1]-1], [0,0])
    
    return valeur

#2.3
def meilleur_voisin(XY, s, n):
    val_min = math.inf
    solutions = []

    for i in range(n):
        for j in range(i+1,n):
        
            s_loc = copy.copy(s)
            s_loc[i], s_loc[j] = s_loc[j], s_loc[i]
            val_loc = calculer_solution(XY, s_loc, n)
        
            if val_loc <= val_min:
                solutions.append(s_loc)
                val_min = val_loc
    
    indice = random.randint(0, len(solutions) - 1)
    return solutions[indice] 

#2.4
def meilleur(s_prime, s, XY, n):
    return calculer_solution(XY, s, n) > calculer_solution(XY ,s_prime ,n)

def hill_climbing_red(XY ,max_essais ,n):
    # On effectue plusieurs essais de hill climbing
    for i in range(max_essais):
        # solution initiale au hasard
        solution = init_solution(n)
        print(f"Essai {i+1} : solution initiale = {solution}")

        nb_depl = 0

        STOP = False
        while not STOP:
            # On cherche le meilleur voisin
            voisin = meilleur_voisin(XY ,solution, n)

            if meilleur(voisin, solution, XY, n):
                solution = voisin
            else:
                STOP = True
                
            nb_depl += 1

        print(f"Solution finale = {solution} valeur => {calculer_solution(XY,solution,n)} (nombre de déplacements = {nb_depl})")

#2.5
def meilleur_voisin_non_tabou(XY ,Tabou ,s ,n):
    val_min = math.inf
    solutions = []

    for i in range(n):
        for j in range(i+1,n):
        
            s_loc = copy.copy(s)
            s_loc[i], s_loc[j] = s_loc[j], s_loc[i]
            val_loc = calculer_solution(XY, s_loc, n)
        
            if (val_loc <= val_min) and (s_loc not in Tabou):
                solutions.append(s_loc)
                val_min = val_loc
    
    if len(solutions) != 0:
        indice = random.randint(0, len(solutions) - 1)
        return solutions[indice] 
    else:
        return None

def tabou(XY, max_depl, n, tabou_size):
    # solution initiale au hasard
    solution = init_solution(n)
    print(f"MAX_DEPL {max_depl} : solution initiale = {solution}")

    # initialise la liste tabou
    Tabou = []

    msol = solution
    nb_depl = 0
    STOP = False

    while (nb_depl < max_depl) and (not STOP):
        voisin = meilleur_voisin_non_tabou(XY, Tabou, solution, n)
        if voisin == None:
            STOP = True
        
        Tabou.append(solution)
        if meilleur(voisin, msol, XY, n):
            msol = voisin
        solution = voisin
        nb_depl += 1
        if len(Tabou) > tabou_size:
            Tabou.pop(0)

    print(f"Solution finale = {solution} valeur => {calculer_solution(XY,msol,n)} (nombre de déplacements = {nb_depl})")


if len(sys.argv) != 3:
    print("Needed Instance Name, MAX_ESSAIE")
    sys.exit(1)

XY, n = lire_instance(sys.argv[1])
MAX_ESSAIE = int(sys.argv[2])
tabou(XY,10, n, 10)

