from services import *

def main():
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
                        admin.add(vending_machine)
                    if admin_mode == 2: # Remove products
                        admin.remove(vending_machine)
                    if admin_mode == 3: # Edit products
                        admin.edit(vending_machine)
                    if admin_mode == 4: # Show products matrix
                        print()
                        database.show(vending_machine)
                        print()
                    if admin_mode == 5: # Modify available value for note/coin [Default: 30]
                        coin_value = float(
                            input("Insert the value of R$ to be modified: "))
                        admin.edit_cash(notes, coin_value)
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

if __name__ == '__main__':
    main()
