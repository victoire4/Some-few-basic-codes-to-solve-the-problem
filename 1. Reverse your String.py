def ReveX(N):								# We define the function

	M=""									# We create a empty string
	i=1
	while i<=(len(N)):
		M+=N[-i]							#We know that N[-1] is a last element of n. So, we put gradualy in M respectively the last element of N 
		i+=1
	return(M)


#For example

print(ReveX('banana'))
