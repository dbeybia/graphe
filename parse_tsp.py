
import math

from sys import argv
from os.path import isfile

def parse_test(fichier):

	f = open(fichier, 'r') #passer fichier en parametre
	lines = f.read().splitlines()
	sommets = []
	arretes = []
	x = {}
	y={}
	cout = {}
	for line in lines:
		if line and line.lstrip()[0].isdigit(): #vrai, si ya que des chiffres dans la ligne
			k= line.split()
			sommets.append(int(k[0]))
			x[sommets[int(k[0])-1]] = float(k[1])
			y[sommets[int(k[0])-1]] = float(k[2])
	#print(x)
		for i in range(len(sommets)):
			#print(len(sommets))
			for j in range(i+1, len(sommets)):
				arretes.append((sommets[i],sommets[j]))
				arretes.append((sommets[j],sommets[i]))
				cout[sommets[i],sommets[j]]=cout[sommets[j],sommets[i]]=math.sqrt((x[sommets[i]]-x[sommets[j]])**2 + (y[sommets[i]]-y[sommets[j]])**2)

	return sommets, arretes, cout
