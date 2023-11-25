class Database:
    def __init__(self) -> None:
        pass

    def show(self, matrix):
        print("ID | Name | Price | Stock")
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                print(matrix[row][column], end=" ")
            print()
