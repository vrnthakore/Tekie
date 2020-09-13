# Assumed that all elements in the list are different 
arr = []
n = int(input('Enter number of elements in the list : ')) 

for i in range(0, n): 
    e = int(input())
    arr.append(e)
      

print(arr)

arr_sorted = sorted(arr,reverse = True)

print(arr_sorted)

print('The second largest element is : ' + str(arr_sorted[1]))
