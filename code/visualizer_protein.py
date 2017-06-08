# Visualizer for 2D protein folding

import math

from Tkinter import *

class Visualization:
	def __init__(self, width = 100, height = 100, delay = 0.1):

		self.delay = delay

		self.max_dim = max(width, height)
		self.width = width
		self.height = height

		# Drawing surface
		self.master = Tk()
		self.w = Canvas(self.master, width=500, height=500)
		self.w.pack()
		self.master.update()

		# Background
		x1, y1 = self._map_coors(0, 0)
		x2, y2 = self._map_coors(width, height)
		self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

		# Display
		self.master.mainloop()