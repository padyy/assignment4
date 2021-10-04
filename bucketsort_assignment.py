from context import T_Shirt_payment

'''BubbleSort Algorithm'''

def insertionSort(b,features,asc=True): #insertionSort algorithm for sorting the buckets/ b is the bucket / features is by wich feature to be sorted / asc is for ascending if true and descending if false
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while ( j >= 0 and b[j].greaterThan(up,features) and  asc) or (j >= 0 and b[j].lessThan(up,features) and not asc): #greaterThan and lessThan are 2 functions explained context.py
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    

# The main function that implements bucketSort              
def bucketSort(x, features, asc=True): # x is the array to be sorted / features is by wich feature to be sorted / asc is for ascending if true and descending if false
    slot_num = T_Shirt_payment.bucketsNum(features) #bucketsNum is a function explained in context.py
    arr = [[] for i in range(slot_num)]
    
    # Put array elements in different buckets
    for j in x:
        index_b = j.toIndex(features, asc) #toIndex is a function explained in context.py
        arr[index_b].append(j)
     
    # Sort individual buckets
    for i in range(len(arr)):
        arr[i] = insertionSort(arr[i],features,asc)
         
    # concatenate the result
    k = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
 
