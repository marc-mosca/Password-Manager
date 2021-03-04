#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021

import sqlite3
import os

FILE = os.path.abspath(os.getcwd() + "/schema.sqlite3")

class Database:
	"""
	Used to connect, write to and read from a local sqlite3 database and create tables if not exists.
	"""
	def __init__(self):
		"""
		Try to connect to file and create cursor.
		"""
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
