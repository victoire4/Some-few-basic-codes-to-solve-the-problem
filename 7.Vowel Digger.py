def VoweX(N):					# We define the function
	a=0					# a,e,i,o,u represente the number of a,e,i,o,u in the word
	e=0
	i=0
	o=0
	u=0
	for k in range(0,len(N)):
		
		if N[k]=='a':			# When we take each letter of N, if it have 'a', we increase a. Else, if it have 'e', we increase e.
			a+=1
		elif N[k]=='e':			# Else, if it have 'e', we increase e.
			e+=1
		elif N[k]=='i':			# Else, if it have 'i', we increase i.
			i+=1
		elif N[k]=='o':			# Else, if it have 'o', we increase u.
			o+=1
		elif N[k]=='u':			# Else, if it have 'u', we increase u.
			u+=1
		else:				# Else, the result is 0.
			r=0
		
	C=a+e+i+o+u+r				# After, We do the summation of all vowel in the word
	return C

#For example

print(VoweX('bananaofmonkeys'))
