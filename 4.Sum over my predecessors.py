def FactX(n):					# We define the function
	M=0					#Initialization of M is 0 because all number plus 0 is the same.
	i=1
	while i<=n :				#We put in M, the summation of all the integer between 1(initialization of i) and the number n
		M+=i
		i+=1
	return M


#for exemple

print(FactX(10))
