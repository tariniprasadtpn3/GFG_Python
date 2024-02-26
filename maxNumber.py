# Approach 1 : usiing < operator

# def maxNum(a,b):
#     if a <= b:
#         return b
#     else:
#         return a

# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))

# maxNumber = maxNum(num1,num2)

# print("maximum Number : ",maxNumber)


# Approach 2 : using lamda

# maxNumber = lambda a,b: a if a >b else b

# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))

# maxNumb = maxNumber(num1,num2)

# print("maximum Number : ",maxNumb)

# Approach 3 : using max func

# num1 = int(input("Enter Num1 : "))
# num2 = int(input("Enter Num2 : "))

# maxNumber = max(num1,num2)

# print("maximum Number : ",maxNumber)

# Approach 4 : ternary operator

# a = int(input("Enter Num1 : "))
# b = int(input("Enter Num2 : "))

# print("maximum Number : ", a if a>=b  else b)

# Approach 5 : using List

# a = int(input("Enter Num1 : "))
# b = int(input("Enter Num2 : "))

# x = [a,b]

# x.sort()

# print("maximum number is :", x[-1])