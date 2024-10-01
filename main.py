from services import *

def main():
    while True:
        mode = menu.mode_selection()  # Return Menu Mode [ADM, Customer, Exit]
        if mode == 1:
            admin_mode()
        elif mode == 2:
            customer_mode()
        elif mode == 0:
            print("\nThe vending machine is now closed.")
            break

def admin_mode():
    admin_system = AdminSys()
    admin = Admin()
    if admin_system.validation() == ADMIN_PASSWORD:
        while True:
            admin_mode = admin_system.show()
            if admin_mode == 0:
                break
            handle_admin_actions(admin_mode, admin)

def handle_admin_actions(admin_mode, admin):
    if admin_mode == 1:  # Add new products
        admin.add(vending_machine)
    elif admin_mode == 2:  # Remove products
        admin.remove(vending_machine)
    elif admin_mode == 3:  # Edit products
        admin.edit(vending_machine)
    elif admin_mode == 4:  # Show products matrix
        print()
        database.show(vending_machine)
        print()
    elif admin_mode == 5:  # Modify available value for note/coin [Default: 30]
        coin_value = float(input("Insert the value of R$ to be modified: "))
        admin.edit_cash(notes, coin_value)

def customer_mode():
    customer = Customer()
    while True:
        print()
        database.show(vending_machine)  # Print vending machine products
        print()
        product_id = int(input("[ ID ] - Choose the product to buy: "))
        if product_id == 0:  # Return to mode selection [ADM, Customer, Exit]
            break
        process_customer_purchase(customer, product_id)

def process_customer_purchase(customer, product_id):
    id_valid = customer.id_validation(vending_machine, product_id)
    if id_valid:
        stock_valid = customer.stock_validation(vending_machine, product_id)  # Check if stock > 0
        if stock_valid:
            payment = Payment()
            price = payment.get_price(vending_machine, product_id)  # Return price from chosen product
            customer_payment = float(input("[ R$ ] - Enter the payment: "))
            customer_payment = customer_payment * 100  # Convert to INT
            change_value = payment.get_change(customer_payment, price)  # Return change value
            give_change = payment.change(change_value, notes)  # Verify if the purchase is possible
            if give_change is not None:
                customer.down_stock(vending_machine, product_id)  # -1 from stock
            else:
                print("Not enough cash deposited in machine! Purchase canceled.")

if __name__ == '__main__':
    main()
