#Mitchel Kovacs
#Practice questions from "Cracking the Coding Interview"

#1.1 Determine if a String has all unique characters without additional data structures
def isUnique(string):
	for i in range(len(string)):
		n = i + 1
		while n < len(string):
			if string[i] == string[n]:
				return False
			n = n+1
	return True		

#CHAPTER 1 TESTING
SELECT = input("Choose a function for testing: \n" + "1. isUnique\n \n")

#1.1
if SELECT == '1':

	t1 = input("\nTesting for isUnique. \nEnter a string: ")

	if isUnique(t1):
		print("\nunique\n")
	else:
		print("\nnot unique\n")
