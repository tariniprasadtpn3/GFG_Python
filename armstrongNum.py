num = input("Enter Number : ")

sum = 0 
r = len(num)
num = int(num)
temp = num
while num > 0:
    digit = num % 10
    sum = sum + digit ** r
    num = num // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")    


