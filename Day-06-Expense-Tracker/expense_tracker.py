import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except Exception:
        return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    category = input("Enter category (e.g., Food, Travel, Books,): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("\nInvalid amount entered. Please enter a number.\n")
        return

    description = input("Enter description: ").strip()

    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("\nExpense added successfully!\n")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n" + "="*45)
    print(" ALL EXPENSES")
    print("="*45)
    total = 0
    for idx, item in enumerate(expenses, 1):
        print(f"{idx}. [{item['category']}] {item['description']} - Rs. {item['amount']:.2f}")
        total += item['amount']
    print("="*45)
    print(f" Total Spent: Rs. {total:.2f}")
    print("="*45 + "\n")

def main():
    expenses = load_expenses()
    while True:
        print("Select an Option:")
        print("1. Add Expense")
        print("2. View All Expenses & Total")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice selected. Please try again.\n")

if __name__ == "__main__":
    main()