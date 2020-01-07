def longest(N): 									# We define the function
 
    A = N.split(' ')  								# A is a list. Each element of A is one word of N

    L = 0   										# Initialisation of the size for the comparison

    for i in range(0,len(A)):    
        if (len(A[i]) > L):							
            W= A[i]
            L = len(A[i])   						# We compare lement by element. When lenght of A[i] is the biggest, L take this values and the result W take the word A[i]
   													# Then, gradualy, we find the longest word of N
    return W

#For example

print (longest("today is my birthday")) 
