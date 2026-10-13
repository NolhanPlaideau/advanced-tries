
class Restaurant:
  name = ''        # (text string)
  category = ''    # (text string)
  rating = 0     # (decimal number)
  delivery = False # (boolean value) 

bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

Steak_n_shake= Restaurant()

Steak_n_shake.name='Steak\'n shake'
Steak_n_shake.category = 'Fast Food'
Steak_n_shake.rating = 5
Steak_n_shake.delivery = True

Five_Guys= Restaurant()

Five_Guys.name='Five Guys'
Five_Guys.category = 'Fast Food'
Five_Guys.rating = 5
Five_Guys.delivery = True

print(vars(bobs_burgers))
print(vars(Steak_n_shake))
print(vars(Five_Guys))

