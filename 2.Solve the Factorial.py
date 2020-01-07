def FactX(n):				# We define the function
	M=1				#Initialization of M is 1 because all number multiple by 1 is the same.
	i=1				#We put in M, the multiplication of all the integer between 1(initialization of i) and the number n
	while i<=n :
		M*=i
		i+=1
	return M


#for exemple

print(FactX(5))
