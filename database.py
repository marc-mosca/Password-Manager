#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021

import os
import sqlite3
from system import System

FILE = os.path.abspath(os.getcwd() + "/schema.sqlite3")

class Database:
	"""
	Used to connect, write to and read from a local sqlite3 database and create tables if not exists.
	"""
	def __init__(self):
		"""
		Try to connect to file and create cursor.
		"""
		self.system = System()
		self.connection = None
		try:
			self.connection = sqlite3.connect(FILE)
		except (Exception, sqlite3.Error) as error:
			print(error)
		self.cursor = self.connection.cursor()
		queries = [
			"""CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT UNIQUE, password TEXT);""",
			"""CREATE TABLE IF NOT EXISTS Accounts (id_user INTEGER, app_name TEXT, identifier TEXT, password TEXT, url TEXT, FOREIGN KEY("id_user") REFERENCES "Users"("id"));"""
		]
		[self.cursor.execute(queries[i]) for i in range(len(queries))]
		self.connection.commit()

	def research_user_by_email(self, user_email: str):
		"""
		This method allows you to search for a user with their email adress.
		"""
		try:
			query = f"""SELECT * FROM Users WHERE email = "{user_email}";"""
			self.cursor.execute(query)
			self.connection.commit()
			return self.cursor.fetchall()
		except (Exception, sqlite3.Error) as error:
			print(error)

	def adding_user_to_database(self, username: str, user_email: str, user_password: str):
		"""
		This method adds the user to the database.
		"""
		try:
			query = f"""INSERT INTO Users (name, email, password) VALUES ("{username}", "{user_email}", "{user_password}");"""
			self.cursor.execute(query)
			self.connection.commit()
		except (Exception, sqlite3.Error) as error:
			print(error)

	def insert_new_password(self, id_user: int, app_name: str, identifier: str, password: str, url: str):
		"""
		This method adds the new password to the database.
		"""
		try:
			query = f"""INSERT INTO Accounts VALUES ("{id_user}", "{app_name}", "{identifier}", "{password}", "{url}");"""
			self.cursor.execute(query)
			self.connection.commit()
		except (Exception, sqlite3.Error) as error:
			print(error)

	def search_all_sites(self, id_user: int):
		"""
		This method retrieves all accounts saved by the logged in user.
		"""
		try:
			query = f"""SELECT app_name, identifier, password, url FROM Accounts WHERE id_user = "{id_user}";"""
			self.cursor.execute(query)
			self.connection.commit()
			return self.cursor.fetchall()
		except (Exception, sqlite3.Error) as error:
			print(error)

	def find_password_to_application(self, id_user: int, app_name: str):
		"""
		This method .
		"""
		try:
			query = f"""SELECT password FROM Accounts WHERE (id_user = "{id_user}" and app_name = "{app_name}");"""
			self.cursor.execute(query)
			self.connection.commit()
			return self.cursor.fetchall()
		except (Exception, sqlite3.Error) as error:
			print(error)
