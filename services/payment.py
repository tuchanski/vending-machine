class Payment:
    def __init__(self) -> None:
        pass

    def get_change(self, payment, price):
        change = 0

        while payment < price:
            payment = float(
                input("Deposited value is not enough. Try again: "))
        else:
            change = (int(payment) - int(price))
            print(f"The change is R$ {change/100}")
            return change

    def get_price(self, matrix, product_id):
        price = 0
        for row in range(len(matrix)):
            if matrix[row][0] == product_id:
                price = matrix[row][2] * 100
        return price

    def change(self, change, notes):

        availability_change = []

        for values in range(0, len(notes)):
            availability_change.append(notes[values][1])

        temp = change

        for row in range(len(notes)):
            while notes[row][0] <= temp and availability_change[row] > 0:
                temp -= notes[row][0]
                availability_change[row] -= 1

        if temp > 0:
            return None

        else:
            for row in range(len(notes)):
                if availability_change[row] < notes[row][1]:
                    print(
                        f"{notes[row][1] - availability_change[row]} units of R$ {(notes[row][0])/100}")
                notes[row][1] = availability_change[row]
            return notes
