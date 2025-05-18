# Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

# Examples:

# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#         Maximum element is: 9

# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#         Maximum element is: 35


def min_max(arr):
    
    min=arr[0]
    max=arr[0]
    
    for num in arr:
        if num>max:
            max=num
        if num<min:
            min=num
    print("Minimum element is:",min)
    print("Maximum element is:",max)

len=int(input("Enter the length of the array:"))
arr=[]
for i in range(len):
    arr.append(int(input("Enter the number:")))

min_max(arr)