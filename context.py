'''
This is the module for context of the strategy Pattern. In it, there is the class for the product,
which in our case is the T-shirt. Context can use the desired strategy.
'''
from strategy import PaymentCredit,PaymentBank,PaymentCash
import random

class T_Shirt_payment: #This is the context class for the strategy Pattern

    color = sorted(['red','orange','yellow','green','blue','indigo','violet']) #In this line and above  are the lists with the accepted inputs for color,size,fabric and payment
    size = ['xs','s','m','l','xl','xxl','xxxl']
    fabric = sorted(['wool','cotton','polyester','rayon','linen','cashmere','silk'])
    payment = sorted(['credit','bank','cash'])

    #dictionaries with the price of each color,size and fabric
    color_prices={'red': 7 , 'orange': 5.70 , 'yellow': 5.60, 'green': 5.90 , 'blue': 6.20 , 'indigo': 7.30,'violet': 6.60 }
    size_prices={'xs': 5, 's': 5.5, 'm': 6.5, 'l': 7.2, 'xl': 7.8, 'xxl': 8, 'xxxl':8.5}
    fabric_prices={'wool' : 10, 'cotton': 13, 'polyester': 11.5, 'rayon':14, 'linen': 12, 'cashmere':16, 'silk':15.5}
    
    def __init__(self, t_color=None, t_size=None, t_fabric=None, t_payment=None, strategy=None ) : #init of T_shirt_payment
        self._t_color = t_color
        self._t_size = t_size
        self._t_fabric = t_fabric
        self._t_payment = t_payment
        self._strategy = strategy
        
        #Dummie data for T-shirts if no parameters are given to Tshirt
        if t_color is None:    
            self._t_color = self.color[random.randrange(len(self.color))] #random color choice
            self._t_color = self.color.index(self._t_color) #taking the indexes of colors so the sort algorithms work with numbers and not words.
           
        if t_size is None:
            self._t_size = self.size[random.randrange(len(self.size))]
            self._t_size = self.size.index(self._t_size) #taking the indexes of sizes so the sort algorithms work with numbers and not words.

        if t_fabric is None:
            self._t_fabric = self.fabric[random.randrange(len(self.fabric))]
            self._t_fabric = self.fabric.index(self._t_fabric) #taking the indexes of sizes so the sort algorithms work with numbers and not words.

        if t_payment is None:
            self._t_payment = self.payment[random.randrange(len(self.payment))]
        if strategy is None:
            if self._t_payment == 'credit':
                self._strategy = PaymentCredit()
            elif self._t_payment == 'bank':
                self._strategy = PaymentBank()
            elif self._t_payment == 'cash':
                self._strategy = PaymentCash()
                
    def __str__(self): # Overide str method for print necessary info for given assignment
        return f"A {self.size[self._t_size]}, {self.color[self._t_color]} made of {self.fabric[self._t_fabric]} T-shirt, paid with {self._t_payment}."

    #Properties and setters for getting the protected attributes
    @property
    def t_color(self):
        return self._t_color

    @property
    def t_size(self):
        return self._t_size

    @property
    def t_fabric(self):
        return self._t_fabric

    @property
    def t_payment(self):
        return self._t_payment

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter #setter for strategy so it can be redefined outside the class
    def strategy(self,value):
        self._strategy = value

        
    def executeStrategy(self): #The function that executes the chosen strategy
        return self._strategy.dopayment(self)

    def totalCost(self): # Function that culculates the total cost of each t-shirt object
        total_cost = self.color_prices[self.t_color] + self.size_prices[self.t_size] + self.fabric_prices[self.t_fabric]
        return total_cost

    #function for checking if feature of t-shirt1 is greater than feature of t-shirt2.
    #It's use is for making the procedure automatic by giving for input into the function self(wich is the tshirt1), T-shirt2 and the feature or features  by wich the T-shirts need to be sorted    
    def greaterThan(self, t_shirt2, feature): 
        if type(feature) == list:
            for feat in feature:
                if getattr(self, feat) > getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) < getattr(t_shirt2, feat):
                    return False
            return False
        else:
            return getattr(self, feature) > getattr(t_shirt2, feature)
            
    #function for checking if feature of t-shirt1 is greater than or equal to feature of t-shirt2.
    def greaterThanEqual(self, t_shirt2, feature): 
        if type(feature) == list:
            for featIndex, feat in enumerate(feature):
                if getattr(self, feat) > getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) < getattr(t_shirt2, feat):
                    return False
                elif getattr(self, feat) == getattr(t_shirt2, feat) and featIndex == (len(feature) - 1):
                    return True
            return False
        else:
            return getattr(self, feature) >= getattr(t_shirt2, feature)

    #function for checking if feature of t-shirt1 is less than feature of t-shirt2.    
    def lessThan(self, t_shirt2, feature):
        if type(feature) == list:
            for feat in feature:
                if getattr(self, feat) < getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) > getattr(t_shirt2, feat):
                    return False
            return False
        else:
            return getattr(self, feature) < getattr(t_shirt2, feature)

    #function for checking if feature of t-shirt1 is less than or equal to feature of t-shirt2.    
    def lessThanEqual(self, t_shirt2, feature):
        if type(feature) == list:
            for featIndex, feat in enumerate(feature):
                if getattr(self, feat) < getattr(t_shirt2, feat):
                    return True
                elif getattr(self, feat) > getattr(t_shirt2, feat):
                    return False
                elif getattr(self, feat) == getattr(t_shirt2, feat) and featIndex == (len(feature) - 1):
                    return True
            return False
        else:
            return getattr(self, feature) <= getattr(t_shirt2, feature)
    
    #get number of buckets for bucketSorting
    def bucketsNum(features):
        featureToArray = {'_t_color':T_Shirt_payment.color,'_t_size':T_Shirt_payment.size,'_t_fabric':T_Shirt_payment.fabric,'_t_payment':T_Shirt_payment.payment}
        return len(featureToArray[features[0]])
    
    #get bucket index for bucketSorting
    def toIndex(self,features, asc=True):
        featureToArray = {'_t_color':T_Shirt_payment.color,'_t_size':T_Shirt_payment.size,'_t_fabric':T_Shirt_payment.fabric,'_t_payment':T_Shirt_payment.payment}
        if asc:
            return getattr(self, features[0])
        else:
            return (len(featureToArray[features[0]]) - 1) - getattr(self, features[0])