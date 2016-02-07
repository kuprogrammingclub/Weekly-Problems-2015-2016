#	SLongofono	Week 01 Spring 2016	Intermediate
#
#	Roman Numeral Conversion
#
#	Write a program that takes in a string representing a Roman numeral
#	and returns its value.  For this exercise, the following rules apply:
#
#		Each letter may only be repeated three times, with the exception
#		of M which may be repeated four times.
#		I may only be subtracted from V or X
#		X may only be subtracted from L or C
#		C may only be subtracted from D or M
#		
#	Nonstandard input such as MDIXI was not specified as wrong, so it is passed through.
#	Holy corner cases Batman!


import sys


def getValue(a):

		if(a=='M'):
			return 1000
		elif(a=='D'):
			return 500
		elif(a=='C'):
			return 100
		elif(a=='L'):
			return 50
		elif(a=='X'):
			return 10
		elif(a=='V'):
			return 5
		elif(a=='I'):
			return 1
		elif(a=='CM'):
			return 900
		elif(a=='CD'):
			return 400
		elif(a=='XC'):
			return 90
		elif(a=='XL'):
			return 40
		elif(a=='IX'):
			return 9
		elif(a=='IV'):
			return 4
		else: 
			raise TypeError

#builds a list of parsed values.  Must be called after a check for multiple
#ascending chars is made, since it automatically groups ascending terms together
#and moves on
def normalize(word):
	try:
		result = []
		length = len(word)
		skip = False
		for i in range(length):
			if skip:
				skip = False
			else:
				if(i+1)<length:
					if(getValue(word[i])<getValue(word[i+1])):
						skip = True
						result.append(getValue(str(word[i]+ word[i+1])))
					else:
						result.append(getValue(word[i]))
				else:
					result.append(getValue(word[i]))
		return result
	except Exception as err:
		print str(err)
		#this will get caught downstream by descending
		return [1,2,3,4]				
	

#Expects at least two chars
def isValid(word):

	#Check repeats
	charz = ['I','V','X','L','C','D','M']
	for i in charz:
		if((i+i+i+i) in word):
			if i == 'M':
				if((i+i+i+i+i)in word):
					return False
			else:
				return False
	
	#Check multiple ascending and undefined chars
	length = len(word)
	match = False
	for i in range (length):
		if not word[i] in charz:
			print word[i]  + " is not in " + word
			print 'Invalid characters found'
			return False
		a = getValue(word[i])
		if((i+1)<length):
			b = getValue(word[i+1])	
		
		if a<b:
			if match:
				return False
			else:
				match = True
		else:
			match = False

	return True

def descending(arr):
	for i in range(len(arr)):
		if (i+1) < len(arr):
			if arr[i] < arr[i+1]:
				return False
	return True


if len(sys.argv) < 2:
	print 'Usage: ettubrute [Roman numeral]'
	sys.exit(0)

if len(sys.argv[1]) == 1:
	print getValue(sys.argv[1][0])
	sys.exit(0)

if not isValid(sys.argv[1]):
	print 'The input ' + sys.argv[1] + ' was invalid'
	sys.exit(0)

nums = normalize(sys.argv[1])
if not descending(nums):
	print 'Descending error'
	print 'The input ' + sys.argv[1] + ' was invalid and yielded:'
	print nums
	sys.exit(0)

sum = 0
for i in nums:
	sum += i
print sum
