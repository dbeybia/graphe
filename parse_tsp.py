from math import sqrt
from sys import argv
from os.path import isfile

def dist_euc(x1, y1, x2, y2):
	return( sqrt( (x1-x2)**2 + (y1 - y2)**2))



def parse_test(fichier):
    f = open(fichier, 'r') # passer fichier en parametre

    lines = f.read().splitlines()
    sommets = list()

    #print(lines)
    for line in lines:
        if line and line.lstrip()[0].isdigit(): # vrai, si ya que des chiffres dans la ligne
            #print (line.lstrip().split())
            sommets.append([int(i) for i in line.split()])

    print (sommets)

    dic_arretes = dict()
    arretes = list() # début, fin, poids
    print('------ nb sommets ---------')
    print(len(sommets))
    print('------ nb sommets ---------')

    # arretes
    for i in range(1, len(sommets)):
        for j in range(i):
            if i != j:
                dic_arretes[dist_euc(sommets[i][1], sommets[i][2], sommets[j][1], sommets[j][2])] = (i, j)
                arretes.append([i, j, dist_euc(sommets[i][1], sommets[i][2], sommets[j][1], sommets[j][2])])


    sommets_indices = list(range(len(sommets)))
    #print(len(sommets_indices), len(sommets))
    print('------ nb arretes ---------')
    print(len(arretes))
    print('------ nb arretes ---------')
    return sommets_indices, arretes, sommets



def parse_h2(filename):
    nodes = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda x:x.strip(), lines))
        # check structure fichier changer selon fichier
        s = lines.index("NODE_COORD_SECTION")
        e = lines.index("EOF")
        parsed = lines[s+1: e]

        parsed = list(map(lambda x: tuple(map(lambda y: float(y), x.split())), parsed))

    for node in parsed:
        nodes[int(node[0])] = {
            "id": int(node[0]),
            "x": node[1],
            "y": node[2]
        }

    return nodes
