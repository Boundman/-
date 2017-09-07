#Short function min:
def findMin(arr):
    return min(arr)

#Long function min:
def findMinimum(arr):
    minimum = arr[0]
    for i in range(len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]
    return minimum

#function average_arifm:
def averageArifm(arr):
    sumAll = 0
    for i in range(len(arr)):
        sumAll += arr[i]
    return sumAll/len(arr)

mas = [100, 23, 76, 44, 123, 214, 32, 888]
print("FIND MIN:")
print("      Min element(calculated with SHORT func):", findMin(mas))
print("      Min element(calculated with LONG func):", findMinimum(mas))
print("FIND AVERAGE:")
print("      Average arifmetics:", averageArifm(mas))
input()
