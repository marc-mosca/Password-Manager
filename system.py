#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# Created by MOSCA Marc on March 04 2021
# License: CC BY-NC-ND 4.0

import os
import platform

class System:
	def __init__(self):
		"""
		Init method.
		"""
		self.operating_system = platform.system()

	def clear_terminal(self):
		"""
		This method determine operating system and clear terminal.
		"""
		if self.operating_system.lower() == 'linux' or self.operating_system.lower() == 'darwin':
			os.system("clear")
		else:
			os.system("cls")

	def exit_program(self, message: str):
		"""
		This method exit program with message.
		"""
		print(f"\n{message}")
		exit()
