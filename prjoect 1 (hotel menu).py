#Basic Project1
#item in menu
menu={
    'chai':8,
    'vada pav':15,
    'samosa':18,
    'sada dosa':45,
    'masala dosa':50,
    'pizza':60,
    'veg momo':40,
    'chiken momo':60,
    'veg burger':40,
    'chicken burger':60,
    'chiken biryani':100,
    'mutton biryani':150,
    'egg biryani':90,
    'veg biryani':85,
    'chicken 65':120,
    'chiken lolipop':100,
    'paneer 65':90,
    'paneer chili':90,
    'chiken chili':125,
    'vanilla':20,
    'chocolate':20,
    'strawberry':20,
    'mango':20,
    'pineapple':20
}

print('Welcome to Hotel Annpurna.\n          Menu')#hotel name
#printing all items in menu
print("         Nashata\n\n    Chai Rs:5\n    Vada pav Rs:15\n    Samosa Rs:20\n    Sada Dosa Rs:30\n    Masala Dosa Rs:40\n\n        starters\n     (veg and non-veg)\n    paneer chili Rs:90\n    paneer 65 Rs:90\n    chiken lolipop Rs:100\n    chiken chili Rs:125\n    chiken 65 Rs:120\n\n          Rice\n    (veg and non-veg)\n\n    chiken biryani Rs:100\n    mutton biryani Rs:150\n    egg biryani Rs:90\n    veg biryani Rs:85\n\n        Fast food\n    (veg and non-veg)\n\n    pizza Rs:60\n    veg momo Rs:40\n    veg burger Rs:40\n    chiken momo Rs:60\n    chicken burger Rs:60\n\n        Dessert\n    vanilla Rs:20\n    chocolate Rs:20\n    strawberry Rs:20\n    mango Rs:20\n    pineapple Rs:20\n\n")

order_total=0 #to add item prize
#Order
while True:
    #item 1
    item_1=input('Plese enter Your order here. (one at a time): ').lower()
    print('if you are done with your order then type "done".')
    if item_1 == 'done'.lower():
        break
    elif item_1 in menu:
        order_total += menu[item_1]
        print('Your item',item_1,'added to order.\n')
    else:
        print('Please order somthing from menu.\n')

#anything_else
anything_else=input('Do you want anything else? (Yes/No)')
if anything_else == 'Yes'.lower():
    #item 2
    while True:
        Item_2=input('Please enter your order. (here one at a time): ').lower()
        print('if you are done with your order then type "done".')
        if Item_2 == 'done'.lower():
            break
        elif Item_2 in menu:
            order_total+=menu[Item_2]
            print('Your Item',Item_2,'added to order.\n')
        else:
            print('Please order somthing from menu.\n')
else:
    print(end='')
print('\nYour total bill is',order_total)
print('Thank you for visiting')
