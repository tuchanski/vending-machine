
# Vending Machine

This project emulates a vending machine using Python, implementing functions and matrix concepts to manage the products and transactions.
This project was created for the **Algorithmic Logic** course during the first semester of the **Bachelor's in Computer Science at PUCPR**. It leverages matrix operations and uses methods within classes to manage the vending machine's functionalities.

## Features

- Purchase a beverage by inserting Brazilian currency notes and coins.
- Default available beverages:
  
  | ID | Product    | Price  | Stock |
  |----|------------|--------|-------|
  | 1  | Coca-cola  | 3.75 | 2     |
  | 2  | Pepsi      | 3.67 | 5     |
  | 3  | Monster    | 9.96 | 1     |
  | 4  | Coffee     | 1.25 | 100   |
  | 5  | Redbull    | 13.99 | 2     |

- Validates the availability of the chosen beverage and ensures payment is enough.
- Calculates and returns the change using the fewest possible notes and coins.
- Dynamically updates the stock after each purchase.

## User Instructions

1. The machine awaits the customer to select a beverage by entering its code.
2. The customer is prompted to insert money until it matches or exceeds the beverage price.
3. The machine will calculate and return the change, specifying the notes and coins given.
4. If the input is `0`, the customer can return to the menu.

## Admin Mode

- To access Admin Mode, enter the password `17102004`.
- Admin Mode allows the addition, removal, and updating of products dynamically.
- The program also considers the stock of available notes and coins to manage change. If there is insufficient change, the purchase is canceled.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Navigate to the project directory and run the Python file:
    ```bash
    cd vending-machine
    python main.py
    ```

## Author

- [Guilherme Tuchanski Rocha | GitHub](https://github.com/tuchanski)
