Frequency of Elements
To find the frequency of numbers in a list and display in sorted order.
Constraints: 
1<=n, arr[i]<=100 
Input: 
1 68 79 4 90 68 1 4 5 
output:
 1 2
 4 2
 5 1
 68 2
 79 1 
90 1


For example:
Input	Result
4 3 5 3 4 5	3 2
4 2
5 2


def count_frequency(arr):
    frequency = {}
    
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    
    sorted_frequency = sorted(frequency.items())
  
    for num, freq in sorted_frequency:
        print(num, freq)

arr = list(map(int, input().split()))

count_frequency(arr)
