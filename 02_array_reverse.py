# Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Examples:

# Input: arr[] = {1, 4, 3, 2, 6, 5}  
# Output: {5, 6, 2, 3, 4, 1}
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# Input: arr[] = {4, 5, 1, 2} 
# Output: {2, 1, 5, 4}
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

def reverse(arr):
    temp=[]
    for i in range(len(arr)-1,-1,-1):
        temp.append(arr[i])
    return temp
    

len=int(input("Enter the length of the array:"))
arr=[]
for i in range(len):
    arr.append(int(input("Enter the number:")))
print(reverse(arr))