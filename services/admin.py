class Admin:
    def __init__(self) -> None:
        pass

    def add(self, matrix):
        new_row = []

        product_id = 0
        for row in range(len(matrix)):
            product_id = ((matrix[row][0])) + 1

        product_name = str(input("Enter a name: "))
        product_price = float(input("Enter a price: "))
        product_stock = int(input("Enter how many products are in stock: "))

        new_row = [product_id, product_name, product_price, product_stock]
        matrix.append(new_row)

    def remove(self, matrix):
        product_id = int(input("Insert an ID to be removed: "))
        save_row = 0

        for row in range(len(matrix)):
            if matrix[row][0] == product_id:
                save_row = matrix[row]

        if save_row != None:
            matrix.remove(save_row)
        else:
            print("ID has not been found!")

    def edit(self, matrix):
        product_id = int(input("Insert an ID to be modified: "))
        id_validation = False

        for row in range(len(matrix)):

            if matrix[row][0] == product_id:
                id_validation = True

                product_name = str(
                    input(f"Insert a new name for product with ID {product_id}: "))
                product_price = float(
                    input(f"Insert a new price for product with ID {product_id}: "))
                product_stock = int(
                    input(f"Insert how many products with ID {product_id} are available in stock: "))

                matrix[row] = [product_id, product_name,
                               product_price, product_stock]

        if id_validation == False:
            print("Id has not been found!")
    
    def edit_cash(self, matrix_notes, coin_value):

        note_found = False

        for row in range(len(matrix_notes)):
            if matrix_notes[row][0] == (coin_value * 100):
                print("\nYou can set the amount of notes/coins available. Be sure the value is equal or above 0.\n")
                print(f"Current value of R$ available for {coin_value}: {matrix_notes[row][1]}")
                deposit = int(input(f"Choose the new amount of R$ to be deposited in [{coin_value}] section: "))
                while deposit < 0:
                    deposit = int(input(f"Invalid input! The amount for {coin_value} must be equal or above R$ 0. Try again: "))
                else:
                    matrix_notes[row][1] = deposit
                    note_found = True
        
        if note_found == False:
            print("Value not found.")

class AdminSys:
    def __init__(self) -> None:
        pass

    def validation(self):
        print("\nTo enter in Admin mode, you must log-in.")
        password = int(input("Enter the password here: "))
        return password

    def show(self):
        print(
            "\n- Administrator Mode -\n[ 1 ] - Add products\n[ 2 ] - Remove products\n[ 3 ] - Edit products\n[ 4 ] - See products\n[ 5 ] - Edit Cash \n[ 0 ] - Back to menu")
        mode = int(input("Choose here: "))

        while mode != 1 and mode != 2 and mode != 3 and mode != 4 and mode != 5 and mode != 0:
            mode = int(input("Invalid input. Try again: "))

        else:
            return mode