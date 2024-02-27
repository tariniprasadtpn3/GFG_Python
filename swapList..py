n = int(input("Enter number of element in an array : "))

array = []

for i in range(n):
    element = int(input("Enter Elements : "))
    array.append(element)

print("Array List : ",array)

def swapElement(array):
    array[0],array[-1] = array[-1],array[0]
    
    return array

Result = swapElement(array)

print("Result is : ",Result)


