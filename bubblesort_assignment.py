from context import T_Shirt_payment

'''BubbleSort Algorithm'''

def bubbleSort(data,features,asc=True): #data is the data to be sorted / features is by wich feature to be sorted / asc is for ascending if true and descending if false
    n = len(data)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if (data[j].greaterThan(data[j+1],features) and asc) or (data[j].lessThan(data[j+1],features) and not asc): #greaterThan and lessThan are 2 functions explained context.py
                data[j], data[j+1] = data[j+1], data[j]


