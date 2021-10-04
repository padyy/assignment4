from context import T_Shirt_payment

class User_Interface:   #Class for User_interface

    @staticmethod
    def checkChoices(message,options,errorMessage): ##function for checking the inputs (use for many cases. message for the user, options for values to check and errorMessage if something goes wrong
        inputVal = input(message).upper()
        while inputVal not in options:
            print(errorMessage)
            print()
            inputVal = input(message).upper()
        return inputVal

    @staticmethod
    def divider(number_of_lines,mid_word=''): ##function for design of menu with lines
        draw=' '
        for i in range(int(number_of_lines/2)):
            draw+="-"
        draw+=mid_word
        for i in range(number_of_lines-int(number_of_lines/2)):
            draw+="-"
        return draw

    @staticmethod
    def Menu(): ##1st menu appear to user 
        print('\n\n',"Welcome to the Assigment3 T-shirt shop".center(80))
        print('Please choose something from the menu'.center(82))
        print('\n\n'+User_Interface.divider(70,' MENU '))
        print('1. Buy a t-shirt')
        print('2. Exit')
        print(User_Interface.divider(79))
        return int(User_Interface.checkChoices('Enter your choice [1-2]: ',['1','2'],'Wrong Choise..Please enter an integer between 1-2.'))

    @staticmethod
    def tshirt_buy(tshirt_list,top=False): #function for t-shirt transaction
        if top:
            print('Please give the info for the t-shirt you want to buy.\n') 
        print("T-shirt's availabe Colors: "+','.join([color.capitalize() for color in T_Shirt_payment.color])+".")
        Tshirt_color = User_Interface.checkChoices("Give T-shirt's color: ",[color.upper() for color in T_Shirt_payment.color],'Wrong color.Please give one of: '+','.join([color.capitalize() for color in T_Shirt_payment.color])+'.').lower()
        print("T-shirt's availabe sizes: "+','.join([size.capitalize() for size in T_Shirt_payment.size])+".")
        Tshirt_size = User_Interface.checkChoices("Give T-shirt's size: ",[size.upper() for size in T_Shirt_payment.size],'Wrong size.Please give one of: '+','.join([size.capitalize() for size in T_Shirt_payment.size])+'.').lower()
        print("T-shirt's availabe fabric: "+','.join([fabric.capitalize() for fabric in T_Shirt_payment.fabric])+".")
        Tshirt_fabric = User_Interface.checkChoices("Give T-shirt's fabric: ",[fabric.upper() for fabric in T_Shirt_payment.fabric],'Wrong fabric.Please give one of: '+','.join([fabric.capitalize() for fabric in T_Shirt_payment.fabric])+'.').lower()
        print("Please choose a payment method from the following list: "+','.join([payment.capitalize() for payment in T_Shirt_payment.payment])+".")
        Tshirt_payment = User_Interface.checkChoices("Give payment method: ",[payment.upper() for payment in T_Shirt_payment.payment],'Wrong payment method.Please give one of: '+','.join([payment.capitalize() for payment in T_Shirt_payment.payment])+'.').lower()

        new_Tshirt = T_Shirt_payment ( t_color = Tshirt_color, t_size = Tshirt_size, t_fabric = Tshirt_fabric , t_payment = Tshirt_payment, strategy=None )
        tshirt_list.append(new_Tshirt) #fill the tshirt list with as many as tshirt user likes 
        anotherDec = User_Interface.checkChoices("Want to buy another t-shirt? Type 'y' for yes and 'n' for no.",['Y','N'],'Wrong choice!') #ask user for adding another t-shirt
        if anotherDec == 'Y': #if yes fill inputs for another t-shirt
            User_Interface.tshirt_buy(tshirt_list,top=True) 
        else:
            print('\n')
            print('T-shirt transaction completed succesfully.')
        return tshirt_list #return tshirt list to main module.
    @staticmethod
    def exitprogram(): #prints for exit
        print(User_Interface.divider(79))
        print(User_Interface.divider(79))
        print('Program terminated. Thanks for using it.\nCopyrights: Pantelakis Ioannis\n')
