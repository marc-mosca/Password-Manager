#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021

from system import System

class PasswordManager:
	def __init__(self):
		"""
		Init method.
		"""
		self.system = System()
		self.system.clear_terminal()
		print(("-" * 25) + " Menu " + ("-" * 25))
		print("1. Create a new password")
		print("2. Search for all sites you have registered")
		print("3. Find a password for a site or application")
		print("Q. Quit")
		print("-" * 56)
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
			self.create_new_password()
		elif self.choice == "2":
			self.search_all_sites_registered()
		elif self.choice == "3":
			self.find_password()
		else:
			self.system.exit_program("You leave the program.")

	def create_new_password(self):
		"""
		"""
		pass

	def search_all_sites_registered(self):
		"""
		"""
		pass

	def find_password(self):
		"""
		"""
		pass	
