def get_item(item_number):
    if item_number == 1:
        return '🍔 Cheeseburger'
    elif item_number == 2:
        return '🍟 Fries'
    elif item_number == 3:
        return '🥤 Soda'
    elif item_number == 4:
        return '🍦 Ice Cream'
    elif item_number == 5:
        return '🍪 Cookie'    
    else:
        return 'Item not found' 

def welcome(): 
    print(1,'-🍔 Cheeseburger',
          2,'-🍟 Fries',
          3,'-🥤 Soda',
          4,'-🍦 Ice Cream',
          5,'-🍪 Cookie') 

welcome()

option = int(input('What would you like to order? '))
print(get_item(option)) 