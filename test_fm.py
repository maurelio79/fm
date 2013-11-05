#!/usr/bin/env python

from fm import *

# instantiate class
fm = Fm()

# write head for trash file
scart_text = "# Server not imported for parameters error."
fm.writeF("trash.txt", "a", scart_text)

# get content from list.txt file in list format
line = fm.readF("list.txt",  param=['list'])

# cycle to create record split with , and get record number
for j, i in enumerate(line):
	i.rstrip("\n")
	line_split = i.split(",")	
	line_number = j
	
	#print line_split
	#print line_number

# set variables for each item of each list
	host = line_split[0]
	alias = line_split[1]
	ip = line_split[2]
	environment = line_split[3]

# check record with missing parameters and put them in trash file
	if ((host == '') or (alias == '') or (ip == '')):
		scart_text = """
ERROR at line %d record %s for hostname %s: missing some parameters""" % (line_number, line_split, host)
		fm.writeF("trash.txt", "a", scart_text)

# create the configuration file for each host (record[0])
	else:
		text = """
define host{
		host_name			%s
		alias				%s
		address				%s
		environment			%s
		}

# SECTION SERVICES

define service{
		service_description			connection secure shell
		display_name				SSH
		check_command				check-ssh
		}
		""" % (host, alias, ip, environment)

# write down the file
		fm.writeF(host + ".cfg", "w", text)


