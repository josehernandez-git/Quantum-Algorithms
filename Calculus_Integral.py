# -*- coding: utf-8 -*-





# Simple Integral, will only work for a simple variable (x), its nth power,
# its divisor, and its multiple.

# and does not use the solving methods for complex integration or negative exponents 


#--------------------------


# example: (3(x^2))/2   With Bounds 0 to 3



#--------------------------



# obtaing the variables x nth power

nth_x = int(input("To what power is this x variable? : "))



# getting the multiple if any

multiple = int(input("What is the multiple? : "))

divisor = int(input("What is the divisor? : "))



# obtaining the bounds of the integral

# upper
upper = int(input("What is the upper bound? : "))

# lower
lower = int(input("What is the lower bound? : "))


# this will be integer to be multipled one integration is done


if divisor == 0:
    
    divisor = 1
    lst_int = multiple/divisor 
    
else:
    lst_int = multiple/divisor 
    





# if n is zero then the variable x turns into 1, then its just the bounds 
# and multiple to compute 

if nth_x == 0:
    
    Zero_power = 0
    Zero_power = upper - lower
    Zero_power = Zero_power * lst_int
    
    print('{} is the computation to the integral.' .format(Zero_power))
    
    
    
    

    
    
# nth power greater than 0
    
if nth_x > 0:
        
 final_pos = 0
 den_nth = 0
        
 nth_x += 1    # adding 1 for integration
 den_nth = nth_x # denominator must match n power
        
        # exponent will be nth_x and denominator will be den_nth
        
 final_pos = ((upper**nth_x)/den_nth) - ((lower**nth_x)/den_nth)
        
        # multiple with divisor if any
        
 final_pos = final_pos * lst_int
        
 print('{} is the computation for the given integral.' .format(final_pos))
        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 