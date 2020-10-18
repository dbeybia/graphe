'''
DM Graphes
-------------------------------
DBEYBIA Mohamed Baha - 21911190
KERIMI Yacine
-------------------------------
'''
from math import sqrt
from parse_tsp import *
import os
import parse_tsp


##################################################
### Calcul cout
##################################################
def cout_algorithme(path, cout):
    dist = 0
    for idx in range(len(path)):
        cur = path[idx]
        nxt = path[(idx+1) % len(path)]
        if(cur!=nxt):
            dist += cout[(cur, nxt)]
    return dist
##################################################
### Algorithme H1 glouton
##################################################

def h1(n, nodes, cout, sommets):
    path = [n]
    #print(nodes)
    print(len(sommets))
    toVisit = list(range(1, len(sommets)+1)) # liste des sommets
    toVisit.remove(n) # supprimer element numero n
    while len(toVisit) > 0:
        m = 999999999
        mIdx = -1
        for target in toVisit:
            dist = cout[(target, path[-1])]
            if dist < m:
                m = dist
                mIdx = target
                #print(mIdx)
        toVisit.remove(mIdx)
        path.append(mIdx)
    print (path)
    return path


##################################################
### Algorithme H2 glouton
##################################################

def h2(n, sommets, cout):
    path = n # liste
    path.append(n[0])
    toVisit = list(range(1, len(sommets)+1))
    toVisit.remove(n[0])
    toVisit.remove(n[1])
    while len(toVisit) > 0:
        m = 999999999
        mIdx = -1
        for element in range(0, len(path) - 1):
            for target in toVisit:
                dist = cout[(target, path[element])]
                dist1 = cout[(target, path[element+1])]
                dist2 = cout[(path[element],path[element+1])]
                couts = (dist1 + dist) - dist2
                if(couts>0) and couts<m:
                    m = couts
                    mIdx = target
                    indice = element+1
        path.insert(indice,mIdx)
        toVisit.remove(mIdx)
    return path

##################################################
### Union-find
##################################################

class unionfind:
    def __init__(self, nodes):
        self.parent = {}
        self.rank = {}
        self.elements = nodes
        for i in self.elements:
            self.makeset(i)

    def makeset(self,i):
        self.parent[i]=i
        self.rank[i]=0

    def findset(self,i):
        if self.parent[i]!=i:
            self.parent[i] = self.findset(self.parent[i])
        return self.parent[i]

    def join(self,i,j):
        i = self.findset(i)
        j = self.findset(j)
        if i==j:
            return
        if self.rank[i]>self.rank[j]:
            self.parent[j]=i
        else:
            self.parent[i]=j
            if self.rank[i]==self.rank[j]:
                self.rank[j]+=1


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
    tree = []
    uf = unionfind(sommets)
    arretes_tri = sorted(arretes, key = dic_arretes.get)
    size=0
    for cur in arretes_tri:
        u = cur[0]
        v = cur[1]
        if uf.findset(u)!=uf.findset(v):
            tree.append(cur)
            uf.join(u,v)
            size+=1
            if size==n-1:
                break
    return tree


##################################################
### 2-OPT - a faire
##################################################




##################################################
### execution de l'algorithme
##################################################

def main():
    if len(argv) > 1 and isfile(argv[1]):

            ##################################################
            ### Parsing fichier et récuperation des données
            ### liste sommets, liste arretes, dictionnaire des
            ### couts
            ##################################################

            sommets, arretes, cout = parse_test(argv[1])

            ##################################################
            ### Algorithme glouton H2 (et H1)
            ##################################################

            liste_sommets = [1, 2]
            test_h2 = h2(liste_sommets, sommets, cout)
            #print(test_h2)
            print("Cout H2 :", cout_algorithme(test_h2, cout))

            ##################################################
            ### 2 - Approximation (en utilisant L'ARPM de kruskal)
            ##################################################

            test_2ap = deux_approximation(sommets, arretes, cout)
            print("Cout 2-Approximation :", cout_algorithme(test_2ap, cout))


            ##################################################
            ### 2-OPT
            ##################################################

    else:
            print("Utilisiation : ", os.path.basename(__file__), " <fichier_test.tsp>")

main()
