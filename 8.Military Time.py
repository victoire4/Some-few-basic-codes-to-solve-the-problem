def Military(T): 				# We define the function
      
    					# Checking if last two elements of time 
    					# if they are AM and first two elements are 12 
    if T[-2:] == "AM" and T[:2] == "12": 
        return "00" + str1[2:-2] 		#The form of T is hh:hhAM. so, we return 00:hh because 12:00AM in 12 hours is 00:00 in 24 hours
          
    					# We remove the AM     
    elif T[-2:] == "AM": 
        return str1[:-2] 
      
    					
    					# if the last two element are PM and first two elements are 12    
    elif T[-2:] == "PM" and T[:2] == "12": 
        return T[:-2] 			#  12:00PM in 12 hours is 12:00 in 24 hours. So, we remove only PM
          
    else: 
          
        					# We add 12 to hours and remove PM 
        return str(int(T[:2]) + 12) + T[2:5] 
  

# For example  
     
print(Military("03:00PM")) 
