from admin import Admin
from admin_sys import AdminSys
from database import Database
from menu import Menu
from customer import Customer
from payment import Payment

# ID, Product, Price, Stock
vending_machine = [
    [1, "Coca-Cola", 3.75, 2],
    [2, "Pepsi", 3.67, 5],
    [3, "Monster", 9.96, 1],
    [4, "Café", 1.25, 100],
    [5, "Redbull", 13.99, 2]
]

# Note value, Available, Used
notes = [
    [100 * 100, 30, 0],
    [50 * 100, 30, 0],
    [20 * 100, 30, 0],
    [10 * 100, 30, 0],
    [5 * 100, 30, 0],
    [2 * 100, 30, 0],
    [1 * 100, 30, 0],
    [0.5 * 100, 30, 0],
    [0.25 * 100, 30, 0],
    [0.10 * 100, 30, 0],
    [0.05 * 100, 30, 0],
    [0.01 * 100, 30, 0]
]

menu = Menu()
database = Database()
ADMIN_PASSWORD = int(open("password.txt", "r").read())

while True:
    mode = menu.mode_selection()  # Return Menu Mode [ADM, Customer, Exit]
    if mode == 1:
        # Administrator mode
        admin_system = AdminSys()
        admin = Admin()
        if admin_system.validation() == ADMIN_PASSWORD: # Verify if ADM password is RIGHT
            while True:
                admin_mode = admin_system.show()
                if admin_mode == 0: # Get out of ADM Loop, return to Menu
                    break
                if admin_mode == 1: # Add new products
                    new_product = admin.add(vending_machine)
                if admin_mode == 2: # Remove products
                    product_to_be_removed = admin.remove(vending_machine)
                if admin_mode == 3: # Edit products
                    product_to_be_edited = admin.edit(vending_machine)
                if admin_mode == 4: # Show products matrix
                    print()
                    product_list = database.show(vending_machine)
                    print()
                if admin_mode == 5: # Modify available value for note/coin [Default: 30]
                    coin_value = float(
                        input("Insert the value of R$ to be modified: "))
                    edit_prices = admin.edit_cash(notes, coin_value)

    if mode == 2:
        # Customer mode
        while True:
            customer = Customer()
            print()
            database.show(vending_machine) # Print vending machine products
            print()
            product_id = int(
                input("[ ID ] - Choose the product to buy: "))
            if product_id == 0: # Return to mode selection [ADM, Customer, Exit]
                break
            else:
                # Checks ID Range (Returns True or False)
                id_for_validation = customer.id_validation(
                    vending_machine, product_id)
                if id_for_validation == True:
                    stock_for_validation = customer.stock_validation(
                        vending_machine, product_id)  # Check if stock > 0
                    if stock_for_validation == True:
                        payment = Payment()
                        price = payment.get_price(
                            vending_machine, product_id) # Return price from chosen product
                        customer_payment = float(
                            input("[ R$ ] - Enter the payment: "))
                        customer_payment = (customer_payment * 100) # The payment is convert to INT
                        change_value = payment.get_change(
                            customer_payment, price) # Return change value
                        give_change = payment.change(change_value, notes) # Verify if the purchase is possible, may print change.
                        if give_change is not None:
                            customer.down_stock(vending_machine, product_id) # -1 from stock
                        else:
                            print(
                                "Not enough cash deposited in machine! Purchase canceled.")
    if mode == 0:
        print("\nThe vending machine is now closed.")
        break
