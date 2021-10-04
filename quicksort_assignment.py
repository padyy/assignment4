from context import T_Shirt_payment

'''Quick sort algorithm'''

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(array, features, asc, start, end):
    pivot_index = start 
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and ((array[start].lessThanEqual(pivot,features) and asc) or (array[start].greaterThanEqual(pivot,features) and not asc)): #lessThanEqual and greaterThanEqual are explained in context.py
            start += 1
        while (array[end].greaterThan(pivot,features) and asc) or (array[end].lessThan(pivot,features) and not asc): #greaterThan and lessThan are explained in context.py
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end
      
# The main function that implements QuickSort 
def quick_sort(array, features, asc=True, start=0, end=None): #array is the data to be sorted / features is by wich feature to be sorted / asc is for ascending if true and descending if false / start is starting point of array / end is end point of array
    if end is None: end = len(array)-1
    if (start < end):
        p = partition(array, features, asc, start, end)
        quick_sort(array, features, asc, start, p - 1)
        quick_sort(array, features, asc, p + 1, end)

