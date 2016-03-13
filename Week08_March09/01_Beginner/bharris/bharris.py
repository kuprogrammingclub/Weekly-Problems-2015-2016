"""
	Blaine Harris
	Week 8 Beginner - Atbash Cipher
	03/09/16
"""


import string

#create a strings of the alphabet in ascending and descending order
alpha = string.ascii_lowercase
cipher = string.ascii_lowercase[::-1]

#save testcases into an array to be ciphered
testcases = [
			'foobar',
			'wizard',
			'/r/dailyprogrammer',
			'gsrh rh zm vcznkov lu gsv zgyzhs xrksvi'
]

#formatting
print
print

#print testcases
for i in testcases:
	print i

#formatting
print ""
print "-----------------------------------------------------"
print ""

#loop through each testcase
for i in testcases:

	#variables to save the word to be ciphered and the ciphered word itself
	cipherString = ""
	testWord = i

	#create a dictionary to save the alpha letter as the key and the atbash index value
	dictionary = {}

	#populate the atbash dictionary
	for i in alpha:
		dictionary[i] = cipher.index(i)

	#loop through the testword indeces and append the atbash letter to cipherString
	for i in testWord:
		if(i in dictionary):
			cipherString += alpha[dictionary[i]]
		else:
			cipherString += i

	#print the cipher
	print cipherString

print
print
