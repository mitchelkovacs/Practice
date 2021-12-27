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

#1.2 Given two strings, check if one is a permutation of the other
def checkPermutation(string1,string2):
	if len(string1) != len(string2):
		return False
	else:
		for i in string1: 
			for n in string2:
				if i == n:
					#same characters so remove them both and keep looking
					string1 = string1.replace(i, "",1)
					string2 = string2.replace(n, "",1)
					print(string1 + "\n" + string2)
					break
		#if it is a permutation both strings have had all characters removed and should have length of 0			
		if string1 == string2:
			return True
		else:
			return False


#CHAPTER 1 TESTING - chose to take input so others could test
SELECT = input("Choose a function for testing: \n" + "1. isUnique\n" + "2. checkPermutation\n \n")


#1.1
if SELECT == '1':

	t1 = input("\nTesting for isUnique. \nEnter a string: ")

	if isUnique(t1):
		print("\nunique\n")
	else:
		print("\nnot unique\n")

#1.2
elif SELECT == '2':

	t1, t2= input("\nTesting for checkPermutation. \nEnter two strings: ").split()
	
	if checkPermutation(t1, t2):
		print("\nis permutation\n")
	else:
		print("\nis not permutation\n")
