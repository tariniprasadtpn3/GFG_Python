n = int(input("Enter number of element want to add in an array : "))

arr = []
for i in range(n):
    elem = int(input("Enter Elements : "))
    arr.append(elem)

print("Array Elements Are : ",arr)

sum = 0

for i in range(n):
    sum = sum + arr[i]

print("Sum of an array is : ",sum)    