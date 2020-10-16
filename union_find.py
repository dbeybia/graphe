class UnionFind:
	def __init__(self):
		self.dic_ensembles = dict()
		self.num_ensembles = 0

	def unionUF(self,i,j):
		self.num_ensembles -= 1

		self.dic_ensembles[self.findUF(i)] = self.dic_ensembles[j]


	def findUF(self,i):
		if self.dic_ensembles[i] == i:
			return i
		return self.findUF(self.dic_ensembles[i])

	def creerEnsembles(self,elements):
		for i in elements:
			self.dic_ensembles[i] = i
		self.num_ensembles = len(elements)
