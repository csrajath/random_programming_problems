# Find the median of two sorted arrays
"""
1. combine the lists
2. find the length
3. if length is odd, the element at (len/2)+1 position is the median
4. if length is even, the average of the element at (len/2) and (len/2)+1 will be the median
"""

def median_find(arr1, arr2):
    arr3 = arr1 + arr2
    if len(arr3) % 2 == 1:
        median = arr3[(int(len(arr3)/2))]
    else:
        m1 = arr3[int(len(arr3)/2)-1]
        m2 = arr3[(int(len(arr3)/2))]
        median = (m1+m2)/2
    return median
print(median_find([1,2,3,4,5],[6,7,8,9]))
print(median_find([10,20],[30,40]))
