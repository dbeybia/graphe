'''
DM Graphes
-------------------------------
DBEYBIA Mohamed Baha - 21911190
KERIMI Yacine
-------------------------------
'''
from union_find import *
from math import sqrt
from parse_tsp import *
import os
import parse_tsp



def kruskall(sommets, arretes):
    #print(arretes)
    ensembles = UnionFind()
    ensembles.creerEnsembles(sommets)
    arretes = sorted(arretes, key = lambda x : x[2])

    mst = list()
    while ensembles.num_ensembles > 1:
        a = arretes.pop(0)
        if not ensembles.findUF(a[0]) == ensembles.findUF(a[1]):
            #print("avant union", ensembles.findUF(a[0]), ensembles.findUF(a[1]), ensemble.nSets)
            ensembles.unionUF(a[0], a[1])
            #print("après union", ensembles.findUF(a[0]), ensembles.findUF(a[1]), ensembles.nSets)
            mst.append(a)
    return mst


'''
def fastDistance(node1, node2): # distance without the sqrt, for fast comparisons
    print(node1)
    print(node2)
    return (node2[2] - node1[2])**2 + (node2[1] - node1[1])**2
'''
##################################################
### execution de l'algorithme
##################################################


def main():
    if len(argv) > 1 and isfile(argv[1]):
            sommets_indices, arretes, sommets = parse_test(argv[1])
            mst_kruskall = kruskall(list(range(len(sommets_indices))), arretes)
            print("test")
            print(mst_kruskall)
            #print(r)
    else:
            print("Utilisiation : ", os.path.basename(__file__), " <fichier_test.tsp>")

main()
