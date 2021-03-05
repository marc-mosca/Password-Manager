#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021

import sqlite3
import os
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
			"""CREATE TABLE IF NOT EXISTS Accounts (id_user INTEGER UNIQUE, name TEXT, email TEXT, password TEXT, app_name TEXT, url TEXT, FOREIGN KEY("id_user") REFERENCES Users("id"));"""
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
			return self.system.exit_program(f"{user_email} has been registered !")
		except (Exception, sqlite3.Error) as error:
			print(error)
