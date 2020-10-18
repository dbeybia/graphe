'''
DM Graphes
-------------------------------
DBEYBIA Mohamed Baha - 21911190
KERIMI Yacine
-------------------------------
'''
from math import sqrt
from parse_tsp import *
import parse_tsp
from os.path import isfile
from copy import deepcopy
from timeit import default_timer
from random import randrange


##################################################
### Algorithme H1 glouton
##################################################

def h1(n, cout, sommets):
    tour = [n]
    print(len(sommets))
    avisiter = list(range(1, len(sommets)+1)) # liste des sommets
    avisiter.remove(n) # supprimer element numero n
    while len(avisiter) > 0:
        m = 999999999
        mIdx = -1
        for target in avisiter:
            dist = cout[(target, tour[-1])]
            if dist < m:
                m = dist
                mIdx = target
                #print(mIdx)
        avisiter.remove(mIdx)
        tour.append(mIdx)
    return tour


##################################################
### Algorithme H2 glouton
##################################################

def h2(n, sommets, cout):
    tour = n # liste
    tour.append(n[0])
    avisiter = list(range(1, len(sommets)+1))
    avisiter.remove(n[0])
    avisiter.remove(n[1])
    while len(avisiter) > 0:
        m = 999999999
        mIdx = -1
        for element in range(0, len(tour) - 1):
            for target in avisiter:
                dist = cout[(target, tour[element])]
                dist1 = cout[(target, tour[element+1])]
                dist2 = cout[(tour[element],tour[element+1])]
                couts = (dist1 + dist) - dist2
                if(couts>0) and couts<m:
                    m = couts
                    mIdx = target
                    indice = element+1
        tour.insert(indice,mIdx)
        avisiter.remove(mIdx)
    return tour

##################################################
### Union-find
##################################################

class unionfind:
    def __init__(self, sommets):
        self.parent = {}
        self.rang = {}
        self.elements = sommets
        for i in self.elements:
            self.creerensemble(i)

    def creerensemble(self,i):
        self.parent[i]=i
        self.rang[i]=0

    def find(self,i):
        if self.parent[i]!=i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self,i,j):
        i = self.find(i)
        j = self.find(j)
        if i==j:
            return
        if self.rang[i]>self.rang[j]:
            self.parent[j]=i
        else:
            self.parent[i]=j
            if self.rang[i]==self.rang[j]:
                self.rang[j]+=1

##################################################
### 2-Approximation en Utilisant l'ARPM de Kruskal
##################################################

def deux_approximation(sommets, arretes, dic_arretes):
     n=len(sommets)
     tree = kruskal(sommets, arretes, dic_arretes)
     adj = {} # liste adjacence
     for arrete in tree:
          adj.setdefault(arrete[0],[]).append(arrete[1])
          adj.setdefault(arrete[1],[]).append(arrete[0])

     visites = dict.fromkeys(sommets, False)
     pile = [sommets[0]]
     tour = []
     while len(pile)>0:
          sommet = pile.pop()
          visites[sommet]=True
          tour.append(sommet)
          for i in adj[sommet]:
               if visites[i]!=True:
                    pile.append(i)
     return tour

##################################################
### Kruskal avec union-find
##################################################
def kruskal(sommets, arretes, dic_arretes):
    n = len(sommets)
    arbre = []
    uf = unionfind(sommets)
    arretes_tri = sorted(arretes, key = dic_arretes.get)
    taille=0
    for cur in arretes_tri:
        u = cur[0]
        v = cur[1]
        if uf.find(u)!=uf.find(v):
            arbre.append(cur)
            uf.union(u,v)
            taille+=1
            if taille==n-1:
                break
    return arbre

##################################################
### Calcul distance/cout
##################################################
def tour_distance(tour, cout):
    dist = 0
    idx = tour[-1]
    for sommet in tour:
        if(sommet!=idx):
            dist += cout[(sommet, idx)]
            idx = sommet
    return dist

##################################################
### Fonction permut_2_opt
##################################################

def permut_2_opt(tour, i, k):

    assert i >= 0 and i < (len(tour) - 1)
    assert k > i and k < len(tour)

    nouv_tour = tour[0:i]
    nouv_tour.extend(reversed(tour[i:k + 1]))
    nouv_tour.extend(tour[k + 1:])

    assert len(nouv_tour) == len(tour)
    return nouv_tour

##################################################
### Implementation algorithme de post-optimisation (2opt)
##################################################
def deux_opt(tour, cout):

    changement = True
    cycle_initale = tour
    distance_initial = tour_distance(tour, cout)
    while changement:
        changement = False
        for i in range(len(cycle_initale) - 1):
            for k in range(i + 1, len(cycle_initale)):
                nouv_tour = permut_2_opt(cycle_initale, i, k)
                nouv_distance = tour_distance(nouv_tour, cout)
                if nouv_distance < distance_initial:
                    distance_initial = nouv_distance
                    cycle_initale = nouv_tour
                    changement = True
                    break
            if changement:
                break
    assert len(cycle_initale) == len(tour)
    return cycle_initale


##################################################
### Affichage expiremntation
##################################################
'''
def affichage_expirementation(description):


    print("Nom : " + str(len(tour)))
    print("Fichier : " + str(len(tour)))
    print("Dimension : " + str(len(tour)))
    return True
'''
##################################################
### execution de l'algorithme
##################################################

def main():
    if len(argv) > 1 and isfile(argv[1]):

            ##################################################
            ### Test global sur tout les fichiers
            ##################################################



            ##################################################
            ### Parsing fichier et récuperation des données
            ### liste sommets, liste arretes, dictionnaire des
            ### couts
            ##################################################

            sommets, arretes, cout, description = parse_test(argv[1])
            assert len(sommets) != 0

            #sommets, arretes, cout, description, opt_tour = parse_test(argv[1])
            #sommets, arretes, cout, description = parse_test(argv[1])

            ##################################################
            ### Algorithme glouton H2 (et H1)
            ##################################################
            #print(description)
            liste_sommets = [1, 2]
            test_h2 = h2(liste_sommets, sommets, cout)
            #print(test_h2)
            print("Cout H2 : " , tour_distance(test_h2, cout))
            #print(test_h2)
            ##################################################
            ### 2 - Approximation (en utilisant L'ARPM de kruskal)
            ##################################################

            test_2ap = deux_approximation(sommets, arretes, cout)
            print("Cout 2-Approximation : " , tour_distance(test_2ap, cout))
            #print(test_2ap)
            ##################################################
            ### 2-OPT
            ##################################################

            #test_2_opt = two_opt_python(sommets, cout)
            test_2opt = deux_opt(sommets, cout)
            print("Cout 2-Opt : " , tour_distance(test_2opt, cout))

    else:
            print("Utilisiation : ", os.path.basename(__file__), " <fichier_test.tsp>")

main()
