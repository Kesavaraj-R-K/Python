Distinct Elements in an Array
Program to print all the distinct elements in an array. Distinct elements are nothing but the unique (non-duplicate) elements present in the given array.
Input Format:
First line take an Integer input from stdin which is array length n.
Second line take n Integers which is inputs of array.
Output Format:
Print the Distinct Elements in Array in single line which is space Separated

Example Input:
5
1 
2 
2 
3 
4
Output:
1 2 3 4
Example Input:
6
1 
1 
2 
2 
3 
3
Output:
1 2 3

For example:
Input	Result
5
1 
2 
2 
3
4
1 2 3 4 
6
1 
1 
2 
2 
3 
3
1 2 3


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
