n = int(input("Enter number of element in an array : "))

array = []

for i in range(n):
    element = int(input("Enter Elements : "))
    array.append(element)

print("Array List : ",array)

existElement = int(input("Enter Element to check Exist in list or not : "))


if existElement in array:
    print("Element is exist")
else:
    print("Element is not exist")   