#Basic Project1 HOTEL MENU
import datetime

# ------------------ MENU ------------------ #
menu = {
    # Nashta
    "chai": 10,
    "vada pav": 20,
    "samosa": 20,
    "sada dosa": 35,
    "masala dosa": 45,
    "pohe":20,
    "mendu vada":30,

    # Veg Main Course
    "veg biryani": 85,
    "veg bambu biryani":150,
    "veg schezwan rice": 100,
    "veg triple rice": 120,

    # Non-Veg Main Course
    "chicken biryani": 120,
    "mutton biryani": 150,
    "egg biryani": 90,
    "bambu biryani": 180,
    
    #starter
    "paneer 65": 90,
    "paneer chili": 90,
    "chicken 65": 120,
    "chicken lolipop": 100,
    "chicken chili": 125,
    
    # Fast Food
    "pizza": 60,
    "veg burger": 50,
    "veg momo": 60,
    "paneer chili": 90,
    "chicken burger": 60,
    "chicken momo": 80,

    # Dessert
    "vanilla": 20,
    "chocolate": 20,
    "strawberry": 20,
    "mango": 20,
    "pineapple": 20
}

# ------------------ CUSTOMER DETAILS ------------------ #
print("\n====================================")
print("        WELCOME TO HOTEL ANNPURNA")
print("====================================\n")

customer_name = input("Enter Customer Name: ").title()

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M %p")

# ------------------ MENU CATEGORIES ------------------ #
menu_categories = {
    "🍵 NASHTA": [
        "chai", "vada pav", "samosa", "sada dosa",
        "masala dosa", "pohe", "mendu vada"
    ],

    "🥦 VEG MAIN COURSE": [
        "veg biryani", "veg bambu biryani",
        "veg schezwan rice", "veg triple rice"
    ],

    "🍗 NON-VEG MAIN COURSE": [
        "chicken biryani", "mutton biryani",
        "egg biryani", "bambu biryani"
    ],

    "🔥 STARTERS": [
        "paneer 65", "paneer chili",
        "chicken 65", "chicken lolipop",
        "chicken chili"
    ],

    "🍕 FAST FOOD": [
        "pizza", "veg burger", "veg momo",
        "chicken burger", "chicken momo"
    ],

    "🍨 DESSERT": [
        "vanilla", "chocolate", "strawberry",
        "mango", "pineapple"
    ]
}

# ------------------ DISPLAY MENU ------------------ #
print("\n--------------- MENU ---------------")

for category, items in menu_categories.items():
    print(f"\n{category}")
    for item in items:
        print(f"{item.title():25} Rs {menu[item]}")

print("------------------------------------\n")


# ------------------ ORDER SECTION ------------------ #
order_total = 0
ordered_items = {}

while True:
    user_input = input("Enter item (or item + quantity) or type 'done': ").lower()

    if user_input == "done":
        break

    parts = user_input.split()

    try:
        # If user gives only item name → default quantity = 1
        if len(parts) == 1:
            item = parts[0]
            qty = 1

        # If user gives item + quantity
        else:
            item = " ".join(parts[:-1])
            qty = int(parts[-1])

        if item in menu and qty > 0:
            total_price = menu[item] * qty
            order_total += total_price

            if item in ordered_items:
                ordered_items[item] += qty
            else:
                ordered_items[item] = qty

            print(f"✔ {item.title()} x{qty} added | Rs {total_price}\n")

        else:
            print("❌ Item not available or invalid quantity.\n")

    except ValueError:
        print("⚠ Invalid format! Example: pizza 2 OR chai\n")


# ------------------ INVOICE ------------------ #
print("\n\n====================================")
print("             INVOICE")
print("====================================")
print(f"Customer Name : {customer_name}")
print(f"Date          : {date}")
print(f"Time          : {time}")
print("------------------------------------")

for item, qty in ordered_items.items():
    price = menu[item]
    total = price * qty
    print(f"{item.title():20} x{qty:<3} Rs {total}")

print("------------------------------------")

gst = order_total * 0.05
grand_total = order_total + gst

print(f"Subtotal      : Rs {order_total}")
print(f"GST (5%)      : Rs {gst:.2f}")
print(f"Grand Total   : Rs {grand_total:.2f}")
print("====================================")
print("Thank You! Visit Again.")


