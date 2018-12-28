"""
Author: KHP
"""


import random

class RandRegion:
	def __init__(self, max_width, max_height):
		self.x1 = random.randrange(max_width - 5)
		self.y1 = random.randrange(max_height - 30)
		
		self.width = random.randrange(2, min((max_width - 5 - self.x1 + 2), 101))
		self.height = random.randrange(2, min((max_height - 30 - self.y1 + 2), 81))
		
		self.x2 = self.x1 + self.width
		self.y2 = self.y1 + self.height

	def get_coord(self):
		x1, y1 = self.x1, self.y1
		return x1, y1, self.width, self.height
		

	def __repr__(self):
		return "x1, y1: ({0}, {1})\nx2, y2: ({2}, {3})\nx2 - x1 = {4}\ny2 - y1 = {5}".format(self.x1, self.y1, self.x2, self.y2, self.width, self.height)
	
	def __str__(self):
		return "Top Left Corner is ({0}, {1})\nBottom Right Corner is ({2}, {3})\nWidth is {4}\nHeight is {5}".format(self.x1, self.y1, self.x2, self.y2, self.width, self.height)