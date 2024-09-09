# About my first python project

#Basic Project1

#item in menu

menu={
    'chai':5,
    'vada pav':15,
    'samosa':20,
    'sada Dosa':30,
    'masala Dosa':40,
    'pizza':50,
    'momo':40
}

print('Welcome to Raju Corner\nMenu')

print("Chai Rs:5\nVada pav Rs:15\nSamosa Rs:20\nSada Dosa Rs:30\nMasala Dosa Rs:40\nPizza Rs:50\nMomo Rs:40")

order_total=0 #to add item prize

#Order

item_1=input('Enter Your first item here ').lower()
if item_1 in menu:
    order_total += menu[item_1]
    print('Your item',item_1,'added to order.')
else:
    print('Please order somthing from menu')

#anything_else

anything_else=input('Do you want anything else (Yes/No)')
if anything_else == 'Yes'or'yes':
#item 2
    Item_2=input('Whats do you want? ').lower()
    if Item_2 in menu:
        order_total+=menu[Item_2]
        print('Your Item',Item_2,'added to order')
        
else:
    print('Please order somthing from menu')

print('You have to pay',order_total)
print('Thanks for visiting')
