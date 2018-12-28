"""
Author: KHP
"""

from tkinter import *
from RandRegion import *
from Stack import Stack
from Queue import Queue

class A1:
	def __init__(self, master):
		self.canvas_width = 700
		self.canvas_height = 400
		master.title("Shapes")
		geometry_string = str(self.canvas_width)+"x"+str(self.canvas_height)+"+10+20"
		master.geometry(geometry_string)
		self.a_canvas = Canvas(root)
		self.a_canvas.config(background="SlateBlue1")	
		self.a_canvas.pack(fill=BOTH, expand = True)
		
		self.a_list = []
		self.s = Stack()
		self.q = Queue()
		
		self.rec_num = 0
		self.circ_num = 0
		self.arc_num = 0
		
		add_rec = Button(master, text ="Add Rect", command = self.add_rectangle)
		add_rec.pack(side = LEFT)
		remove_rec = Button(master, text ="Remove Rect", command = self.remove_rectangle)
		remove_rec.pack(side = LEFT)
		add_circ = Button(master, text ="Add Circle", command = self.add_circle)
		add_circ.pack(side = LEFT)
		remove_circ = Button(master, text ="Remove Circle", command = self.remove_circle)
		remove_circ.pack(side = LEFT)
		add_arc = Button(master, text ="Add Arc", command = self.add_arc)
		add_arc.pack(side = LEFT)
		remove_arc = Button(master, text ="Remove Arc", command = self.remove_arc)
		remove_arc.pack(side = LEFT)
		remove_red = Button(master, text ="Remove Red Shapes", command = self.remove_red_shapes)
		remove_red.pack(side = LEFT)
		
	def select_color(self, num):
		self.color_str = ["red", "orange", "yellow", "green", "blue", "purple"]
		return self.color_str[num]

	def add_rectangle(self):	
		r = RandRegion(self.canvas_width, self.canvas_height)
		a_rect = r.get_coord()
		if self.rec_num == 6:
			self.rec_num = 0
		a_color = self.select_color(self.rec_num)
		self.a_rect_shape_color= (self.a_canvas.create_rectangle(a_rect[0], a_rect[1], a_rect[0] + a_rect[2], a_rect[1] + a_rect[3], fill=a_color), a_color)
		self.a_list.append(self.a_rect_shape_color)
		self.rec_num += 1
		
	def remove_rectangle(self):
		if self.rec_num > 0:
			self.rec_num -= 1
		if self.a_list != []:
			i = random.randrange(len(self.a_list))
			random_index = (self.a_list.pop(i))
			self.a_canvas.delete(random_index[0])
		pass
	
	def add_circle(self):	
		r = RandRegion(self.canvas_width, self.canvas_height)
		a_circle = r.get_coord()
		if self.circ_num == 6:
			self.circ_num = 0
		a_color = self.select_color(self.circ_num)
		self.a_circle_shape_color= (self.a_canvas.create_oval(a_circle[0], a_circle[1], a_circle[0] + a_circle[2], a_circle[1] + a_circle[3], fill=a_color), a_color)
		self.s.push(self.a_circle_shape_color)
		self.circ_num += 1
		
	def remove_circle(self):
		if self.circ_num > 0:
			self.circ_num -= 1
		if not self.s.is_empty():
			top = self.s.pop()
			self.a_canvas.delete(top[0])
		pass

	def add_arc(self):	
		r = RandRegion(self.canvas_width, self.canvas_height)
		a_arc = r.get_coord()
		if self.arc_num == 6:
			self.arc_num = 0
		a_color = self.select_color(self.arc_num)
		self.a_arc_shape_color= (self.a_canvas.create_arc(a_arc[0], a_arc[1], a_arc[0] + a_arc[2], a_arc[1] + a_arc[3], start=45, extent=90, fill=a_color), a_color)
		self.q.enqueue(self.a_arc_shape_color)
		self.arc_num += 1
		
	def remove_arc(self):
		if self.arc_num > 0:
			self.arc_num -= 1
		if not self.q.is_empty():
			front = self.q.dequeue()
			self.a_canvas.delete(front[0])
		pass

	def remove_red_shapes(self):
		for object in self.a_list:
			if object[1] == "red":
				self.a_canvas.delete(object[0])
				self.a_list.remove(object)
		for object in self.s.items:
			if object[1] == "red":
				self.a_canvas.delete(object[0])
				self.s.items.remove(object)
		for object in self.q.items:
			if object[1] == "red":
				self.a_canvas.delete(object[0])
				self.q.items.remove(object)
		if self.a_list == [] and self.s.items == [] and self.q.items == []:
			self.rec_num = 0
			self.circ_num = 0
			self.arc_num = 0
			
root = Tk()
my_window = A1(root)
r = RandRegion(my_window.canvas_width, my_window.canvas_height)
root.mainloop()