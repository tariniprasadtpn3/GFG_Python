
def factorialNum(num):
    if num == 0:
        return 1
    
    return num * factorialNum(num-1)


num = int(input("Enter Number : "))

factorial = factorialNum(num)

print("Factorial number : ",factorial)