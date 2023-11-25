class Customer:
    def __init__(self) -> None:
        pass

    def id_validation(self, matrix, product_id):
        saved_id = False

        for row in range(len(matrix)):
            if product_id == matrix[row][0]:
                return True

        if saved_id == False:
            print(f"The ID {product_id} does not exist.")
            return False

    def stock_validation(self, matrix, product_id):
        for row in range(len(matrix)):
            if product_id == matrix[row][0]:
                if matrix[row][3] > 0:
                    print(
                        f"The product with ID {product_id} has {matrix[row][3]} units available.")
                    return True
                else:
                    print(f"The product with ID {product_id} is not available due to no stock.")
                    return False
    
    def down_stock(self, matrix, product_id):
        for row in range(len(matrix)):
            if matrix[row][0] == product_id:
                matrix[row][3] -= 1  # Remove 1 from stock
