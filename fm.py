"""
fm.py - manage operation on text file

This module helps programmer to quickly manage text file.
It's possible read, write, append, prepend, find & replace any text to any file.

logF function will log module error in fm_module.log.

To use this module, import this module and create class object in your script:

from fm import Fm
fm = Fm()

then call function inside this module with prefix fm.
For example to call the read function just write:

fm.readF()

The __init__ function of class Fm will import
sys, os, string, commands
so you don't need to import them in your script.
"""

import sys, string, logging, fileinput

class Fm(object):
	"""FileManager Module

	This is the main class for FM module.
	All function defined under this class take required arguments and in some cases
	also param argument but they are not required.
	"""
	def __init__(self):
		import sys, os, string, commands

	def logF(self, error):
		"""logF function
		Function to log module errors into log file
		Still not complete!!
		"""
		logging.basicConfig(filename='fm_module.log',level=logging.ERROR, format='%(asctime)s %(message)s')
		logging.debug('This message should go to the log file')
		logging.info('So should this')
		logging.warning('And this, too')
		logging.error("ERROR:  %s", error)

	def readF(self, data, param=[]):
		"""readF function
		Function to read file.

		Required arguments:
		- data -> file name to open
		Param:
		- 'list' -> retrive file content as a list.
		It's usefull pass the param 'list' if you don't want just print
		the file content, but you want put the file content in a variable
		as a list.
		
		Example:
			fm.ReadF("file.txt", param=['list'])
		"""
		try:
			with open(data, 'r') as f:
				length = len(param)
				if((length > 0) and (param[0] == 'list')):
					#self.line = f.readlines()
					self.line = list(f)					
					return self.line
				else:
					self.text = f.read()
					return self.text
			f.close()
		except IOError:
			self.logF(sys.exc_info()[1])

	def writeF(self, data, mode, text):
		"""writeF function
		Function to write file.

		Required arguments:
		- data -> file name to write
		- mode -> 'w' or 'a'
		- text -> text to write(w) or append(a)
		"""
		try:
			with open(data, mode) as f:
				f.write(text)
			f.close()
		except IOError:
			self.logF(sys.exc_info()[1])

	def prependF(self, data, text):
		"""prependF function
		Function to prepend (write in the head of file, opposite of append) text to a file.

		Required arguments:
		- data -> file name to write
		- text -> text to prepend

		Example:
			fm.prependF("file.txt", "This text will be prepend to file")
		"""
		try:
			with open(data, 'r') as f_old:
				text_old = f_old.read()
				try:
					with open(data, 'w') as f:
						f.write(text + "\n" + text_old)
					f.close()
				except IOError:
					self.logF(sys.exc_info()[1])
			f_old.close()
		except IOError:
			self.logF(sys.exc_info()[1])

	def substrF(self, data, dic):
		"""substrF function
		Function to find and replace text in file.

		Required arguments:
		- data -> file name to modify
		- dic -> string to find and replacer string.

		You nned to pass dic as python dictionary and you can replace as many string as you want.

		Example:
			dic = {'-':'*', 'old_text':'new_text'}
			fm.substrF("file.txt", dic)

		In file.txt every occurence of '-' will be substitute with '*'
		and every occurence of 'old_text will be substitute with 'new_text'
		"""
		text = self.readF(data)

		for i, j in dic.iteritems():
			text = text.replace(i, j)
		self.writeF(data, "w", text)			




