#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021

import pyperclip
from hashlib import sha256
from database import Database
from system import System

KEY = ",m9P?@!Y{w?03Afdq<@>AhG5]-d"

class PasswordManager:
	def __init__(self, id_user: int=0):
		"""
		Init method.
		"""
		self.database = Database()
		self.system = System()
		self.id_user = id_user
		self.alert = ""

	def menu(self):
		"""
		This method print a menu and checks the data entered by the user.
		"""
		self.system.clear_terminal()
		if self.alert != "":
			print(f"{self.alert}\n")
		print(("-" * 19) + " Menu " + ("-" * 19))
		print("1. Create a new password")
		print("2. Search for all sites you have registered")
		print("3. Find a password for a site or application")
		print("Q. Quit")
		print("-" * 44)
		self.choice = input(": ").lower()
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
		This method is a form to create a new password for an application or site.
		"""
		app_name = input("Please enter the application name : ").capitalize()
		identifier = input("Please enter the identifier : ")
		password = input("Please enter the password : ")
		url = input("Please enter the url : ").lower()
		while app_name == "" or identifier == "" or password == "" or url == "":
			print("\nPlease complete all fields !")
			app_name = input("Please enter the application name : ").capitalize()
			identifier = input("Please enter the identifier : ")
			password = input("Please enter the password : ")
			url = input("Please enter the url : ").lower()
		verify_app_name = self.database.research_app_name(self.id_user, app_name)
		if verify_app_name != []:
			self.alert = f"{app_name} is already registered !"
			self.menu()
		password_hashed = self.hash(password)
		pyperclip.copy(password_hashed)
		pyperclip.paste()
		self.database.insert_new_password(self.id_user, app_name, identifier, password_hashed, url)
		self.alert = f"The password for the site or the application {app_name} has been saved !"
		self.menu()

	def search_all_sites_registered(self):
		"""
		This method displays all accounts of the logged in user.
		"""
		data = ("App Name: ", "Identifier: ", "Password: ", "Url: ")
		result = self.database.search_all_sites(self.id_user)
		if result == []:
			self.alert = "You have not registered an account !"
			self.menu()
		print("\nResult:\n")
		for row in result:
			[print(str(data[i]) + str(row[i])) for i in range(len(row))]
			print("")
		print("-" * 30)

	def find_password(self):
		"""
		This method saves the password of the application that the user to request.
		"""
		app_name = input("Please enter the name of application/site : ").capitalize()
		result = self.database.find_password_to_application(self.id_user, app_name)
		if result == []:
			self.alert = f"{app_name} has not been registered !"
			self.menu()
		pyperclip.copy(result[0][0])
		pyperclip.paste()
		self.alert = f"The password for {app_name} has been copied to the clipboard !"
		self.menu()

	def hash(self, password: str):
		"""
		This method encrypts the password passed as a parameter.
		"""
		return sha256((password + KEY + password).encode("utf-8")).hexdigest()
