#Mitchel Kovacs
#Practice questions from "Cracking the Coding Interview"
#Chapter 1 - Arrays and Strings

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

					break
		#if it is a permutation both strings have had all characters removed and should have length of 0			
		if string1 == string2:
			return True
		else:
			return False

#1.3 replace all spaces in a string with '%20'
def URLify(string):
	return string.replace(' ', "%20")

#1.4 check if a string is a permutation of a palindrome
def palindromePermutaion(string):
	string = string.replace(" ", "")
	string = string.lower()
	isOdd = len(string) % 2
	i = 0
	while i < len(string): 
		n = i + 1
		while n < len(string):
			if string[i] == string[n]:
				#same characters so remove them both and keep looking
				string = string.replace(string[i], "",2)
				i = i - 1
				break
			n = n + 1
		i = i + 1
	#not sure if its needed to check if odd but in my mind it makes sense	
	if isOdd == 1:
		if len(string) == 1:
			return True
		else:
			return False
	else:
		if len(string) == 0:
			return True
		else:
			return False

#1.5 check if 2 strings are one character away from being the same
def oneAway(string1, string2):
	differences = 0
	if(len(string1) >= len(string2)):
		if len(string1) - len(string2) == 0:
			for i in range(len(string1)):
				if string1[i] != string2[i]:
					differences = differences + 1
			if differences == 1:
				return True
			else:
				return False
		elif len(string1) - len(string2) == 1:
			for i in range(len(string2)):
				if string1[i] != string2[i]:
					string1 = string1.replace(string1[i], '', 1)
					differences = differences + 1
			if differences == 1 or differences == 0:
				return True
			else:
				return False

		else:
			return False
	else:
		if len(string2) - len(string1) == 0:
			for i in range(len(string2)):
				if string1[i] != string2[i]:
					differences = differences + 1
			if differences == 1:
				return True
			else:
				return False
		elif len(string2) - len(string1) == 1:
			for i in range(len(string1)):
				if string1[i] != string2[i]:
					string2 = string2.replace(string2[i], '', 1)
					differences = differences + 1
			if differences == 1 or differences == 0:
				return True
			else:
				return False
		else:
			return False
	
#1.6 String compression using the counts of repeated characters
def stringCompression(string):
	compressed = ""
	for i in range(len(string)):
		if i >= len(string):
			break
		n = i
		count = 0
		while n < len(string) and string[n] == string[i]:
			count = count + 1
			n = n + 1
		compressed = compressed + string[i] + str(count)
		string = string.replace(string[i],'', count-1)
	return compressed

#CHAPTER 1 TESTING - chose to take input so others could test
SELECT = input("Choose a function for testing: \n" + "1. isUnique\n"
	 + "2. checkPermutation\n"
	 + "3. URLify\n"
 	 + "4. palindromePermutation\n"
 	 + "5. oneAway\n"
 	 + "6. stringCompression\n"
	 + "\n")


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

#1.3
elif SELECT == '3':

	t1 = input("\nTesting for URLify. \nEnter a string: ")
	
	print("\n" + URLify(t1)+ "\n")

#1.4
elif SELECT == '4':

	t1 = input("\nTesting for palindromePermutaion. \nEnter a string: ")

	if palindromePermutaion(t1):
		print("\nis a permutation of a palindrome\n")
	else:
		print("\nis not a permutation of a palindrome\n")

#1.5
elif SELECT == '5':

	t1, t2= input("\nTesting for oneAway. \nEnter two strings: ").split()
	
	if oneAway(t1, t2):
		print("\nis one away\n")
	else:
		print("\nis not one away\n")

#1.6
elif SELECT == '6':

	t1 = input("\nTesting for stringCompression. \nEnter a string: ")
	
	print("\n" + stringCompression(t1)+ "\n")