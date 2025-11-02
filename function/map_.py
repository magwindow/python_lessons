from functools import reduce


arr1 = [1,2,3,4,5]
arr2 = map(lambda x:x**2, arr1)
arr3 = reduce(lambda x,y:x+y, arr1)

print(list(arr2))
print(arr3)