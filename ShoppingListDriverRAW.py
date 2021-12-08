'''
This is the driver module that will contain:

1. A function that creates a list of objects. The function accepts no parameters but returns 
the list of objects. The function should: 
a. Create an empty list. 
b. Prompt the user for the number of items. This value will be used to determine 
the number of repetitions for a necessary loop. (Make sure to include input 
validation to ensure that the number of items purchases is at least 1.) 
c. Contain a loop that prompts the user for the name of the item and the amount 
of the item in pounds. (Make sure to include input validation to ensure that the 
number of pounds is greater than 0.) The loop should use this information to 
create an object, and append the object to the list 
d. Returns the list (once the loop is completed)

2. A function to display the contents of the list. This function accepts a list of objects as a 
parameter but does not return a value. The function should: 
a. display the contents of each object in the list (all 4 attributes). Make sure to 
include appropriate formatting for prices. 

3. A function that calculates the total cost of all items. Recall, your object will only have the 
cost of each item (based on the amount of pounds ordered for that item). This function 
accepts the list of objects as a parameter and returns a value. This function should: 
a. access the individual cost of each ordered item 
b. calculate the total cost of all the items in the list 
c. return the total cost 

4. A main function. Your main function should: 
a. Call the three aforementioned functions
'''
#importing the class module
from ShoppingListRAW import ShopListRAW

#creating a function that creates a list of objects
def CreateShopListRAW():
    #creates empty list
    ShopList = []
    #input validation for the number of items
    while True:
        #setting order amount as a global value
        global OrderAmount
        #prompting user input for the amount of items they want to order
        OrderAmount = int(input('How many items would you like to order today?'))
        #input validation for the order amount
        if OrderAmount < 1:
            print('Whoops, that\'s not possible, please enter an amount of at least 1')
        else:
            break
    #for loop for the items the user wants to buy 
    for amount in range(OrderAmount):
        print('\nItem #',amount + 1,'-')
        #prompting user input for the name of the food
        FoodName = input('Enter the name of the desired food:')
        #prompting user input for the amount of food in pounds
        FoodAmount = float(input('Enter desired amount in pounds:'))
        #input validation for the amount of food in pounds
        while True:
            if FoodAmount <= 0:
                print('Sorry, the food\'s weight must be greater than 0.\nPlease try again.')
            else:
                break
        #adding the contents to the list
        ShopList.append(ShopListRAW(FoodName, FoodAmount))
    #returning the list    
    return ShopList

#creates a function to display the attributes
def DisplayShopListRAW(List):
    #
    print("\nHere are the list of the item(s) ordered:")
    print("--------------------------------------------------------")
    #for loop to print out each object's attributes in the class
    for i in List:
        print(f'\n{i}') 

#creates a function to calculate the total cost of items
def CalcTotalRAW(List):
    #creating a variable for the total cost
    TotalCost = 0
    #for loop to calculate the total cost of each item
    for x in List:
           TotalCost = x.getCalcCostRAW() + TotalCost
    #printing the result of the total cost calculation
    print('\nTotal Cost: ${:,.2f}'.format(TotalCost))


#creates a main function to call the other 3 functions
def main():
    #calling the function to create the list and storing the list in variable form
    ShopList = CreateShopListRAW()
    #calling the function to display the item list
    DisplayShopListRAW(ShopList)
    #calling the function to calculate and display the total cost of the purchase
    CalcTotalRAW(ShopList)

#testing the main() function
test = main()
    
    
    

    




