stock={'banana':6,
'apple':0,
'orange':32,
'pear':15,}
prices={'banana': 4,
'apple':2,
'orange':1.5,
'pear':465465465}

def uppercase(x):
  return x[0].upper()+x[1:]

name=input('''What is your name?
''')
print('Hi, %s, welcome to my fruit store. Here is the menu:'%(name))
print()

def menu():
  for fruit in prices:
    print(uppercase(fruit))
    print('Price: $%s'%(prices[fruit]))
    print('Stock: %s'%(stock[fruit]))
    print()
  print('You have: $%s'%(money))
  print()

def ask_fruit(money):
  fruit=input('''What fruit do you want?
''')
  print()
  if fruit in stock:
    if stock[fruit]>0:
      ask_amount(fruit,money)
    else:
      print('''Sorry, %ss are out of stock
'''%(fruit))
      ask_fruit(money)
  else:
    print('''Sorry, we don\'t have that, look at the menu.
    ''')
    ask_fruit(money)

def ask_amount(fruit,money):
  amount=int(input('''How many %ss do you want?
'''%(fruit)))
  print()
  if amount<=0:
    print('''At least buy one.
  ''')
    ask_amount(fruit,money)
  elif stock[fruit]>=amount:
    sell(fruit,amount,money)
  else:
    print('''Sorry, we don\'t have that many %ss.
    '''%(fruit))
    ask_amount(fruit,money)

def sell(fruit,amount,money):
  cost=prices[fruit]*amount
  confirmation=input('''Are you sure? That will be $%s.
-Yes
-No
'''%(cost)).lower()
  print()
  if confirmation=='yes':
    money-cost
    print('''Thank you for the business!
''')
    stock[fruit]=stock[fruit]-amount
    ask_again()
  elif confirmation=='no':
    ask_fruit(money)
  else:
    print('''Answer me.
''')
    sell(fruit,amount,money)

def ask_again():
  answer=input('''Do you want anything else?
-Yes
-No
''').lower()
  print()
  if answer=='yes':
    menu()
    ask_fruit(money)
  elif answer=='no':
    print('Okay, bye.')
  else:
    print('Answer me.')
    ask_again()

money=132
menu()
ask_fruit(money)