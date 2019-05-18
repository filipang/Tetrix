import pygame
import block
import piece_constructor
import forms

import time

debug = open("debug.txt","w")

class Robot:
	def __init__(self,foreground,board,currentForm,generator):
		self.foreground = foreground
		self.board = board
		self.currentForm = currentForm
		self.generator = generator

	def update(self,board,currentForm,generator):
		self.board = board
		self.currentForm = currentForm
		self.generator = generator
		self.queue = []
		self.moveQueue = []
		self.bestscore = 0

	def movePiece(self,sign):
		#DOWN arrow down
		if sign == "DOWN":
			self.currentForm.moveWith(0,1)
			return

		#RIGHT arrow right
		if sign == "RIGHT":
			self.currentForm.moveWith(1,0)
			return

		#LEFT arrow left
		if sign == "LEFT":
			self.currentForm.moveWith(-1,0)
			return

		#ROTATE arrow up
		if sign == "ROTATE":
			self.currentForm.rotate()
			return

	def islocked(self):
		if self.currentForm.moveWith(0,1,True,False):
			self.currentForm.moveWith(0,-1,True,False)
			return False
		return True	

	def evaluate(self):
		ymax=0
		for b in self.currentForm.blocks:
			if b.coords[1]>ymax:
				ymax=b.coords[1]

		return ymax	


	def backtracking(self,canLeft,canRight,goesDown):
		
		if self.islocked():
			evaluare = self.evaluate()
			if evaluare>self.bestscore:
				self.bestscore = evaluare
				while len(self.queue):
					self.queue.pop()
				for move in self.moveQueue:
					self.queue.append(move)
		else:
			if canLeft and not(goesDown):
				if self.currentForm.moveWith(-1,0,True,False):
					self.moveQueue.append("LEFT")

					self.backtracking(canLeft,False,goesDown)

					self.moveQueue.pop()
					self.currentForm.moveWith(1,0,True,False)

			if canRight and not(goesDown):
				if self.currentForm.moveWith(1,0,True,False):
					self.moveQueue.append("RIGHT")

					self.backtracking(False,canRight,goesDown)

					self.moveQueue.pop()
					self.currentForm.moveWith(-1,0,True,False)

			self.currentForm.moveWith(0,1,True,False)
			self.moveQueue.append("DOWN")

			self.backtracking(canLeft,canRight,True)

			self.moveQueue.pop()
			self.currentForm.moveWith(0,-1,True,False)

	def play(self):
		self.moveQueue = []

		self.queue = []
		self.bestscore = 0

		self.backtracking(True,True,False)

		self.moveQueue.append("ROTATE")
		self.currentForm.rotate(0,0,False)

		self.backtracking(True,True,False)

		self.moveQueue.append("ROTATE")
		self.currentForm.rotate(0,0,False)

		self.backtracking(True,True,False)

		self.moveQueue.append("ROTATE")
		self.currentForm.rotate(0,0,False)

		self.backtracking(True,True,False)

		self.currentForm.rotate(0,0,False)

		print(str(self.bestscore))

		for move in self.queue:
			print(move)
			self.movePiece(move)

		#time.sleep(5)