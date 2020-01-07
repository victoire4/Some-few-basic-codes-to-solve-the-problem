
for x in range(1000,10000):					#the number have 4digit.So it is between 1000 and 9999
	y=sorted(list(str(x)))				# transformation of integer x to str ,after to list and we use sorted for range. We obtain Xmin but this type is list
	z=y[::-1]						# We reverse Xmin and we obtain Xmax but this type is list
	X=int(''.join(y))					# Join and convers the type of Xmin to integer
	Y=int(''.join(z))
	if (Y-X)==x:					# Join and convers the type of Xmin to integer
		print(x)					#'The value of number X such that Xmax-Xmin=X is:',.
