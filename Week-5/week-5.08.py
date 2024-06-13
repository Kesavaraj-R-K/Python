Merge Two Sorted Arrays Without Duplication
Output is a merged array without duplicates.
Input Format
N1 - no of elements in array 1
Array elements for array 1
N2 - no of elements in array 2
Array elements for array2
Output Format
Display the merged array

Sample Input 1

5
1 
2 
3 
6 
9
4
2 
4 
5 
10

Sample Output 1

1 2 3 4 5 6 9 10

def merge_arrays_without_duplicates(arr1, arr2):
    result_set = set(arr1 + arr2)
    merged_sorted_array = sorted(result_set)
    return merged_sorted_array
def process_input():
    n1 = int(input())
    array1 = []
    for _ in range(n1):
        element = int(input())
        array1.append(element)
 
    n2 = int(input())
    array2 = []
    for _ in range(n2):
        element = int(input())
        array2.append(element)
 
    result = merge_arrays_without_duplicates(array1, array2)
 
    print(" ".join(map(str, result)))
