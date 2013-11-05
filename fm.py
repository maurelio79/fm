"""
fm.py - manage operation on text file
"""
#import sys, os, string, commands
import sys, string, logging

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
		logging.basicConfig(filename='nagios.log',level=logging.ERROR, format='%(asctime)s %(message)s')
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
			#print "Error ", sys.exc_info()
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
			#print "Error ", sys.exc_info()
			self.logF(sys.exc_info()[1])

	def prependF(self, data, text):
		"""prependF function
		Function to prepend (write in the head of file, opposite of append) text to a file.

		Required arguments:
		- data -> file name to write
		- text -> text to prepend
		"""
		try:
			with open(data, 'r') as f_old:
				text_old = f_old.read()
				try:
					with open(data, 'w') as f:
						f.write(text + "\n" + text_old)
					f.close()
				except IOError:
					#print "Error ", sys.exc_info()
					self.logF(sys.exc_info()[1])
			f_old.close()
		except IOError:
			#print "Error ", sys.exc_info()
			self.logF(sys.exc_info()[1])

