
# creating a list containing 4 items
menu_list = ['Hot-Coffee_items', 'Iced-Coffee_items', 'Drinks_items', 'Savoury_items']

# creating a dictionary containing stock-value for each item from the menu
stock_dictionary = {'Hot-Coffee_items': 10, 'Iced-Coffee_items': 7, 'Drinks_items': 6, 'Savoury_items': 7}

# creating another dictionary containing price for each item from the menu
price_dictionary = {'Hot-Coffee_items': 3.40, 'Iced-Coffee_items': 2.20, 'Drinks_items': 3.50, 'Savoury_items': 9.99}

total_stock = 0          # giving value to the variable

for items in menu_list:  # using for-loop to give the condition
    
    # calculating the total worth of available-stocks from the created dictonaries based on the assigned-values
    total_stock += (stock_dictionary[items] * price_dictionary[items]) 

print('The total stock_worth of cafe items in GBP: £',total_stock)
print()