''' Coding Bootcamp - Assignment 
-Title:  Assignment 4a Brief Python
-Last name : Pantelakis
-First Name: Ioannis
-Advisors: Galanopoulou Rafaila, Tyrovola Sarantia, Tzoumba Danae
-Python ver:3.9.2
-win: win10 64bit

'''

'''
This is the main module that executes the program.
'''
from u_i import User_Interface
from context import T_Shirt_payment
from strategy import PaymentCredit,PaymentBank,PaymentCash
from bubblesort_assignment import bubbleSort
from bucketsort_assignment import bucketSort
from quicksort_assignment import quick_sort

def main():
    # graphic-message
    print('\n\n',"Welcome to the Assignment4 T-shirt sorting Algorithms!".center(140))

    #Creation of Dummy T-Shirts
    shirts = [T_Shirt_payment() for i in range(40)]
    print('\n\n'+User_Interface.divider(30,' T-shirts Before the use of sorting algorithms: '))
    print()
    x=1
    for shirt in shirts: #print Dummy T-shirts before use of algorithms
        print(f"{x}: {shirt}")
        x=x+1
    print()

    algos=[bubbleSort,bucketSort,quick_sort] #Creation of list with algorithms for making automatic the implementation

    for case in range(1,9): #Loop for the cases 1-8
        if case == 1: #Case1 --> Size in ascending
            features=['_t_size'] # sorting variables 
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 1 --> Size in ascending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 1:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 1:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 1:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()
        elif case == 2: #Case2 --> Size in descending
            features=['_t_size'] # sorting variables 
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 2 --> Size in descending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features,asc=False)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 2:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 2:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 2:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()
        elif case == 3: #Case3 --> Color in ascending
            features=['_t_color'] # sorting variables 
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 3 --> Color in ascending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 3:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 3:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 3:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()    
        elif case == 4: #Case4 --> Color in descending
            features=['_t_color'] # sorting variables  
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 4 --> Color in descending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features,asc=False)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 4:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 4:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 4:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print() 
        elif case == 5: #Case5 --> Fabric in ascending
            features=['_t_fabric'] # sorting variables   
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 5 --> Fabric in ascending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 5:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 5:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 5:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()   
        elif case == 6: #Case6 --> Fabric in descending
            features=['_t_fabric'] # sorting variables   
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 6 --> Fabric in descending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features,asc=False)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 6:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 6:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 6:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print() 
        elif case == 7: #Case7 --> Size and Color and Fabric in ascending
            features=['_t_size','_t_color','_t_fabric'] # sorting variables    
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 7 --> Size and Color and Fabric in ascending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 7:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 7:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 7:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print() 
        else: #Case8 --> Size and Color and Fabric in descending
            features=['_t_size','_t_color','_t_fabric'] # sorting variables     
            print('\n\n'+User_Interface.divider(70,'T-shirts After algorithms for case 8 --> Size and Color and Fabric in descending'))
            print()
            for algo in algos: #run each one of algorithm from the list for each one case
                algo(shirts,features,asc=False)
                if algo == bubbleSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bubbleSort algorithm, case 8:'))
                    print()
                elif algo == bucketSort:
                    print('\n\n'+User_Interface.divider(30,'T-shirts After bucketSort algorithm, case 8:'))
                    print()
                else: 
                    print('\n\n'+User_Interface.divider(30,'T-shirts After quickSort algorithm, case 8:'))
                    print()
                x=1
                for shirt in shirts:
                    print(f"{x}: {shirt}")
                    x=x+1
                print() 




    #End of program - graphic- messages
    User_Interface.exitprogram()

if __name__=='__main()__':
    main()

main()  