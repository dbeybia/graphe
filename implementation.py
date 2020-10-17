'''
DM Graphes
-------------------------------
DBEYBIA Mohamed Baha - 21911190
KERIMI Yacine
-------------------------------
'''
#from union_find import *
from math import sqrt
from parse_tsp import *
import os
import parse_tsp


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


'''
class UnionFind:
	def __init__(self):
		self.dic_ensembles = dict()
		self.num_ensembles = 0

	def unionUF(self,i,j):
		self.num_ensembles -= 1

		self.dic_ensembles[self.findUF(i)] = self.dic_ensembles[j]


	def findUF(self,i):
        #print(i)
		if self.dic_ensembles[i] == i:
			return i
		return self.findUF(self.dic_ensembles[i])

	def creerEnsembles(self,elements):
		for i in elements:
			self.dic_ensembles[i] = i
		self.num_ensembles = len(elements)

'''


def deux_approximation(sommets,arretes, dic_arretes):
     n=len(sommets)
     tree = arpm(list(range(len(sommets))), arretes, dic_arretes)
     #print(tree)
     adj = {}
     # liste adjacence
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
     print (tour, tour[0])
     print (n)
     print ('Cout: ', sum([dic_arretes[(tour[i],tour[(i+1)%n])] for i in range(len(tour))]))



     '''
     for i in range(0,n):
         print ('hello')
         print(n    )
         print(dic_arretes[(tour[i],tour[(i+1)%n])])
         '''
     #print ('Cost: ', sum([dic_arretes[(tour[i],tour[(i+1)%n])] for i in range(n)]))

     return tour


#
def arpm(sommets, arretes, dic_arretes):
    return kruskal(sommets, arretes, dic_arretes)


def kruskal(sommets, arretes, dic_arretes):
    n = len(sommets)+1
    tree = []
    uf = unionfind(sommets)
    #uf.creerEnsembles(sommets)

    arretes_tri = sorted(dic_arretes, key = dic_arretes.get)
    #arretes_tri = sorted(arretes, key = dic_arretes.get)

   # for x in dic_arretes:
    #    if(int(dic_arretes[x]) == 0):
     #       print(x)

    #print(arretes_tri)
    #arretes_tri = sorted(arretes, key = lambda x : x[2]1

    #print('sort ok')
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



'''
def kruskal(sommets, arretes, dic_arretes):
    #print(arretes)
    #print(dic_arretes)
    ensembles = UnionFind()
    ensembles.creerEnsembles(sommets)

    #arretes_tri = sorted(arretes, key = dic_arretes.get)
    #arretes_tri = sorted(arretes, key = lambda x : x[2]1

    print('sort ok')
    mst = list()
    while ensembles.num_ensembles > 1:
        a = arretes.pop(0)
        if not ensembles.findUF(a[0]) == ensembles.findUF(a[1]):
            #print("avant union", ensembles.findUF(a[0]), ensembles.findUF(a[1]), ensemble.nSets)
            ensembles.unionUF(a[0], a[1])
            #print("après union", ensembles.findUF(a[0]), ensembles.findUF(a[1]), ensembles.nSets)
            mst.append(a)
    print("---------------------------")
    print("ARPM")
    #print(x)
    return mst
'''
##################################################
### execution de l'algorithme
##################################################


def main():
    if len(argv) > 1 and isfile(argv[1]):
            sommets_indices, arretes, sommets, dic_arretes = parse_test(argv[1])
            mst_kruskal = arpm(list(range(len(sommets_indices))), arretes, dic_arretes)
            #print(sommets)
            #print(mst_kruskal)
            #print('test')
            #print(dic_arretes)
            deux_approximation(sommets_indices, arretes, dic_arretes)
            #print(dic_arretes)
            #print(r)
    else:
            print("Utilisiation : ", os.path.basename(__file__), " <fichier_test.tsp>")

main()
