'''
This is the class definition module that will contain:
1. An initializer method, accepting two attributes (other than self) but containing 4 hidden attributes
2. A private method, that will store the list of items and their price per pound and 
    accepting no parameters (other than self) and returns no value. 
3. A public method, to calculate the cost of the ordered food, accepting no parameters (other than self), 
    but returns the calculated cost. 
4. Accessors as needed.

Class Description:
A shopping list with 4 attributes
1. Food Name, 
2. Food Amount (in pounds),
3. Food Price / pound,
4. Calculated cost of the ordered food item(s)

'''

#Class definition
class ShopListRAW:
    #initializer method - 2 parameters, 4 hidden attributes
    #creating the 2 hidden variables
    def __init__(self, FoodName = '', FoodAmount = 0.00):
        #creating the 4 hidden attributes
        #updated by initializer input: 
        #food name, food amount (in pounds)
        self.__FoodName = FoodName
        self.__FoodAmount = FoodAmount
        #updated by private methods:
        #price of food/pound
        self.__FoodPrice = self.__FoodListRAW()#FoodPrice
        #updated by public methods:
        #calculated price of ordered item(s)
        self.CalcCost = self.setCalcCostRAW()#CalcCost
    
    #mutator method for the FoodName parameter
    def setFoodNameRAW(self, FoodName):
        self.__FoodName = FoodName
    
    #mutator method for the FoodAmount parameter
    def setFoodAmountRAW(self, FoodAmount):
        self.__FoodAmount = FoodAmount

    #private mutator method, for storing item list and price
    def __FoodListRAW(self):
        #creating the structure for the food's standard price
        if self.__FoodName == 'Dry Cured Iberian Ham':
            self.__FoodPrice = 177.80

        elif self.__FoodName == 'Wagyu Steaks':
            self.__FoodPrice = 450.00

        elif self.__FoodName == 'Matsutake Mushrooms':
            self.__FoodPrice = 272.00

        elif self.__FoodName == 'Kopi Luwak Coffee':
            self.__FoodPrice = 306.50

        elif self.__FoodName == 'Moose Cheese':
            self.__FoodPrice = 487.20

        elif self.__FoodName == 'White Truffles':
            self.__FoodPrice = 3600.00

        elif self.__FoodName == 'Blue Fin Tuna':
            self.__FoodPrice = 3603.00

        elif self.__FoodName == 'Le Bonnotte Potatoes':
            self.__FoodPrice = 270.81
        #else clause for if the food name is misspelled or an item not on the table is referenced
        else:
            self.__FoodPrice = 0.00
        
        return self.__FoodPrice

    #public mutator method, for calculating price of ordered item(s) 
    #formula used: amount of food (in pounds) x price per pound 
    def setCalcCostRAW(self):
        return self.__FoodAmount * self.__FoodPrice
        
    #accessor method for food name
    def getFoodNameRAW(self):
        return self.__FoodName
    
    #accessor method for food amount in pounds
    def getFoodAmountRAW(self):
        return self.__FoodAmount

    #accessor method for returning the CalcCost data
    def getCalcCostRAW(self):
        return self.CalcCost

    #accessor method for the food price
    def getFoodPrice(self):
        return self.__FoodPrice
    
    #str method to return the item attributes in str form
    def __str__(self):
        return f'Item Name: {self.getFoodNameRAW()}\nAmount Ordered: {self.getFoodAmountRAW()} pounds\nPrice per pound: ${self.__FoodListRAW():.2f}\nPrice of Order: ${self.getCalcCostRAW()}'
       
    

    











