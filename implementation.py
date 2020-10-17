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
### Calcul distance entre deux noeuds pour H1 et H2

##################################################

def distanceEntre(f, t):
    return ((f['x'] - t['x'])**2 + (f['y'] - t['y'])**2)**0.5



##################################################
### Algorithme H1 glouton
##################################################

def h1(n, nodes):
    path = [n]
    print(nodes)
    toVisit = list(nodes.keys()) # liste des sommets
    toVisit.remove(n) # supprimer element numero n
    while len(toVisit) > 0:
        m = 999999999
        mIdx = -1
        for target in toVisit:
            print(nodes[target])
            print(target)
            dist = distanceEntre(nodes[target], nodes[path[-1]])
            if dist < m:
                m = dist
                mIdx = target
                print(mIdx)
        toVisit.remove(mIdx)
        path.append(mIdx)
        print(path)
    return path

##################################################
### Algorithme H2 glouton
##################################################

def h2(n, nodes):
    path = n # liste
    path.append(n[0])
    #print(path)
    toVisit = list(nodes.keys()) #
    #print(toVisit)
    toVisit.remove(n[0])
    toVisit.remove(n[1])
    while len(toVisit) > 0:
        m = 999999999
        mIdx = -1
        for element in range(0, len(path) - 1):
            for target in toVisit:
                dist = distanceEntre(nodes[target], nodes[path[element]])
                dist1 = distanceEntre(nodes[target], nodes[path[element+1]])
                dist2 = distanceEntre(nodes[path[element]], nodes[path[element+1]])

                cout = (dist1 + dist) - dist2
                #print(cout)
                if(cout>0) and cout<m:
                    m = cout
                    mIdx = target
                    indice = element+1
        path.insert(indice,mIdx)
        #toVisit.remove(mIdx)
        #path.append(mIdx)
        toVisit.remove(mIdx)
    #print (path)
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

     print ('\n Tour optimale pour deux approximation :')
     print (tour)
     print (n)
     print ('Cout: ', sum([dic_arretes[(tour[i],tour[(i+1)%n])] for i in range(len(tour))]))

     return tour



##################################################
### Kruskal avec union-find
##################################################
def kruskal(sommets, arretes, dic_arretes):
    n = len(sommets)
    tree = []
    uf = unionfind(sommets)
    #uf.creerEnsembles(sommets)

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
    print("---------------------------")
    print("ARPM")
    #print(tree)

    return tree




##################################################
### execution de l'algorithme
##################################################


def main():
    if len(argv) > 1 and isfile(argv[1]):
            sommets, arretes, cout = parse_test(argv[1])
            #mst_kruskal = kruskal(sommets, arretes, cout)
            #print(mst_kruskal)
            #h2
            #print(dic_arretes)
            deux_approximation(sommets, arretes, cout)
            #print(sommets_indices)
            #print(dic_arretes)
            #print(r)
    else:
            print("Utilisiation : ", os.path.basename(__file__), " <fichier_test.tsp>")

main()
