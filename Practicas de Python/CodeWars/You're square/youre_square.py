def is_square(n):
    if n < 0:
        return False 
    else:
        for i in range(0,n+1):
            if i**2 == n:
                return True
                break
            elif i**2 > n:
                break
        return False
    
#Best solution
#import math
#def is_square(n):
#    return n > -1 and math.sqrt(n) % 1 == 0;

