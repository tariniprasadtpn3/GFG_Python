# input a number and check fibonnaci number or not 


import math
def isPerfectSqr(number):
    s = int(math.sqrt(number))
    if s*s == number:
        return True
    else:
        return False

def isFibonnaciSeries(number):
    if isPerfectSqr(5*(number**2)+4) or isPerfectSqr(5*(number**2)-4):
        return True 
    else:
        return False


num = int(input("Enter Number : "))

result = isFibonnaciSeries(num)

print("Result : ",result)