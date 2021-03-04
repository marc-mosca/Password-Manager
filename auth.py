#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021

from hashlib import sha256
from database import Database
from system import System

KEY = ",m9P?@!Y{w?03Afdq<@>AhG5]-d"

class Auth:
	def __init__(self):
		"""
		Init method.
		"""
		self.database = Database()
		self.system = System()
		print("\n")
		print(("-" * 4) + " Connection " + ("-" * 4))
		print("1. Connect")
		print("2. Register")
		print("Q. Quit")
		print("-" * 20)
		self.choice = input(": ").lower()
		self.check()

	def check(self):
		"""
		This method checks the data entered by the user.
		"""
		while self.choice != "q" and self.choice != "1" and self.choice != "2":
			print("Sorry, I don't understand !")
			self.choice = input(": ").lower()
		if self.choice == "1":
			self.connection()
		elif self.choice == "2":
			self.register()
		else:
			self.system.exit_program("You leave the program.")

	def connection(self):
		"""
		Retrieves the data entered by the user to insert them into database.
		"""
		user_email = input("\nPlease enter your email adress : ")
		user_password = input("Please enter your password : ")
		user_password_hashed = self.hash(user_password)
		user_informations = self.database.research_user_by_email(user_email)
		if user_informations == []:
			self.system.exit_program(f"{user_email} is not registered !")
		if user_informations[0][3] != user_password_hashed:
			self.system.exit_program("Wrong password !")

	# TODO register method
	def register(self):
		"""
		"""
		pass

	def hash(self, password: str):
		"""
		"""
		return sha256((password + KEY + password).encode("utf-8")).hexdigest()
