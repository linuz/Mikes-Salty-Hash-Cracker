#!/usr/bin/python
#############################################################
# Mikes Salty Hash Cracker v1.0 		            #
# Written By: Dennis Linuz <dennismald@gmial.com>	    #
# A script to crack Mike's custom MD5 hash salting          #
# 			***I love salty crackers!***	    #
#############################################################

import hashlib, sys

if (len(sys.argv) <= 1):
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "Please enter the hash via the only argument."
	print ""
	print "USAGE: python MikesSaltyHashCracker <HASH>"
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	quit()
else:
	if (len(sys.argv[1]) != 52):
		print "Incompatable hash! Hash must be 52 characters long."
		quit()
	passwordHash = sys.argv[1]
	hashLength = len(passwordHash)
	passwordSalt1 = passwordHash[0:10]
	passwordSalt2 = passwordHash[hashLength-10:hashLength]
	passwordHash = passwordHash[10:hashLength-10]
	try:
		dictFile = open("dictionary.txt")
	except:
		print "Unable to open password dictionary file (dictionary.txt)"
		quit()
	for line in dictFile:
		line = line.replace("\n","")
		print "Trying: "+line
		hasherMD5 = hashlib.md5()
		hasherMD5.update(line)
		tempHash = hasherMD5.hexdigest()
		hasherMD5 = hashlib.md5()
		hasherMD5.update(passwordSalt2+tempHash)
		tempHash = hasherMD5.hexdigest()
		hasherMD5 = hashlib.md5()
		hasherMD5.update(tempHash+passwordSalt1)
		tempHash = hasherMD5.hexdigest()
		if (tempHash == passwordHash):
			print "Success!"
			print "The Password for hash " + passwordHash + " is: "
			print line
			break



