#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021

from system import System

class Graphic:
	def __init__(self):
		"""
		Init method.
		"""
		self.system = System()
		print("\n")
		print(("-" * 9) + " Menu " + ("-" * 9))
		print("1. Create a new password")
		print("2. Research all website who used your email adress")
		print("3. Research password for a website or application")
		print("Q. Quit")
		print("-" * 30)
		self.choice = input(": ").lower()
		self.check()

	def check(self):
		"""
		This method checks the data entered by the user.
		"""
		while self.choice != "q" and self.choice != "1" and self.choice != "2" and self.choice != "3":
			print("Sorry, I don't understand !")
			self.choice = input(": ").lower()
		if self.choice == "1":
			print("1")
		elif self.choice == "2":
			print("2")
		elif self.choice == "3":
			print("3")
		else:
			self.system.exit_program("You leave the program.")	
