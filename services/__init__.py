from services.admin import Admin, AdminSys
from services.customer import Customer
from services.database import Database
from services.menu import Menu
from services.payment import Payment

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
ADMIN_PASSWORD = int(open("config/password.txt", "r").read())
