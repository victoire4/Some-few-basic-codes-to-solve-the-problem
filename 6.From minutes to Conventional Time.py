def ClockX(n):				# We define the function

	if n<60:
		H=str(0)
		M=str(n)
		if n<10:
			R= '0'+ H +':'+'0'+ M
		else:
				R= '0'+H +':'+ M
	else :
		H=str(n//60)
		M=str(n%60)
		if (n//60)<10 and (n%60)<10:
			R= '0'+ H +':'+'0'+ M
		elif (n//60)<10 and (n%60)>10:
			R= '0'+ H +':'+ M
		elif (n//60)>10 and (n%60)<10:
			R= H +':'+'0'+ M
		elif (n//60)>10 and (n%60)>10:
			R= H +':'+ M
		else:
			R= H +':'+'0'+ M
	return R
	

#For example
print(ClockX(67))
