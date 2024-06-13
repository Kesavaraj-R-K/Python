Peak Element
Given an list, find peak element in it. A peak element is an element that is greater than its neighbors.
An element a[i] is a peak element if
A[i-1] <= A[i] >=a[i+1] for middle elements. [0<i<n-1]
A[i-1] <= A[i] for last element [i=n-1]
A[i]>=A[i+1] for first element [i=0]
Input Format
The first line contains a single integer n , the length of A .
The second line contains n space-separated integers,A[i].

Output Format
Print peak numbers separated by space.

Sample Input
5
8 9 10 2 6
Sample Output
10 6


For example:
Input	Result
4
12 3 6 8 	12 8

def find_peak(arr):
    peak_elements = []

    if arr[0] >= arr[1]:
        peak_elements.append(arr[0])

    for i in range(1, len(arr) - 1):
        if arr[i - 1] <= arr[i] >= arr[i + 1]:
            peak_elements.append(arr[i])

    if arr[-1] >= arr[-2]:
        peak_elements.append(arr[-1])

    return peak_elements

n = int(input())

arr = list(map(int, input().split()))

peak_elements = find_peak(arr)
print(*peak_elements)
