#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021
# License: CC BY-NC-ND 4.0

from database import Database
from password_manager import PasswordManager
from system import System

class Auth:
	def __init__(self):
		"""
		Init method.
		"""
		self.database = Database()
		self.system = System()
		self.password_manager = PasswordManager()
		self.alert = ""

	def menu(self):
		"""
		This method print a menu and checks the data entered by the user.
		"""
		self.system.clear_terminal()
		if self.alert != "":
			print(f"{self.alert}\n")
		print(("-" * 4) + " Connection " + ("-" * 4))
		print("1. Connect")
		print("2. Register")
		print("Q. Quit")
		print("-" * 20)
		self.choice = input(": ").lower()
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
		This method checks if the user informations is correct for the connection.
		"""
		user_email = input("\nPlease enter your email adress : ")
		user_password = input("Please enter your password : ")
		user_informations = self.database.research_user_by_email(user_email)
		if user_informations == []:
			self.system.exit_program(f"{user_email} is not registered !")
		user_password_hashed = self.password_manager.hash(user_password)
		if user_informations[0][3] != user_password_hashed:
			self.system.exit_program("Wrong password !")
		self.password_manager = PasswordManager(user_informations[0][0])
		return self.password_manager.menu() 
	
	def register(self):
		"""
		This method checks if the user informations is correct for the inserted in the database.
		"""
		username = input("Please enter your username : ").capitalize()
		user_email = input("Please enter your email adress : ").lower()
		user_password = input("Please enter your password : ")
		user_password_hashed = self.password_manager.hash(user_password)
		user_informations = self.database.research_user_by_email(user_email)
		if user_informations != []:
			self.system.exit_program(f"{user_email} is already used !")
		self.database.adding_user_to_database(username, user_email, user_password_hashed)
		self.alert = f"{user_email} has been registered !"
		self.menu()
