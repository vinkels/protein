import numpy

class amino_acid(object):
	type = 'amino_acid'

	def __init__(self, chain_loc, ac_type, coordinates, bonds):
		self.chain_loc = chain_loc
		self.ac_type = ac_type
		self.coordinates = coordinates
		self.bonds = bonds

	def __str__(self):
		return str(self.chain_loc) + str(self.ac_type) + str(self.coordinates) + str(self.bonds)	
    # def Folder(self)

	def __repr__(self):
		return str(self.chain_loc) + str(self.ac_type) + str(self.coordinates) + str(self.bonds)
        

class grid (object):

	def __init__(self, size):
		self.size = size
		self.grid = numpy.zeros((size, size), dtype = str)

